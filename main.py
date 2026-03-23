#!/usr/bin/python3
import sys
from stats import get_word_count, get_character_count, sort_by_count

def argument_error_check():
    if len(sys.argv) < 2:
        print("Error: Not enough arguments, missing path to book.", file=sys.stderr)
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("Error: Too many arguments.", file=sys.stderr)
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def get_book_text(book_path):
    with open(book_path, encoding="utf-8") as f:
        book_text = f.read()
    return book_text

def file_error_check(book_path):
    try:
        book_text = get_book_text(book_path)
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


def print_report(book_path, word_count, sorted_list):
    print("=========== BOOKBOT =============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for d in sorted_list:
        print(d["char"] + ":", d["num"])

    print("============= END ===============")


def main():
    argument_error_check()
    book_path = sys.argv[1]
    book_text = file_error_check(book_path)
    word_count = get_word_count(book_text)
    character_dict = get_character_count(book_text)
    sorted_list = sort_by_count(character_dict)
    print_report(book_path, word_count, sorted_list)

if __name__ == "__main__":
    main()









    
