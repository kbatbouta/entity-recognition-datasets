import numpy as np


def create_model(entity_types, embedding_model, name="default"):
    clusters = {}
    for cat in entity_types:
        vectors = embedding_model.encode(sentences=[f"{cat['name']}: {cat['description']}"] + [
            f"{s['name']}: {s['description']}" for s in cat["subcategories"]
        ])
        vectors = [list(v.astype(np.float64)) for v in vectors]
        clusters[cat['name']] = dict(zip([s['name'] for s in cat["subcategories"]], vectors))
    return {
        "name": name,
        "clusters": clusters,
    }
