import praw
import string
import re
import os
from dotenv import load_dotenv

# Load .env variables for authentication
load_dotenv()
reddit_client_id = os.getenv("REDDIT_CLIENT_ID")
reddit_client_secret = os.getenv("REDDIT_CLIENT_SECRET")
reddit_username = os.getenv("REDDIT_USERNAME")
reddit_password = os.getenv("REDDIT_PASSWORD")

reddit = praw.Reddit(
    client_id=reddit_client_id,
    client_secret=reddit_client_secret,
    password=reddit_password,
    username=reddit_username,
    user_agent="pangram_detector_bot:v1 (by /u/you-wrote-a-pangram)",
)


def main(): ...


def reproduce_pangram_if_it_exists(str):
    """
    Str -> Str
    Take a string and determine if a pangram exists in it
    """
    if string_has_over_25_letters(str):
        z_sentence = isolate_z_sentence(str)
        if determine_if_sentence_is_pangram(z_sentence):
            return z_sentence


def string_has_over_25_letters(str):
    """
    Str -> Boolean
    Produce true if string has 26 letters or more
    """
    # Create string of all punctuation and space
    chars_to_remove = " " + string.punctuation

    # Create translation table of characters to remove
    translation_table = str.maketrans("", "", chars_to_remove)

    cleaned_str = str.translate(translation_table)
    if len(cleaned_str) > 25:
        return True
    else:
        return False


def isolate_z_sentence(str):
    """
    Str -> Str
    Take a string and if it has a 'z' then isolate that sentence
    """
    if "z" in str.lower():
        separated_string = re.split(r"(?<=\w[.!?])\s", str)
        for sentence in separated_string:
            if "z" in sentence:
                return sentence
    else:
        return "No pangram"


def determine_if_sentence_is_pangram(str):
    """
    Str -> Boolean
    """
    # Create set of letters found in str
    letters_found = set()

    # Iterate over each character and if it is an alpha and not in letters_found, add it to letters_found
    for char in str.lower():
        if char.isalpha() and char not in letters_found:
            letters_found.add(char)

    return len(letters_found) == 26
