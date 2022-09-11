from vaderSentiment import vaderSentiment

def sentiment_vader(sentence):
    # Sentiment intensity analyzer object
    obj = vaderSentiment.SentimentIntensityAnalyzer()

    resultPolarity = obj.polarity_scores(sentence)

    if resultPolarity['compound'] >= 0.05:
        return "positive"
    elif resultPolarity['compound'] <= -0.05:
        return "negative"
    else:
        return "neutral"

print(sentiment_vader("The movie was bad"))