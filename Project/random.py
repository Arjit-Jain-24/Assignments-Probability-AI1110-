import pygame
import numpy as np
import threading
import time
import os

def play_song(song_number, stop_event):
    number_str = str(song_number)
    print("playing song", number_str)
    song_path = os.path.join('songs', number_str + '.mp3')
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() and not stop_event.is_set():
        continue

def my_playlist():
    my_list = []
    stop_event = threading.Event()

    pygame.mixer.init()

    while len(my_list) <= 20:
        number = np.random.randint(1, 21)
        if number not in my_list:
            my_list.append(number)

            # Create a new thread to play the song
            song_thread = threading.Thread(target=play_song, args=(number, stop_event))
            song_thread.start()

            # Prompt for next song in the main thread
            user_input = input("Press 'n' for the next song, or any other key to stop: ")
            if user_input.lower() != 'n':
                stop_event.set()
                break
            else:
                stop_event.set()
                time.sleep(0.5)  # Wait for the current song to stop completely
                stop_event.clear()

    pygame.mixer.quit()

while True:
    my_playlist()
