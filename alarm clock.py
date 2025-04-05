import time
import datetime
import pygame 

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = " " #input audio file's path location
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP!")
            pygame.mixer.init() #initializes the sound mixer.
            pygame.mixer.music.load(sound_file) #loads the sound file.
            pygame.mixer.music.play() #plays the alarm sound.

            while pygame.mixer.music.get_busy(): # keeps the program running while the sound is playing, waits until the sound finishes.
                time.sleep(1)
            is_running = False
        
        time.sleep(1)
 
if __name__ == "__main__":
    alarm_time = input("Enter the alarm time in 24 hours format (HH:MM:SS): ")
    set_alarm(alarm_time)
