# Function to count the number of words in a string
def count_words(input_string):
    # Split the input string into words using space as the delimiter
    words = input_string.split()
    # Return the number of words
    return len(words)

# Input string
input_string = input("Enter a string: ")

# Call the function to count words and print the result
word_count = count_words(input_string)
print("Number of words:", word_count)

