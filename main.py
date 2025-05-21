def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

from stats import get_num_words

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    count = get_num_words(file_contents)
    print(f"{count} words found in the document")

main()