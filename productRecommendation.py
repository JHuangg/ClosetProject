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

def provide_sentiment():
    with open("reviews.txt", "r") as f:
        reviews = f.readlines()
        
    review_polarity = []
    for i in range(len(reviews)):
        result = sentiment_vader(reviews[i])
        review_polarity.append(result)

    return(review_polarity)