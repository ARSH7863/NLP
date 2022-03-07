from polyglot.text import Text, Word
words = ["settlement", "carelessness", "almighty"]
for w in words:
    w = Word(w, language="en")
    print("{:<20}{}".format(w, w.morphemes))
