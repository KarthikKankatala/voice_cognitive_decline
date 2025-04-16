import numpy as np
import librosa
from config import Config

class FeatureExtractor:
    @staticmethod
    def extract_features(y, sr, text=""):
        """Extract features with text-optional mode"""
        features = {}
        
        # Silence analysis
        non_silent = librosa.effects.split(y, top_db=25)
        speech_duration = sum(end-start for start,end in non_silent)/sr
        features['pause_ratio'] = 1 - (speech_duration / (len(y)/sr))
        
        # Speech metrics (works without text)
        features['speech_rate'] = len(text.split())/(len(y)/sr) if text else 0
        features['filler_count'] = sum(text.lower().count(f) 
                                    for f in Config.HESITATION_MARKERS) if text else 0
        
        # Vocal characteristics
        pitches = librosa.yin(y, fmin=75, fmax=300, sr=sr)
        valid_pitches = pitches[pitches > 0]
        features['pitch_variability'] = np.std(valid_pitches) if len(valid_pitches) > 0 else 0
        
        return features
