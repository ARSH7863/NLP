import re

s = "Mutual fund investments are subject to market risks. Read whole scheme related documents and invest carefully."


def generate_ngrams(s, n):
    s = s.lower()
    s = re.sub(r"[^A-zA-Z0-9\s]", "", s)
    token = [token for token in s.split(" ") if token != ""]
    ngrams = zip(*[token[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]


generate_ngrams(s, n=3)
