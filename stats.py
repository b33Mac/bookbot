#accepts filepath and returns the pritned text as a string
def get_book_text(book):
    with open(book) as f:
        wholebook = f.read()
    return wholebook


#accepts the string and returns total word count as int
def count_words(words):
    num_words = len(words.split())
    return num_words


"""
accepts string and returns dictionary with character
count in lower case only
"""
def character_count(words):
    lowercase = words.lower()
    characters = {}
    for character in lowercase:
        if character not in characters:
            characters[character] = 1
        elif character in characters:
            characters[character] += 1
    return characters

#creates sort key for sort
def sort_on(item):
    return item["num"]

#creates list of dicitonaries for each character
def list_of_dictionary(dictionary):
    char_list = []
    for character, number in dictionary.items():
        values = {"char":character, "num": number}
        char_list.append(values)
    char_list.sort(reverse=True, key=sort_on)
    return char_list 

