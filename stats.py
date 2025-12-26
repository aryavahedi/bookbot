def count_words(book_text):
    num_words = len(book_text.split())
    return num_words

def get_chars_dict(book_text):
    chars_dict = {}
    for char in book_text:
        lowered = char.lower()
        if lowered in chars_dict:
            chars_dict[lowered] += 1
        else:
            chars_dict[lowered] = 1
    return chars_dict

def helper(items):
        return items["num"]
        
def sorted_list(dictionary):
    list_dictionary = []
    for char,count in dictionary.items():
        temporary_dict = {"char": char, "num": count}
        list_dictionary.append(temporary_dict)
    
    list_dictionary.sort(reverse=True, key=helper)
    return list_dictionary























