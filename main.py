from stats import get_book_text, count_words, character_count, sort_on, list_of_dictionary

def main():
    words = get_book_text("./books/frankenstein.txt")
    count = character_count(words)
    organised_count = list_of_dictionary(count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(words)} total words")
    print("--------- Character Count -------")
    
    
    #for item in organised_count: 
    #for i in organised_count:
    #   print(organised_count[i["Char"]])



main()