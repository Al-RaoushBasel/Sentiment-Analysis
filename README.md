# Twitter Sentiment Analysis Dashboard 🐦

## Overview 🌍
This project analyzes the sentiment of tweets using a pre-trained Hugging Face model. It provides a user-friendly interface for entering tweets, fetching real-time tweets from Twitter, and visualizing sentiment distributions. The app is built using Streamlit for the frontend and uses the Hugging Face Transformers library for sentiment analysis.

## Features ✨
- **Sentiment Analysis:** Analyze the sentiment (Positive, Negative, or Neutral) of user-inputted tweets or pre-collected tweets. 🧠
- **Real-time Data Fetching:** Fetch the latest tweets from Twitter using the Twitter API and analyze them. 🔄
- **Data Visualization:** View sentiment distributions using bar charts to understand the general mood of the tweets. 📊
- **CSV Export:** Export the analyzed results as a CSV file for further use. 📥

### Live Demo 🚀
Check out the live version of the app here:  
[Twitter Sentiment Analysis Dashboard - Streamlit](https://baselalraoush.streamlit.app/)


## Technologies Used 🛠️
- **Python**: The main programming language used for the backend processing. 🐍
- **Streamlit**: The framework used to create an interactive frontend for visualizing results. 🌐
- **Hugging Face Transformers**: Pre-trained models used for sentiment analysis of tweets. 🤗
- **Matplotlib**: Used for creating visualizations like bar charts. 📉
- **Twitter API**: Fetches real-time tweets based on predefined queries. 🐦

## How to Use 🚀

### Setup:
1. **Clone this repository:**
    ```bash
    git clone https://github.com/your-username/twitter-sentiment-analysis.git
    ```
2. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3. **Create a `.env` file and add your Twitter API credentials:**
    ```bash
    TWITTER_BEARER_TOKEN=your_bearer_token
    ```

### Running the App:
1. Run the following command to start the app:
    ```bash
    streamlit run app.py
    ```

### Features:
- Enter your tweet or text to analyze its sentiment. 📝
- View sentiment analysis results for pre-collected tweets. 📈
- Download the analyzed results as a CSV. 💾

### Requirements 📜
- Python 3.7 or higher 🐍
- Streamlit 🌐
- pandas 📊
- Hugging Face Transformers 🤗
- Matplotlib 📈
- requests 📥
- dotenv (for environment variables) 🌳
- Twitter API access (for fetching tweets) 🐦

Feel free to fork, contribute, or open issues for improvements! 🔧

**Developed by**: Basel Al-Raoush 👨‍💻
