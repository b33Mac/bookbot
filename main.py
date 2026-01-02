from stats import get_book_text, count_words, character_count, sort_on, list_of_dictionary
def main():
    words = get_book_text("./books/frankenstein.txt")
    count = character_count(words)
    organised_count = list_of_dictionary(count)
    
    
    print(organised_count)
    #print(count)
    #print(f"Found {count_words(words)} total words")


main()