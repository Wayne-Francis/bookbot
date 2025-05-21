def get_num_words():
    book_string = get_book_text("books/frankenstein.txt")
    words = book_string.split()
    count = len(words)
    print(f"{count} words found in the document")