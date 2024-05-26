def get_user_input():
    """Prompt the user to enter a sentence or paragraph and return the input."""
    return input("Please enter a sentence or paragraph: ").strip()
def count_words(text):
    """Count the number of words in the given text."""
    if not text:
        return 0
    words = text.split()
    return len(words)
def display_word_count(count):
    """Display the word count to the user."""
    print(f"The number of words in the entered text is: {count}")
def main():
    """Main function to run the Word Counter program."""
    print("Welcome to the Word Counter Program!")
    user_text = get_user_input()

    # Error handling for empty input
    if not user_text:
        print("You entered an empty string. Please enter a valid sentence or paragraph.")
    else:
        word_count = count_words(user_text)
        display_word_count(word_count)
if __name__ == "__main__":
    main()
