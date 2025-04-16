import os
import random
import numpy as np
import soundfile as sf
from gtts import gTTS  # Google Text-to-Speech for generating synthetic speech
from config import Config

# Function to generate a synthetic speech sample
def generate_speech(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)

# Function to create a folder for the samples if it doesn't exist
def create_sample_folder(folder_name="data"):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# List of sentences to generate cognitive decline-related speech samples
sentences = [
    "Today is a good day to check my memory and attention.",
    "I need to remember where I placed my keys.",
    "How many months are in a year?",
    "I was trying to recall a word earlier, but I forgot it.",
    "The cat is on the table, I think it was the dog."
]

# Function to generate synthetic samples for "healthy" and "impaired" categories
def generate_samples():
    create_sample_folder()

    # Generate 5 healthy samples
    for i in range(1, 6):
        sentence = random.choice(sentences)
        filename = f"data/healthy_{i}.wav"
        generate_speech(sentence, filename)
        print(f"Generated: {filename}")

    # Generate 5 impaired samples (with slight speech issues like pauses)
    for i in range(1, 6):
        sentence = random.choice(sentences) + " um, um... uh, I think."
        filename = f"data/impaired_{i}.wav"
        generate_speech(sentence, filename)
        print(f"Generated: {filename}")

    print("Sample generation complete!")

if __name__ == "__main__":
    generate_samples()
