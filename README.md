
# 🧠 Voice-Based Cognitive Decline Detection

A proof-of-concept AI/ML web app that detects signs of cognitive stress or decline from voice data. Users can speak live via a microphone or upload `.wav` files. The app extracts speech and language features and generates a cognitive **risk score**.

---

## 🚀 Features

- 🎙️ Real-time speech input via microphone  
- 📁 Upload `.wav` audio files  
- 🔬 Audio + text feature extraction (pauses, hesitations, speech rate, etc.)  
- 📈 Risk score prediction using unsupervised ML  
- 📊 Feature trend visualization  
- ✅ Clean UI built with Streamlit  

---

## 🧩 Tech Stack

- Python, Streamlit  
- NumPy, Scikit-learn, librosa, gTTS  
- streamlit-webrtc, SpeechRecognition  
- Matplotlib  

---

## 📁 Project Structure

voice_cognitive_decline/  
├── app.py                  → Streamlit web app  
├── train_model.py          → Trains & saves model as detector.pkl  
├── generate_samples.py     → Generates synthetic test samples in the data folder  
├── models/  
│   └── detector.pkl        → Saved ML model (auto-generated)  
├── results/                → Output results  
├── utils/  
│   ├── audio_processor.py   → Handles audio loading + transcription  
│   ├── feature_extractor.py → Extracts cognitive features  
│   └── model.py             → Loads and applies ML model  
├── config.py              → Config constants (e.g., sample rate)  
├── requirements.txt       → Python dependencies  
└── README.md              → This file  

---

## ⚙️ Setup Instructions

1. Clone the repo and set up a virtual environment:

```bash
git clone https://github.com/KarthikKankatala/voice_cognitive_decline.git
cd voice_cognitive_decline
python -m venv venv
venv\Scripts\activate  # For Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Install and configure `ffmpeg`:

Download from https://ffmpeg.org/download.html  
Make sure it’s added to your system PATH.

4. Generate synthetic audio samples (optional, if you need more test data)

```bash
python generate_samples.py

```

4. Train the ML model (if not already trained):

```bash
python train_model.py
```

5. Run the web app:

```bash
streamlit run app.py
```

---

## 🧠 Cognitive Features Extracted

- Speech rate (words per second)  
- Number of pauses  
- Hesitation count (“uh”, “um”)  
- Pitch variability  
- Sentence completeness  
- Word-recall cues  

---

## 📈 Output Example

- **Risk Score** between `0.0` (low risk) and `1.0` (high risk)  
- Feature breakdown in JSON  
- Feature trend chart (bar graph)  

---

## ✅ Example Use

**Speak a sentence like:**  
“Yesterday I went to the grocery store to buy... uh... I forgot... oh yes, bananas.”  
Then click **🔍 Analyze Microphone Input** and view the results.

---

## ⚠️ Disclaimer

This is a demo/prototype and **not a clinical tool**. Do not use for health-related decisions.  
For research/educational purposes only.

---

## 💡 Future Enhancements

- More robust speech NLP features (BERT, Wav2Vec)  
- Larger dataset for training  
- API endpoint deployment  
- Clinical testing integration
