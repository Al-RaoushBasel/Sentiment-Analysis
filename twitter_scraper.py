import requests
import os
from dotenv import load_dotenv
import pandas as pd

# Load environment variables
load_dotenv()

# Access the API keys and tokens from environment variables
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# Twitter API v2 endpoint for searching tweets
search_url = "https://api.twitter.com/2/tweets/search/recent"

def fetch_tweets(query="climate change OR technology OR politics OR sports OR AI OR Dubai OR Elon Musk OR World Cup", max_results=5):
    query_params = {
        'query': query,
        'max_results': max_results
    }

    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }

    response = requests.get(search_url, headers=headers, params=query_params)

    if response.status_code == 200:
        tweets = response.json().get('data', [])
        tweet_data = [{"text": tweet['text']} for tweet in tweets]

        # Check if 'tweets.csv' exists and append the new tweets
        if os.path.exists("tweets.csv"):
            df = pd.read_csv("tweets.csv")
            new_df = pd.DataFrame(tweet_data)
            df = pd.concat([df, new_df], ignore_index=True)  # Concatenate old and new tweets
        else:
            df = pd.DataFrame(tweet_data)  # If no file exists, create a new DataFrame

        # Save the combined data to 'tweets.csv'
        df.to_csv("tweets.csv", index=False)
        print("Saved new tweets to tweets.csv!")

    else:
        print(f"Error: {response.status_code}")
        return []

if __name__ == "__main__":
    fetch_tweets()
