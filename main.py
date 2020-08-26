
from os import listdir
from os.path import isfile, join
from playsound import playsound

import glob

sound_path = ('music_path', 'other_music_path')

def get_sound_list():
    
    sound_files = [i for k in range(len(sound_path)) for i in glob.glob(sound_path[k])]

    print(sound_files)

    return sound_files
    
    
def print_sounds(sound_files):
    
    for i in range(len(sound_files)):
        
        print(f"{i} {sound_files[i].split('/')[-1]}")
        

def play_sound(sound_files):
    
    file_choosed = int(input())
    
    playsound(sound_files[file_choosed])
    

def main():
    
    sound_files = get_sound_list()
    print_sounds(sound_files)
    play_sound(sound_files)
    
main()
