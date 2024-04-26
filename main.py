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


def determine_if_pangram_exists(x): ...
