# -*- coding: iso-8859-1 -*-

"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.types.VoiceSelectionParams(
    language_code='de-DE',
    name='de-DE-Wavenet-D',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)

# Select the type of audio file you want returned
audio_config = texttospeech.types.AudioConfig(
    pitch=9.2,
    speaking_rate=1.23,
    audio_encoding=texttospeech.enums.AudioEncoding.LINEAR16)

with open("outputjason.txt") as f:
    for line in f:
        # Set the text input to be synthesized
        transcribe = line
        synthesis_input = texttospeech.types.SynthesisInput(text=transcribe)  
        filename = line.replace(" ","") 
        filename = filename.replace(".","") 
        filename = filename.replace(",","") 
        filename = filename.replace("?","") 
        filename = filename.replace("\n","") 
        filename = filename.replace("!","") + ".wav"
        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        response = client.synthesize_speech(synthesis_input, voice, audio_config)   
        # The response's audio_content is binary.
        with open(filename, 'wb') as out:
             # Write the response to the output file.
            out.write(response.audio_content)
            print('Audio content written to file',filename)
