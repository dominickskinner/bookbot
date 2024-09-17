def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    ###########################
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print(f"---Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")
    #########################

###
def get_num_words(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

###

def get_book_text(path):
    with open(path) as f:
        return f.read()
       #words = story.split()
        #dict = {}
        #for word in words:
           # lower_word = word.lower()
           # letters = [char for char in lower_word]
           # for letter in letters:
               # if letter in dict:
                   # dict[letter] += 1
               # else:
                   # dict[letter] = 1
            #dict.items()
            #sorted_dict = sorted(dict.items())
            #sorted_dict2 = sorted(sorted_dict, key=lambda d: d['name'])
            #list_from_dict = [(key, value) for key, value in dict.items()]
            #list_from_dict.sort(reverse=False)
            #print(list_from_dict(1))
            #my_letters = list(dict)
            #my_numbers = list(dict.values())
            #my_letters.sort()
        #return(sorted_dict2)

main()
