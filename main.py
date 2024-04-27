import praw
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
    user_agent="pangram_detector_bot:v1",
)


def main():
    determine_if_pangram_exists()


def determine_if_pangram_exists(str):
    """
    Str -> Boolean
    Take a string and determine if a pangram exists in it
    """


def string_has_over_25_letters(str):
    """
    Str -> Boolean
    Produce true if string has 26 letters or more
    """
    cleaned_str = ''.join(filter(str.isalpha, str))
    print(cleaned_str)
    if len(cleaned_str) > 25:
        return True
    else:
        return False


def isolate_z_sentence(str):
    """
    Str -> Str
    Take a string and if it has a 'z' then isolate that sentence
    """
