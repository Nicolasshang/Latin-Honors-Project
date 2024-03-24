from cltk.stem.latin.j_v import JVReplacer
from cltk.stem.latin.declension import CollatinusDecliner
from cltk.lemmatize.latin.backoff import BackoffLatinLemmatizer
from cltk.prosody.latin.macronizer import Macronizer
import re

# pl.txt is usually the test data
def read(name):
  with open(f"data/{name}", "r") as f:
    return f.read()

def write(name, text):
  with open(f"data/{name}", "w", encoding = "utf-8") as f:
    f.write(text)

# Replaces the j's with i's and v's with u's (and vice versa as well)
def replace_jv(text):
  replacer = JVReplacer()
  text = replacer.replace(text)
  return text

# Deletes everthing in square brackets or parenthesis, and removes excessive whitespace
def clean(text, lower=False):
  for i in range(2):
    text = re.sub(r"([\(\[].*?[\)\]])|( +[\.,:;!])", "", text)
  cleaned_data = re.sub(r" {2,}", " ", text)
  
  if lower:
    lower_cleaned_data = cleaned_data.lower()
    return (cleaned_data, lower_cleaned_data)

  return cleaned_data

# Find all wordforms when given a lemma (usually in the nom. sing.)
def decline(words):
  decliner = CollatinusDecliner()
  declined_words = {}
  for word in words:
    declined_word = decliner.decline(word)
    print(declined_word)

# Find the lemma using CLTK's backoff lemmatizer
def find_lemma(tokens):
  lemmatizer = BackoffLatinLemmatizer()
  tokens = lemmatizer.lemmatize(tokens)
  return tokens

# Add Macrons
def macronize(text):
  macronizer = Macronizer("tag_ngram_123_backoff")
  text = macronizer.macronize_text(text)
  return text

if __name__ == "__main__":
  text = read("pl.txt")
  text = replace_jv(text)
  text = clean(text)
  text = macronize(text)
  write("pl_macron.txt", text)