from textblob import TextBlob
import nltk
from newspaper import Article

# get article
url = 'http://everythingcomputerscience.com/'
article = Article(url)

# do some NLP
article.download()
article.parse()
nltk.download('punkt')
article.nlp()

# get the summary of the article
text = article.summary
print(text)

# create a textblob object
obj = TextBlob(text)

# this returns a value between -1 and 1
sentiment = obj.sentiment.polarity
print(sentiment)

# -1<negative<0 ,  0=neutral , 0<positive<1
if sentiment == 0:
    print("The text is neutral")
elif sentiment > 0:
    print("The text is positive")
else:
    print("The text is negative")

########        Using TextBlob Library          ######

# Language Translation
# text = TextBlob("Simple is better than complex")
# text_blob_obj =text.translate(to="tr")
# print(text_blob_obj)

# #Spelling Corrections
# text = 'I love to watchf footbal, but I have neter played it'
# text_blob_obj = TextBlob(text)
# print(text_blob_obj.correct())

# Converting to Upper and Lowercase
# text = "I love to watch football, but I have never played it"
# text_blob_obj = TextBlob(text)
# print(text_blob_obj.upper())

# Tokenization
# document = ("In computer science, artificial intelligence (AI), \
#             sometimes called machine intelligence, is intelligence \
#             demonstrated by machines, in contrast to the natural intelligence \
#             displayed by humans and animals. Computer science defines AI \
#             research as the study of \"intelligent agents\": any device that \
#             perceives its environment and takes actions that maximize its\
#             chance of successfully achieving its goals.[1] Colloquially,\
#             the term \"artificial intelligence\" is used to describe machines\
#             that mimic \"cognitive\" functions that humans associate with other\
#             human minds, such as \"learning\" and \"problem solving\".[2]")

# text_blob_obj = TextBlob(document)
# document_sentence = text_blob_obj.sentences
# print(document_sentence)
# print(len(document_sentence))

# document_word = text_blob_obj.word
# print(document_word)
# print(len(document_word))
