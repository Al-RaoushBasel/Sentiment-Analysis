import streamlit as st
import pandas as pd
from transformers import pipeline
import matplotlib.pyplot as plt

# Initialize sentiment analysis model (using a pre-trained Hugging Face model)
model = pipeline("sentiment-analysis")

# Set up Streamlit title
st.title(" Twitter Sentiment Dashboard 🌍")

# Add some styling
st.markdown("""
    <style>
    .title {
        font-size: 40px;
        color: #4CAF50;
        font-weight: bold;
        text-align: center;
    }
    .header {
        font-size: 25px;
        color: #2196F3;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Add a subtitle to make it more engaging
st.markdown('<p class="header">Analyze Twitter sentiment in real time. Powered by AI & Hugging Face</p>', unsafe_allow_html=True)

# Option 1: Let users input their own tweet or text for sentiment analysis
user_input = st.text_input("Enter a tweet or text to analyze sentiment:")

# Add a progress bar while processing
if user_input:
    with st.spinner('Analyzing tweet...'):
        result = model(user_input)[0]  # Get sentiment result
        sentiment_label = result['label']
        sentiment_score = result['score']

        # Display the result with emoji-based sentiment
        sentiment_emoji = "😊" if sentiment_label == "POSITIVE" else "😞" if sentiment_label == "NEGATIVE" else "😐"
        st.markdown(f"### **Sentiment: {sentiment_emoji} {sentiment_label}**")
        st.write(f"Confidence: **{sentiment_score:.2f}**")

# Add a space for a divider
st.markdown("---")

# Option 2: Display pre-analyzed tweets from CSV (sentiment_results.csv)
st.header("📝 Analyzed Tweets")

# Load the sentiment results CSV file
df = pd.read_csv("sentiment_results.csv")

# Display a limited number of tweets as cards (cards are more visually appealing)
tweets_to_show = df.head(10)  # Show the top 10 tweets for simplicity

for index, row in tweets_to_show.iterrows():
    st.markdown(f"### Tweet #{index + 1}")
    st.markdown(f"**Tweet Text:** {row['text']}")
    st.markdown(f"**Sentiment:** {row['sentiment']} (Confidence: {row['confidence']:.2f})")
    st.markdown("---")

# Add a bar chart for sentiment distribution
st.header("📊 Sentiment Distribution")

sentiment_counts = df["sentiment"].value_counts()

# Customize the bar chart color to make it more appealing
fig, ax = plt.subplots()
sentiment_counts.plot(kind="bar", color=["#4CAF50", "#FF5722", "#2196F3"], ax=ax)
ax.set_xlabel('Sentiment')
ax.set_ylabel('Count')
ax.set_title('Sentiment Distribution')

# Show the bar chart in Streamlit
st.pyplot(fig)

# Add a download button for the sentiment results CSV
st.download_button(
    label="Download Analyzed Results as CSV",
    data=df.to_csv(index=False),
    file_name="sentiment_results.csv",
    mime="text/csv"
)

# End with a footer
st.markdown("---")
st.markdown('<p class="footer">Developed with ❤️ by Basel Al-Raoush</p>', unsafe_allow_html=True)
