#!/usr/bin/python3
import sys
from stats import get_word_count, get_character_count, chars_dict_to_sorted_list

def argument_error_check():
    if len(sys.argv) < 2:
        print("Error: Not enough arguments, missing path to book.", file=sys.stderr)
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("Error: Too many arguments.", file=sys.stderr)
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def get_book_text(book_path: str) -> str:
    with open(book_path, encoding="utf-8") as f:
        book_text: str = f.read()
    return book_text

def file_error_check(book_path: str) -> str:
    try:
        book_text: str = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: The file at {book_path} was not found.", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied for {book_path}. Check your file access.", file=sys.stderr)
        sys.exit(1)
    except IsADirectoryError:
        print(f"Error: {book_path} is a directory, not a file.", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Error: {book_path} contains non-text data.", file=sys.stderr)
        sys.exit(1)
    return book_text


def print_report(book_path: str, word_count: int, sorted_character_list: list[tuple[str, int]]):
    print("=========== BOOKBOT =============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------") 
    for t in sorted_character_list:
        if t[0].isalpha():
            print(t[0] + ":", t[1])
    print("============= END ===============")


def main():
    argument_error_check()
    book_path: str = sys.argv[1]
    book_text: str = file_error_check(book_path)
    word_count: int = get_word_count(book_text)
    character_dict: dict[str, int] = get_character_count(book_text)
    sorted_character_list: list[tuple[str, int]] = chars_dict_to_sorted_list(character_dict)
    print_report(book_path, word_count, sorted_character_list)

if __name__ == "__main__":
    main()









    
