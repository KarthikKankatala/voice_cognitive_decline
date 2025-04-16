import os
import librosa
import soundfile as sf
import speech_recognition as sr
from config import Config

class AudioProcessor:
    def __init__(self):
        self.sample_rate = Config.SAMPLE_RATE
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 400
        
    def load_audio(self, filepath):
        """Load audio file with error handling"""
        try:
            y, sr = librosa.load(filepath, sr=self.sample_rate)
            return y, sr
        except Exception as e:
            print(f"Error loading {os.path.basename(filepath)}: {str(e)}")
            return None, None
            
    def transcribe(self, audio_path):
        """Robust transcription with fallback"""
        try:
            with sr.AudioFile(audio_path) as source:
                audio = self.recognizer.record(source)
                try:
                    # Try Google first (requires internet)
                    return self.recognizer.recognize_google(audio)
                except sr.UnknownValueError:
                    print(f"Could not understand audio in {os.path.basename(audio_path)}")
                    return ""
                except sr.RequestError:
                    # Fallback to offline recognition
                    try:
                        return self.recognizer.recognize_sphinx(audio)
                    except:
                        print(f"Offline recognition failed for {os.path.basename(audio_path)}")
                        return ""
        except Exception as e:
            print(f"File error in {os.path.basename(audio_path)}: {str(e)}")
            return ""
