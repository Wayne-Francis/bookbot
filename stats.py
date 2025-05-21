def get_num_words(book_string):
    words = book_string.split()
    count = len(words)
    return count 

def get_num_character(book_string):
    string_count = {}
    book_string = book_string.lower()
    for s in book_string:
        if s in string_count:
            string_count[s] += 1
        else:
            string_count[s] = 1
    return string_count   