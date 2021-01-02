# Python MP3 Player
# Originally from https://towardsdatascience.com/how-to-build-an-mp3-music-player-with-python-619e0c0dcee2
# Added
# Directory Clean up - Only retrieves files ending in mp3
# Pause Button double function - Pause button does both pause and unpause
# (WIP) Change Directory

import pygame  # used to create video games
import tkinter as tkr  # used to develop GUI
from tkinter.filedialog import askdirectory  # it permit to select dir
import os  # it permits to interact with the operating system

music_player = tkr.Tk()
music_player.title('Simple Mp3 Player')
music_player.geometry("450x350")

directory = askdirectory()
os.chdir(directory)  # it permits to change the current dir
song_list = os.listdir()  # it returns the list of files song

play_list = tkr.Listbox(music_player, font="Helvetica 12 bold", bg="yellow", selectmode=tkr.SINGLE)
for item in song_list:
    if item.endswith(".mp3"):  # grabs files ending in MP3
        pos = 0
        play_list.insert(pos, item)
        pos += 1

pygame.init()
pygame.mixer.init()

# pause button double action & Functions

pause_active_state = False


def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()


def stop():
    pygame.mixer.music.stop()


def pause():
    pygame.mixer.music.pause()
    global pause_active_state
    pause_active_state = True


def unpause():
    pygame.mixer.music.unpause()
    global pause_active_state
    pause_active_state = False


def pausebtn():
    if not pause_active_state:
        pause()
    else:
        unpause()
    # print(pause_active_state)


def changedir():  # Unfinished
    new_directory = askdirectory()
    os.chdir(directory)  # it permits to change the current dir
    new_song_list = os.listdir()  # it returns the list of files song

    new_play_list = tkr.Listbox(music_player, font="Helvetica 12 bold", bg="yellow", selectmode=tkr.SINGLE)
    for new_item in song_list:
        if new_item.endswith(".mp3"):  # grabs files ending in MP3
            new_pos = 0
            play_list.insert(new_pos, new_item)
            new_pos += 1


var = tkr.StringVar()
song_title = tkr.Label(music_player, font="Helvetica 12 bold", textvariable=var)

# GUI

Button1 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PLAY", command=play, bg="Blue", fg="Black")
Button2 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=stop, bg="Red", fg="Black")
Button3 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PAUSE", command=pausebtn, bg="Purple", fg="Black")
# Button4 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="CHANGE DIRECTORY", command=changedir, bg="Purple", fg="Black")

song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
# Button4.pack(fill="x")
play_list.pack(fill="both", expand="yes")
music_player.mainloop()
