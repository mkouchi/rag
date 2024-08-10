import pickle
from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration

def load_corpus(filepath='corpus/corpus.pkl'):
    with open(filepath, 'rb') as file:
        corpus = pickle.load(file)
    return corpus

def load_rag_medel(corpus):
    tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")
    retriever = RagRetriever.from_pretrained("facebook/rag-token-nq", index_name="custom", passages=corpus)
    model = RagSequenceForGeneration.from_pretrained("facebook/rag-token-nq", retriever=retriever)
    return model, tokenizer


def generate_answer(model, tokenizer, input_text):
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids)
    return tokenizer.batch_decode(outputs, skip_special_tokens=True)


if __name__== "__main__":

    corpus = load_corpus()

    model, tokenizer = load_rag_medel(corpus)

    input_text = "What is Heterogeneous?"
    answer = generate_answer(model, tokenizer, input_text)
    print(answer)