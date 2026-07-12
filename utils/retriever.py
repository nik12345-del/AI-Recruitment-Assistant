import numpy as np

def retrieve_chunks(index, query_embedding, chunks, top_k=3):

    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:
        results.append(chunks[idx])

    return results