from stats import count_words, get_chars_dict, sorted_list
import sys



def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()

def main():
    if len(sys.argv) == 2:   
        book_text = get_book_text(sys.argv[1])
        num_words = count_words(book_text)
        charachters_dictionary = get_chars_dict(book_text)
        last_sort = sorted_list(charachters_dictionary)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for item in last_sort:
            if item["char"].isalpha():
                print(f'{item["char"]}: {item["num"]}')
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)




main()



