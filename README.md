# Pangram Reddit Bot
A bot that identifies pangrams in Reddit posts and titles

A pangram is a sentence that uses every letter in the alphabet, the most famous being "The quick brown fox jumps over the lazy dog".

This bot watches your selected subreddits and if a user submits a post with either the body or the title containing a pangram, it replies to it telling them so. Specifically it replies:
"Hey! Your sentence, `{sentence}` contains every letter of the alphabet!".

## Running the bot

### Requirements:

- **Reddit Account**
- **Client ID & Client Secret:** These two values are needed to access Reddit’s API as a script application (see Authenticating via OAuth for other application types). If you don’t already have a client ID and client secret, follow Reddit’s First Steps Guide to create them.
- **User Agent:** A user agent is a unique identifier that helps Reddit determine the source of network requests. To use Reddit’s API, you need a unique and descriptive user agent. The recommended format is <platform>:<app ID>:<version string> (by u/<Reddit username>). For example, android:com.example.myredditapp:v1.2.3 (by u/kemitche). Read more about user agents at Reddit’s API wiki page.

### Setup

#### 1. Install all the requirements
In your terminal run `pip install -r requirements.txt`. It may also be a good idea to setup a virtual environment before doing so.

#### 3. Add your API credentials to the Python script
Create a `.env` file in the root directory of the project. In this file paste the following lines:
```
REDDIT_CLIENT_ID="<client id>"
REDDIT_CLIENT_SECRET="<client_secret>"
REDDIT_USERNAME="<username>"
REDDIT_PASSWORD="<password>"
```

For example, if your key was `1234` and your secret was `5678` then your code would like like this:
```
REDDIT_CLIENT_ID="1234"
REDDIT_CLIENT_SECRET="5678"
```

#### 4. Run the script
Run the script by running `python sentence_pangram.py`. 

### Testing

Test by running `pytest` in the terminal.


