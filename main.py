#!/usr/bin/python3
"""
    This is book bot project
"""


def count_words(text):
    """
    Count words of a given text
    """
    return len(text.split())


def chars_appearence_count(text):
    """
    Number of times each character appears in the given string
    """
    char_count = {}
    text = text.lower()
    for char in text:
        if not char.isalpha():
            continue
        if char not in char_count:
            char_count[char] = 1
            continue
        char_count[char] += 1
    return char_count


def main():
    """
    This is the main function of the program.
    """
    with open("./books/frankenstein.txt") as f:
        file_content = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count_words(file_content)} words found in the document")
        print("")
        char_count = chars_appearence_count(file_content)
        for char, count in char_count.items():
            print(f"The '{char}' character was found {count} times")
        print("--- End report ---")


main()
