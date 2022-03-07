import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download("punkt")

sample_text = "I am Arsh Shaikh, and this is experiment one of NLP."
tokens = word_tokenize(sample_text, language="english")
print(tokens)
