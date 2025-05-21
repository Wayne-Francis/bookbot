def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

from stats import get_num_words
from stats import get_num_character
from stats import dict_list
from stats import sort_on

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    file_contents = get_book_text("books/frankenstein.txt")
    count = get_num_words(file_contents)
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    characters = get_num_character(file_contents)
    sort_char = dict_list(characters)
    sort_char.sort(reverse=True,key=sort_on)
    for s in sort_char:
        char = s["char"]
        number = s["num"]
        if char.isalpha() == True:
            print(f"{char}: {number}")
main()