from .language import (
    clean_gloss,
    map_word,
    lemmatize_words,
    llm_text_to_gloss,
)

from .generator import generate_frames, get_landmarks
from .renderer import render

# ==========================
# Lazy-loaded vocabulary
# ==========================

vocab_set = None


def get_vocab():
    global vocab_set

    if vocab_set is None:
        print("Loading text-to-sign assets...")
        vocab_set = set(get_landmarks().keys())

    return vocab_set


# ==========================
# Main Pipeline
# ==========================

def run_pipeline(user_sentence):
    print("INPUT:", user_sentence)

    # STEP 1: Text → Gloss
    raw_gloss = llm_text_to_gloss(user_sentence)
    print("RAW GLOSS:", raw_gloss)

    # STEP 2: Clean gloss
    cleaned = clean_gloss(raw_gloss)
    print("CLEANED:", cleaned)

    # STEP 3: Tokenize + Lemmatize
    tokens = cleaned.split()
    tokens = lemmatize_words(tokens)
    print("TOKENS:", tokens)

    # STEP 4: Map words to vocabulary
    vocab = get_vocab()
    mapped_sequence = [map_word(token, vocab) for token in tokens]
    print("MAPPED:", mapped_sequence)

    # STEP 5: Generate landmark frames
    frames = generate_frames(mapped_sequence)
    print("FRAMES COUNT:", len(frames))

    # STEP 6: Render video
    video_path = render(frames)
    print("VIDEO PATH:", video_path)

    return video_path