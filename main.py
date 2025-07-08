from textblob import TextBlob
from newspaper import Article

with open('text.txt', 'r') as file:
    text = file.read()
    
url = 'https://www.bbc.com/news/articles/cze10y59j91o'    #PLACE YOUR NEWS ARTICLE HERE
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob = TextBlob(text)
sentiment=blob.sentiment.polarity
print(sentiment)
