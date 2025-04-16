# 🧠 Voice-Based Cognitive Decline Detection

## Overview
This project provides a proof-of-concept AI/ML web application that assesses cognitive decline based on voice data. Users can interact with the app by either recording their voice in real time using the microphone or uploading a `.wav` audio file. The app processes the voice input, extracts features related to speech patterns, and generates a cognitive risk score based on those features.

[**Deployed App**](https://voicecognitivedecline-a5s9c98nnivegrvgnrl9sz.streamlit.app/)

---

## 🚀 Features

- 🎙️ Real-time Speech Input: Allows users to record their voice via a microphone.
- 📁 Audio File Upload: Users can upload a `.wav` audio file for analysis.
- 🔬 Speech & Language Feature Extraction: The app analyzes key speech features like speech rate, hesitation markers, pitch variability, and more.
- 📊 Risk Score Prediction: The app calculates a risk score (from 0 to 1) to assess potential cognitive decline or stress.
- 📉 Feature Visualization: Users can view a bar chart displaying the distribution of extracted audio features.
- ✅ User-Friendly UI: Built using Streamlit, providing an interactive and intuitive interface.

---

## 📈 What You Will See on the UI

When you interact with the app, here’s what you will experience:

- **App Title & Description**: At the top of the page, you’ll see the title "🧠 Voice-Based Cognitive Decline Detection" along with a short description explaining how the app works and what you are expected to do.
- **Text on UI**:
  - "Speak the sentence below or upload an audio file to assess cognitive risk."
  - "🗣️ Please say: Today is a good day to check my memory and attention (5-10 seconds)"
- **Upload Audio File Option**: Users can upload `.wav` files. Once a file is uploaded, the app will process the audio and display the results.
  - UI Message: "✅ Audio uploaded!"
- **Microphone Recording Option**: Use the microphone and click "🔍 Analyze Microphone Input".
  - UI Message: "✅ Microphone audio recorded!"

**Prediction Results**:
- **Risk Score**: A number between `0.0` (low risk) and `1.0` (high risk).
- **Features**: A JSON breakdown of the extracted features such as:
```json
{
    "speech_rate": 1.25,
    "filler_count": 2,
    "pause_ratio": 0.12,
    "pitch_variability": 0.25
}
```
- **Feature Trend Chart**: A bar chart shows feature values (e.g., speech rate, pause ratio).

---

## 🧩 What Could Go Wrong?

### Zero or Invalid Feature Values
- **Speech Rate**: If transcription is empty/short, value may be 0.
- **Filler Count**: 0 if no hesitation markers or transcription misses them.
- **Pause Ratio**: Very low if there is no silence.

**Fix**: Speak clearly, include pauses or hesitations naturally.

### Transcription Errors
- Errors affect features like speech_rate and filler_count.

**Fix**: Ensure microphone clarity and minimal background noise.

---

## ⚙️ Steps to Run the Application

### 1. Clone the Repository
```bash
git clone https://github.com/KarthikKankatala/voice_cognitive_decline.git
cd voice_cognitive_decline
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # For Windows
source venv/bin/activate  # For macOS/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install `ffmpeg`
- Download from https://ffmpeg.org/
- Ensure it's added to your system's PATH.

### 5. Generate synthetic audio samples (optional, if you need more test data)

```bash
python generate_samples.py

```

<<<<<<< HEAD
5. Train the ML model (if not already trained):

=======
### 6. Train the ML Model (If Not Already Trained)
>>>>>>> 6470e98 (Added some files)
```bash
python train_model.py
```

<<<<<<< HEAD
6. Run the web app:

=======
### 7. Run the Web App
>>>>>>> 6470e98 (Added some files)
```bash
streamlit run app.py
```

### 8. Access the App
Open your browser and go to http://localhost:8501

---

## 🧠 Cognitive Features Extracted

- **Speech Rate**: Words spoken per second.
- **Filler Count**: Count of hesitation words like "uh", "um".
- **Pause Ratio**: Time spent silent versus speaking.
- **Pitch Variability**: Variation in pitch throughout the speech.

These are used to calculate a cognitive risk score.

---

## 📈 Expected Output Example

- **Risk Score**: Value between `0.0` and `1.0`
- **Feature Breakdown**: JSON display
- **Feature Trend Chart**: Bar graph with extracted features

---

## ⚠️ Disclaimer

This is a prototype and should not be used for clinical decision-making. It is intended for educational and research purposes only.

---


## 💡 Future Enhancements

- Improved NLP Features: BERT, Wav2Vec for better transcription and feature extraction.
- Larger Datasets: Improve training and generalization.
- API Integration: Expose via REST API for integration.