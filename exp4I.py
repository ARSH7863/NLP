# Experiment 4(1)
from nltk import CFG
from nltk.parse.generate import generate
import nltk

grammar1 = CFG.fromstring("""
S -> NP VP
NP -> Det N
NP -> Det ADJ N
VP -> V
VP -> V NP
Det -> 'the'|'a'
NP -> N
N -> 'dogs'
V -> 'cried'
""")

sentence = "the dogs cried".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sentence):
    print(tree)
