import re
from cltk.stem.latin.j_v import JVReplacer

# pl.txt is the test data
with open("data/pl.txt", "r") as f:
  text = f.read()

# Replaces the j's with i's and v's with u's (and vice versa as well)
def replacejv(text):
  replacer = JVReplacer()
  text = replacer.replace(text)
  return text

# Deletes everthing in square brackets or parenthesis, and removes excessive whitespace
def clean(text, lower=False):
  for i in range(2):
    text = re.sub(r"([\(\[].*?[\)\]])|( +[\.,])", "", text)
  cleaned_data = re.sub(r" {2,}", " ", text)
  
  if lower:
    lower_cleaned_data = cleaned_data.lower()
    return (cleaned_data, lower_cleaned_data)

  return cleaned_data