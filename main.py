def main():
    # Define the path to the file
    path_to_file = 'books/frankenstein.txt'
    
    # Open the file and read its contents
    with open(path_to_file, 'r') as f:
        file_contents = f.read()
    
    # Print the contents of the file to the console
    #print(file_contents)
    
    # Count and print the number of words in the file
    word_count = count_words(file_contents)
    #print(f'The number of words in the book is: {word_count}')
    
    # Count and print the frequency of each character
    char_count = count_characters(file_contents)
    print_report(char_count)

def count_words(text):
    # Split the text into words and return the count
    words = text.split()
    return len(words)

def count_characters(text):
    # Create a dictionary to hold character counts
    char_count = {}
    
    # Convert text to lowercase to ensure case insensitivity
    text = text.lower()
    
    # Count each character in the text
    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
            
    return char_count

def print_report(char_count):
    # Convert the character count dictionary to a list of dictionaries for sorting
    char_list = [{"char": char, "num": count} for char, count in char_count.items()]
    
    # Sort the list by the number of occurrences in descending order
    char_list.sort(reverse=True, key=lambda x: x["num"])
    
    # Print the report
    print("\n--- Begin report of books/frankenstein.txt ---")
    print(f"{sum(count['num'] for count in char_list)} words found in the document\n")
    
    for entry in char_list:
        print(f"The '{entry['char']}' character was found {entry['num']} times")
    
    print("--- End report ---")

if __name__ == "__main__":
    main()
    