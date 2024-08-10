import os
import pickle
from extract_text import extract_text_from_pdf, extract_text_from_docx

def create_corpus(directory):
    corpus = []
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            text = extract_text_from_pdf(os.path.join(directory, filename))
            corpus.append(text)
            # add also .doc
        elif filename.endswith('.docx'):
            text = extract_text_from_docx(os.path.join(directory, filename))
            corpus.append(text)
    return corpus

def save_corpus(corpus, filepath='corpus/corpus.pkl'):
    with open(filepath, 'wb') as file:
        pickle.dump(corpus, file)

if __name__ == "__main__":

    directory = 'data/'

    corpus = create_corpus(directory)
    save_corpus(corpus)

