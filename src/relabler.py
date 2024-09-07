import numpy as np


def create_model(entity_types, embedding_model, llm_call_function, name="default"):
    clusters = {}
    generated_examples = []
    for cat in entity_types:
        examples = [
            (s['name'], llm_call_function(f"Provide random very very short example text about the following topic '{s['name']}'"))
            for s in cat["subcategories"]
        ]
        generated_examples.append(examples)
        vectors = embedding_model.encode(sentences=[f"{cat['name']}: {cat['description']}"] + [
            f"{s['name']}: {s['description']}" for s in cat["subcategories"]
        ] + [e[1] for e in examples])
        clusters[cat['name']] = np.mean(vectors, axis=0)
    return {
        "name": name,
        "clusters": list(clusters),
        "generated_examples": generated_examples
    }
