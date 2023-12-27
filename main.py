def open_file(the_file_path):
    with open(the_file_path) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(the_file_path):
    the_book_string = open_file(the_file_path)
    return len(the_book_string.split())

def get_char_count(the_file_path):
    the_book_string = open_file(the_file_path)
    char_dict = {}
    word_list = the_book_string.split()
    for word in word_list:
        for char in word:
            if char.lower() in char_dict:
                char_dict[char.lower()] += 1
            else:
                char_dict[char.lower()] = 1
    return char_dict

def print_book_report(the_file_path):
    char_dict = get_char_count(the_file_path)
    sorted_dict = sorted(char_dict.items(), key=lambda x:x[1], reverse=True)

    print(f"--- Begin report of {the_file_path} ---")
    print(f"{get_word_count(the_file_path)} words found in the document")
    
    for item in sorted_dict:
        if item[0].isalpha():
            print(f"The '{item[0]}' character was found {item[1]} times")
    print("--- End Report ---")



file_path = 'books/frankenstein.txt' 

print_book_report(file_path)
