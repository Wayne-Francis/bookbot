def get_num_words(book_string):
    words = book_string.split()
    count = len(words)
    return count 

def get_num_character(book_string):
    string_count = {}
    #book_string = book_string.lower()
    for s in book_string:
        ### the isalpha added as I had extra 2 in moby dick - hopefully this corrects it
        if s.isalpha(): 
            s = s.lower()
            if s in string_count:
                string_count[s] += 1
            else:
                string_count[s] = 1
    return string_count   

def dict_list(dict):
    character = []
    for c, count in dict.items():
        character.append({"char": c, "num": count})
    return character

def sort_on(dict):
    return dict["num"]
