import pyttsx3
import time


if __name__ == "__main__":
    
    engine = pyttsx3.init()
    
    engine.setProperty('rate', 170) #default 200
    engine.setProperty('volume', 0.8)

    songs = [("Nights", "Frank Ocean"), 
             ("Hey Jane", "Tyler, the Creator"), 
             ("Like A Prayer", "Madonna"),
             ("Smells Like Teen Spirit", "Nirvana"),
             ("Hey, You've Got to Hide Your Love Away", "The Beatles")]

    for song in songs:
        print(f'Now playing {song[0]} by {song[1]}')
        engine.say(f'Now playing {song[0]} by {song[1]}')
        engine.runAndWait()
        time.sleep(1)
