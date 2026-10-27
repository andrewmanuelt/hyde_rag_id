import bm25s
import Stemmer

class BM25Retriever:
    def __init__(self):
        self.index = None
        self.stemmer = Stemmer.steemer("indonesia")
        self.num_k = 100
        
    def create_index(self, corpus):
        corpus = []
        corpus_token = bm25s.tokenize(corpus, stopwords="en", stemmer=self.stemmer)

        retriever = bm25s.BM25()
        retriever.index(corpus_token)

    def retrieve(self, query):
        query = ''
        query_tokens = bm25s.tokenize(query, stemmer=self.stemmer)
        
        retriever = bm25s.BM25()
        return retriever.retrieve(query_tokens, k=self.num_k)