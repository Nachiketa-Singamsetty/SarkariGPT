# fake_detector.py

from transformers.pipelines import pipeline
import torch

# Load fake news detection pipeline with GPU if available
classifier = pipeline(
    "text-classification",
    model="mrm8488/bert-tiny-finetuned-fake-news-detection",
    device=0 if torch.cuda.is_available() else -1
)

LABEL_MAP = {
    'label_0': 'FAKE',
    'label_1': 'REAL',
    'LABEL_0': 'FAKE',
    'LABEL_1': 'REAL',
    'FAKE': 'FAKE',
    'REAL': 'REAL'
}

def detect_fake_news(text):
    result = classifier(text)[0]
    print("[DEBUG] Classifier output:", result)
    label_raw = result['label']
    label = LABEL_MAP.get(label_raw, label_raw)
    confidence = float(result['score'])
    return {
        'label': label,
        'confidence': confidence
    } 