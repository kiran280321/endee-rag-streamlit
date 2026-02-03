import numpy as np

class EndeeClient:
    def __init__(self):
        self.vectors = []
        self.payloads = []

    def add(self, vector, payload):
        self.vectors.append(np.array(vector))
        self.payloads.append(payload)

    def search(self, query_vector, top_k=3):
        query = np.array(query_vector)
        scores = []

        for i, vec in enumerate(self.vectors):
            similarity = np.dot(query, vec) / (
                np.linalg.norm(query) * np.linalg.norm(vec)
            )
            scores.append((similarity, self.payloads[i]))

        scores.sort(reverse=True, key=lambda x: x[0])
        return scores[:top_k]
