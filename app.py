import streamlit as st
import numpy as np
import os
import tempfile
import soundfile as sf
from utils.audio_processor import AudioProcessor
from utils.feature_extractor import FeatureExtractor
from utils.model import RiskDetector
from config import Config
import matplotlib.pyplot as plt
from streamlit_webrtc import webrtc_streamer, AudioProcessorBase

st.set_page_config(page_title="Cognitive Decline Detector", layout="centered")
st.title("🧠 Voice-Based Cognitive Decline Detection")
st.markdown("Speak the sentence below or upload an audio file to assess cognitive risk.")
st.info("🗣️ **Please say:** *Today is a good day to check my memory and attention* (5-10 seconds)")

# Load model and utilities
detector = RiskDetector()
detector.load()
processor = AudioProcessor()
extractor = FeatureExtractor()

# Upload option
uploaded_file = st.file_uploader("📁 Upload Audio File (WAV)", type=["wav"])

# Microphone recording option
st.markdown("Or use your 🎙️ microphone:")
class AudioRecorder(AudioProcessorBase):
    def __init__(self):
        self.frames = []

    def recv(self, frame):
        self.frames.append(frame.to_ndarray().flatten())
        return frame

    def get_audio(self):
        return np.concatenate(self.frames) if self.frames else None

recorder = AudioRecorder()
ctx = webrtc_streamer(key="mic", audio_processor_factory=lambda: recorder, media_stream_constraints={"audio": True, "video": False})

# Risk analysis logic
def run_analysis(audio_path, label="Recording"):
    y, sr = processor.load_audio(audio_path)
    if y is None:
        st.error("❌ Could not load audio.")
        return

    text = processor.transcribe(audio_path)
    features = extractor.extract_features(y, sr, text)
    risk_score = detector.predict(list(features.values()))

    st.subheader("🧪 Prediction Results")
    st.metric("Risk Score", f"{risk_score:.3f}", delta=None)
    st.json(features)

    st.subheader("📉 Feature Trend Chart")
    fig, ax = plt.subplots()
    ax.bar(features.keys(), features.values(), color="skyblue")
    ax.set_ylabel("Value")
    ax.set_title("Audio Feature Distribution")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Uploaded file analysis
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(uploaded_file.read())
        st.success("✅ Audio uploaded!")
        run_analysis(tmp.name)

# Recorded mic audio analysis
elif st.button("🔍 Analyze Microphone Input") and recorder.get_audio() is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        sf.write(tmp.name, recorder.get_audio(), samplerate=Config.SAMPLE_RATE)
        st.success("✅ Microphone audio recorded!")
        run_analysis(tmp.name)
