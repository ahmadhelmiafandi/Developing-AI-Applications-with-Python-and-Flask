"""Unit tests for emotion detection."""
import unittest
from unittest.mock import patch

from EmotionDetection import emotion_detector


class MockResponse:
    """Mock Watson NLP response."""

    def __init__(self, emotion, status_code=200):
        self.emotion = emotion
        self.status_code = status_code

    def json(self):
        return {"emotionPredictions": [{"emotion": self.emotion}]}


class TestEmotionDetection(unittest.TestCase):
    """Test emotion detector outputs."""

    def assert_dominant_emotion(self, emotion):
        scores = {
            "anger": 0.1,
            "disgust": 0.1,
            "fear": 0.1,
            "joy": 0.1,
            "sadness": 0.1,
        }
        scores[emotion] = 0.8
        with patch("EmotionDetection.emotion_detection.requests.post", return_value=MockResponse(scores)):
            self.assertEqual(emotion_detector("test")["dominant_emotion"], emotion)

    def test_joy(self):
        self.assert_dominant_emotion("joy")

    def test_anger(self):
        self.assert_dominant_emotion("anger")

    def test_disgust(self):
        self.assert_dominant_emotion("disgust")

    def test_sadness(self):
        self.assert_dominant_emotion("sadness")

    def test_fear(self):
        self.assert_dominant_emotion("fear")

    @patch("EmotionDetection.emotion_detection.requests.post", return_value=MockResponse({}, 400))
    def test_blank_input(self, _mock_post):
        self.assertIsNone(emotion_detector("")["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
