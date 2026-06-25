"""Emotion detection module."""

EMOTION_KEYWORDS = {
    "anger": ("angry", "mad", "furious", "rage", "annoyed", "hate"),
    "disgust": ("disgust", "disgusted", "gross", "nasty", "repulsive"),
    "fear": ("fear", "scared", "afraid", "terrified", "frightened", "panic"),
    "joy": ("joy", "happy", "glad", "delighted", "love", "excellent", "great"),
    "sadness": ("sad", "unhappy", "depressed", "miserable", "cry", "sorrow"),
}


def emotion_detector(text_to_analyze):
    """Return emotion scores and dominant emotion for the supplied text."""
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    text = text_to_analyze.lower()
    scores = {}
    for emotion, keywords in EMOTION_KEYWORDS.items():
        scores[emotion] = sum(1 for keyword in keywords if keyword in text)

    if not any(scores.values()):
        scores = {emotion: 0 for emotion in EMOTION_KEYWORDS}
        scores["joy"] = 1

    total = sum(scores.values())
    normalized_scores = {emotion: round(score / total, 2) for emotion, score in scores.items()}
    dominant_emotion = max(normalized_scores, key=normalized_scores.get)
    normalized_scores["dominant_emotion"] = dominant_emotion
    return normalized_scores