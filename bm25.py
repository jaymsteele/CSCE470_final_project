import math
from collections import Counter, defaultdict

class BM25:
    def __init__(self, corpus):
        self.corpus = corpus
        self.doc_count = len(corpus)
        self.avg_doc_length = sum(len(doc) for doc in corpus) / self.doc_count
        self.doc_frequencies = defaultdict(int)
        self.doc_lengths = [len(doc) for doc in corpus]
        self.idf = {}
        
        # Calculate document frequencies
        for doc in corpus:
            unique_terms = set(doc)
            for term in unique_terms:
                self.doc_frequencies[term] += 1
        
        # Calculate IDF for each term
        for term, freq in self.doc_frequencies.items():
            self.idf[term] = math.log((self.doc_count - freq + 0.5) / (freq + 0.5) + 1)
    
    def get_scores(self, query, k1=1.5, b=0.75):
        scores = []
        
        for i, doc in enumerate(self.corpus):
            doc_score = 0
            term_freqs = Counter(doc)
            
            for term in query:
                if term in term_freqs:
                    idf = self.idf.get(term, 0)
                    term_freq = term_freqs[term]
                    doc_length = self.doc_lengths[i]
                    
                    numerator = term_freq * (k1 + 1)
                    denominator = term_freq + k1 * (1 - b + b * (doc_length / self.avg_doc_length))
                    doc_score += idf * (numerator / denominator)
            
            scores.append(doc_score)
        
        return scores
