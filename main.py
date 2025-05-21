def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_string = get_book_text("books/frankenstein.txt")
    words = book_string.split()
    count = len(words)
    print(f"{count} words found in the document")

main()

