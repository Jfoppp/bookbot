def get_word_count(book_text: str)  -> int:
    word_list: list[str] = book_text.split()
    word_count: int = len(word_list)
    return word_count

def get_character_count(book_text: str) -> dict[str, int]:
    character_dict: dict[str, int] = {}
    for character in book_text:
        character = character.lower()
        if character not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1
    return character_dict

def sort_on(t: tuple[str, int]) -> int:
    return t[1]

def chars_dict_to_sorted_list(character_dict: dict[str, int]) -> list[tuple[str, int]]:
    character_list: list[tuple[str, int]] = []
    for key in character_dict:
        character_list.append((key, character_dict[key]))
    sorted_character_list: list[tuple[str, int]] = sorted(character_list, key=sort_on, reverse=True)
    return sorted_character_list

# def sort_by_count(character_dict):
#     sorted_list = []
#     for key in character_dict:
#         if key.isalpha():
#             sorted_list.append({"char": key, "num": character_dict[key]})
#     sorted_list.sort(reverse=True, key=sort_on)
#     return sorted_list




