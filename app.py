import streamlit as st
import pandas as pd
from transformers import pipeline
import matplotlib.pyplot as plt

# Initialize sentiment analysis model (using a pre-trained Hugging Face model)
model = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

st.title(" Twitter Sentiment Dashboard 🌍")

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

st.markdown('<p class="header">Analyze Twitter sentiment in real time. Powered by AI & Hugging Face</p>', unsafe_allow_html=True)

user_input = st.text_input("Enter a tweet or text to analyze sentiment:")

model = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

if user_input:
    with st.spinner('Analyzing tweet...'):
        result = model(user_input)[0]  # Get sentiment result
        sentiment_label = result['label']
        sentiment_score = result['score']

        sentiment_emoji = "😊" if sentiment_label == "LABEL_1" else \
                          "😐" if sentiment_label == "LABEL_2" else \
                          "😞"
        sentiment_label_text = "POSITIVE" if sentiment_label == "LABEL_1" else \
                               "NEUTRAL" if sentiment_label == "LABEL_2" else \
                               "NEGATIVE"

        st.markdown(f"### **Sentiment: {sentiment_emoji} {sentiment_label_text}**")
        st.write(f"Confidence: **{sentiment_score:.2f}**")

st.markdown("---")

# Option 2: Display pre-analyzed tweets from CSV (sentiment_results.csv)
st.header("📝 Analyzed Tweets")

# Load the sentiment results CSV file
df = pd.read_csv("sentiment_results.csv")

tweets_to_show = df.head(15)

for index, row in tweets_to_show.iterrows():
    st.markdown(f"### Tweet #{index + 1}")
    st.markdown(f"**Tweet Text:** {row['text']}")
    st.markdown(f"**Sentiment:** {row['sentiment']} (Confidence: {row['confidence']:.2f})")
    st.markdown("---")

st.header("📊 Sentiment Distribution")

sentiment_counts = df["sentiment"].value_counts()

fig, ax = plt.subplots()
sentiment_counts.plot(kind="bar", color=["#4CAF50", "#FF5722", "#2196F3"], ax=ax)
ax.set_xlabel('Sentiment')
ax.set_ylabel('Count')
ax.set_title('Sentiment Distribution')

st.pyplot(fig)

st.download_button(
    label="Download Analyzed Results as CSV",
    data=df.to_csv(index=False),
    file_name="sentiment_results.csv",
    mime="text/csv"
)

st.markdown("---")
st.markdown('<p class="footer">Developed with ❤️ by Basel Al-Raoush</p>', unsafe_allow_html=True)
