def main():
    file_path = 'books/frankenstein.txt'
    book_text = get_book_text(file_path)
    words_count = get_word_count(book_text)
    #print(words_count)
    letter_count_dict = get_letter_count(book_text)
    aphabet_dict = get_alphabet_dict(letter_count_dict)
    report_function(aphabet_dict, words_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    letter_dict = {}
    lower_case_text = text.lower()
    words = lower_case_text.split()
    for word in words:
        for letter in word:
            if letter not in letter_dict:
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1
    return letter_dict

def get_alphabet_dict(dict):
    aplhabet_dict = {}
    for key, value in dict.items():
        if key.isalpha():
            aplhabet_dict[key] = value
    
    sorted_list = sorted(aplhabet_dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_list

def report_function(tuple_list, words_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_count} words found in the document\n")
    for key, value in tuple_list:
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

main()

