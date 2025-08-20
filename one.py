import nltk
nltk.download("punkt")
from nltk.tokenize import word_tokenize
text = "I am learning Python with libraries."
print(word_tokenize(text))
