'''Sentiment analysis using pythons'''

# import textblob module
from textblob import TextBlob

# 1st tweet example
tweet1 = "The food at Taj was awesome."

t1 = TextBlob(tweet1)

# printing sentiment score
print(t1.sentiment)

# 2nd tweet example
tweet2 = "The movie was not so good."

t2 = TextBlob(tweet2)

# printing sentiment score
print(t2.sentiment)
