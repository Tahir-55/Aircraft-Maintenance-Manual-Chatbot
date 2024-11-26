from sentence_transformers import SentenceTransformer
from faiss import IndexFlatL2
from transformers import pipeline
import numpy as np

class Chatbot:
    def __init__(self, text_chunks, model_name='all-MiniLM-L6-v2', qa_model='deepset/roberta-base-squad2'):
        self.text_chunks = text_chunks
        self.model = SentenceTransformer(model_name)
        self.embeddings = self.model.encode(text_chunks)
        self.index = IndexFlatL2(self.embeddings.shape[1])
        self.index.add(np.array(self.embeddings))
        self.qa_pipeline = pipeline("question-answering", model=qa_model, tokenizer=qa_model)

    def search_similar(self, query, k=5):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_embedding), k)
        return [self.text_chunks[i] for i in indices[0]]

    def generate_response(self, question):
        context = "\n".join(self.search_similar(question))
        if len(context) > 1024:
            context = context[:1024]
        answer = self.qa_pipeline(question=question, context=context)
        return answer['answer']
