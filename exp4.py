# Experiment 4(2)
import nltk
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *

# While running the prgram for the first time
# nltk.download("punkt")
# nltk.download("averaged_perceptron_tagger")

sentence = "I saw a dog roaming on street"
tokens = nltk.word_tokenize(sentence)
print(tokens)
tags = nltk.pos_tag(tokens)
print(tags)
pattern = """
NP:{<RP>?<JJ>*<LS>}
IN:{<IN>}
VBD:{<VBD>}
"""
npChunk = nltk.RegexpParser(pattern)
result = npChunk.parse(tags)
result.draw()
