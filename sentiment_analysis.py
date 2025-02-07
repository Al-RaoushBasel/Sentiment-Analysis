from transformers import pipeline
import pandas as pd


# Function to analyze sentiment on tweets
def analyze_sentiment(tweets_df, model_name="cardiffnlp/twitter-roberta-base-sentiment"):
    classifier = pipeline("sentiment-analysis", model=model_name)

    # Define a mapping for the labels
    label_map = {
        'LABEL_0': 'NEGATIVE',
        'LABEL_1': 'NEUTRAL',
        'LABEL_2': 'POSITIVE'
    }

    results = []
    for text in tweets_df["text"]:
        result = classifier(text)[0]
        sentiment_label = label_map[result["label"]]  # Map to readable sentiment label

        results.append({
            "text": text,
            "sentiment": sentiment_label,
            "confidence": result["score"]
        })

    return pd.DataFrame(results)


# Function to save the sentiment results to a CSV file
def save_sentiment_results(results_df, file_name="sentiment_results.csv"):
    results_df.to_csv(file_name, index=False)
    print(f"Sentiment analysis saved to {file_name}!")


# Main execution block
if __name__ == "__main__":
    # Load tweets from CSV
    df = pd.read_csv("tweets.csv")

    # Perform sentiment analysis
    sentiment_results = analyze_sentiment(df)

    # Save the results to a CSV file
    save_sentiment_results(sentiment_results)
