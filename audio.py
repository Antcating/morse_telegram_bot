from pydub import AudioSegment
from morse3 import Morse as m
def audio_enc(message):
    #Sound part
    sound1 = AudioSegment.from_ogg("audio_files/E.ogg")
    sound2 = AudioSegment.from_ogg("audio_files/T.ogg")
    
    text_in_morse = m(message.text).stringToMorse()
    silence = AudioSegment.silent(duration=500)
    silence_letter = AudioSegment.silent(duration=70)
    final_sound = AudioSegment.empty()
    for i in text_in_morse:
        if i == '.':
            final_sound += sound1 
            final_sound += silence_letter
        if i == '-':
            final_sound += sound2
            final_sound += silence_letter
        if i == ' ':
            final_sound += silence
    final_sound.export("audio_files/joinedFile.ogg", format="ogg")
