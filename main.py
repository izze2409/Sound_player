
from os import listdir
from os.path import isfile, join
from playsound import playsound

sound_path = 'folder_directory'

def get_sound_list():
    
    sound_files = [f for f in listdir(sound_path) if isfile(join(sound_path, f))]
    
    return sound_files
    
    
def print_sounds(sound_files):
    
    for i in range(len(sound_files)):
        
        print(f"{i} {sound_files[i]}")
        

def play_sound(sound_files):
    
    file_choosed = int(input())
    
    playsound(f"{sound_path}/{sound_files[file_choosed]}")

def main():
    
    sound_files = get_sound_list()
    print_sounds(sound_files)
    play_sound(sound_files)
    
main()
