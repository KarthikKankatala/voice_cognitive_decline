import os
import numpy as np
from sklearn.utils import shuffle
from utils.feature_extractor import FeatureExtractor
from utils.audio_processor import AudioProcessor
from utils.model import RiskDetector
from config import Config

SYNTHETIC_PATH = "synthetic_data"
os.makedirs(SYNTHETIC_PATH, exist_ok=True)

def generate_synthetic_features():
    healthy = []
    impaired = []
    for _ in range(30):
        healthy.append({
            "pause_ratio": np.random.uniform(0.05, 0.15),
            "speech_rate": np.random.uniform(2.5, 4.0),
            "filler_count": np.random.randint(0, 2),
            "pitch_variability": np.random.uniform(10, 30)
        })
        impaired.append({
            "pause_ratio": np.random.uniform(0.3, 0.6),
            "speech_rate": np.random.uniform(0.8, 1.8),
            "filler_count": np.random.randint(4, 10),
            "pitch_variability": np.random.uniform(0, 8)
        })
    return healthy + impaired

def train_model():
    data = generate_synthetic_features()
    feature_list = [list(d.values()) for d in data]
    detector = RiskDetector()
    detector.train(feature_list)
    print(f"✅ Model trained and saved to {Config.MODEL_PATH}")

if __name__ == "__main__":
    train_model()
