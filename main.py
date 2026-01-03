import sys
from stats import get_book_text, count_words, character_count, sort_on, list_of_dictionary

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_file = sys.argv[1]
    words = get_book_text(f"{book_file}")
    count = character_count(words)
    organised_count = list_of_dictionary(count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(words)} total words")
    print("--------- Character Count -------")
    
    for entry in organised_count:
        char = entry["char"]
        num = entry["num"]
        if char.isalpha() == True:
            print(f"{char}: {num}")
        

main()