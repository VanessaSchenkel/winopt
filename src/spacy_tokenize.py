# Simple English tokenizer from stdin to stdout

import spacy
import fileinput

nlp = spacy.load("en_core_web_md", disable = ["parser", "ner"])
for line in fileinput.input():
    print(" ".join([word.text for word in nlp(line.strip())]))
