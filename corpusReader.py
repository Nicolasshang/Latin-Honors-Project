from cltk.corpus.utils.importer import CorpusImporter
from cltk.corpus.readers import get_corpus_reader

class CorpusReader:
  corpus_importer = CorpusImporter("latin")
  
  def __init__(self, name):
    self.name = name
  
  def get_corpora(self):
    print(self.corpus_importer.list_corpora)
  
  def import_corpus(self, name):
    self.corpus_importer.input_corpus(name)

  def read_corpus(self, start, end):
    corpus_reader = get_corpus_reader(corpus_name = self.name, language = "latin")

    try:
      sentences = list(corpus_reader.sents())[start : end]
    except IndexError:
      print("Indices out of bounds")
      pass

    for sentence in sentences:
      print(sentence, "\n")

if __name__ == "__main__":
  name = input("Enter name: ")
  start = input("Enter start: ")
  end = input("Enter end: ")

  reader = CorpusReader(name)
  reader.read_corpus(start, end)