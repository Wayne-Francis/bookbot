def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

from stats import get_num_words
