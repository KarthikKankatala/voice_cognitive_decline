from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib
from config import Config

class RiskDetector:
    def __init__(self):
        self.scaler = StandardScaler()
        self.model = IsolationForest(
            n_estimators=100,
            contamination=0.15,
            random_state=42
        )
        
    def train(self, features):
        X = self.scaler.fit_transform(features)
        self.model.fit(X)
        joblib.dump((self.scaler, self.model), Config.MODEL_PATH)
        
    def predict(self, features):
        scaled = self.scaler.transform([features])
        return self.model.decision_function(scaled)[0]

    def load(self):
        """Load the pre-trained model"""
        self.scaler, self.model = joblib.load(Config.MODEL_PATH)
