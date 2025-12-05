from sentence_transformers import SentenceTransformer
from typing import List, Union


# Initialize model once (loaded into memory only one time)
try:
    model = SentenceTransformer("all-MiniLM-L6-v2")
except Exception as e:
    raise RuntimeError(f"Failed to load embedding model: {e}")


def get_embeddings(text_list: List[str]) -> List[List[float]]:
    """
    Generates embeddings for a given list of text inputs using a pre-trained SentenceTransformer model.

    Args:
        text_list (List[str]): 
            A list of strings (sentences or words) for which embeddings will be generated.

    Returns:
        List[List[float]]: 
            A list of embedding vectors, one for each input string, in the same order as provided.

    Raises:
        ValueError: If the input is not a list or contains any non-string items.
        RuntimeError: If an error occurs during embedding generation.
    """

    # Validate input
    if not isinstance(text_list, list):
        raise ValueError("Input must be a list of strings.")

    if any(not isinstance(t, str) for t in text_list):
        raise ValueError("All items in text_list must be strings.")

    try:
        raise NotImplementedError("You need to implement this function")

    except Exception as e:
        raise RuntimeError(f"Failed to generate embeddings: {e}")
