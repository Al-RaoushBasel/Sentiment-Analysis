import os
from twitter_scraper import fetch_tweets
from sentiment_analysis import analyze_sentiment, save_sentiment_results
import pandas as pd
import subprocess


def main():
    # Fetch tweets and save them
    print("Fetching tweets...")
    tweets = fetch_tweets()

    if tweets:
        df = pd.DataFrame(tweets)
        df.to_csv("tweets.csv", index=False)
        print("Tweets saved to tweets.csv.")

        # Perform sentiment analysis and save the results
        print("Analyzing sentiment...")
        sentiment_df = analyze_sentiment(df)
        save_sentiment_results(sentiment_df)

    else:
        # If no new tweets, load the existing tweets and proceed with sentiment analysis
        print("No new tweets fetched. Using existing data.")
        df = pd.read_csv("tweets.csv")

        # Perform sentiment analysis on the existing data
        print("Analyzing sentiment on existing tweets...")
        sentiment_df = analyze_sentiment(df)
        save_sentiment_results(sentiment_df)

    # Run Streamlit app (in a subprocess)
    print("Running Streamlit app...")

    os.environ["PATH"] += os.pathsep + r"venv\Scripts"

    subprocess.run(["streamlit", "run", "app.py"])


if __name__ == "__main__":
    main()
