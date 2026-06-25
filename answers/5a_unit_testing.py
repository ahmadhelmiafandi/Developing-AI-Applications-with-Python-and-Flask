"""Unit tests for emotion detection."""
import unittest

from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test emotion detector outputs."""

    def test_joy(self):
        self.assertEqual(emotion_detector("I am glad this happened")["dominant_emotion"], "joy")

    def test_anger(self):
        self.assertEqual(emotion_detector("I am really angry about this")["dominant_emotion"], "anger")

    def test_disgust(self):
        self.assertEqual(emotion_detector("This is disgusting and gross")["dominant_emotion"], "disgust")

    def test_sadness(self):
        self.assertEqual(emotion_detector("I feel sad and miserable")["dominant_emotion"], "sadness")

    def test_fear(self):
        self.assertEqual(emotion_detector("I am scared and afraid")["dominant_emotion"], "fear")

    def test_blank_input(self):
        self.assertIsNone(emotion_detector("")["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
