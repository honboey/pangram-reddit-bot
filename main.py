import praw
import os
from dotenv import load_dotenv

# Load .env variables for authentication
load_dotenv()
reddit_client_id = os.getenv("REDDIT_CLIENT_ID")
reddit_client_secret = os.getenv("REDDIT_CLIENT_ID")
reddit_client_id = os.getenv("REDDIT_CLIENT_ID")
reddit_client_id = os.getenv("REDDIT_CLIENT_ID")

reddit = praw.Reddit(
  client_id=REDDIT
)