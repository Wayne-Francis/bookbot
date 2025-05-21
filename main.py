import sys

## line 4 updated to remove file_path as we are trying to remove hard coding - can return by adding file_path back in
def get_book_text(sys.argv):
    with open(sys.argv) as f:
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
    ## line 18 updated to remove /frankenstein.txt as we are trying to remove hard coding
    file_contents = get_book_text(sys.argv)
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