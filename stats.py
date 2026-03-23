def get_word_count(book_text):
    word_list = book_text.split()
    word_count = len(word_list)
    return word_count

def get_character_count(book_text):
    character_dict = {}
    for character in book_text:
        character = character.lower()
        if character not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1
    return character_dict

def sort_on(d):
    return d["num"]

def sort_by_count(character_dict):
    sorted_list = []
    for key in character_dict:
        if key.isalpha():
            sorted_list.append({"char": key, "num": character_dict[key]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list




