from transformers import pipeline

def load_emotion_model():
    # Load the emotion detection model once
    try:
        classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
        return classifier
    except Exception as e:
        print(f"Error loading emotion detection model: {str(e)}")
        return None

def detect_emotion(text, classifier):
    if classifier is None:
        raise ValueError("Emotion detection model is not loaded")
    try:
        result = classifier(text)
        # The model returns a list of dictionaries; we'll take the first one
        emotion = result[0]['label']
        score = result[0]['score']
        return emotion, score
    except Exception as e:
        print(f"Error during emotion detection: {str(e)}")
        return None, None

if __name__ == "__main__":
    # Load the model once
    classifier = load_emotion_model()
    # Test the function
    test_text = "I'm really excited about this new project!"
    emotion, confidence = detect_emotion(test_text, classifier)
    if emotion and confidence:
        print(f"Detected emotion: {emotion}, Confidence: {confidence:.2f}")
    else:
        print("Failed to detect emotion")