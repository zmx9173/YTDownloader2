from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil


# Functions that allows user to select a path from the explorer
def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)


# Function using pytube built-in functions
def download_file():
    #get user link and path
    get_link = link_field.get()
    user_path = path_label.cget("text")
    screen.title('Downloading...')

    #download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()

    #move file to selected directory
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete!')


# Initializing tkinter screen and canvas
screen = Tk()
title = screen.title('Youtube Downloader')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

# Creating logo image
logo_img = PhotoImage(file='yt.png')
logo_img = logo_img.subsample(2, 2)
canvas.create_image(250, 80, image=logo_img)

# Creating field labels and buttons on canvas
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter Download Link: ", font=('Arial', 15))
path_label = Label(screen, text="Select Path For Download", font=('Arial', 15))
path_btn = Button(screen, text="Select Path", command=select_path)
download_btn = Button(screen, text="Download File", command=download_file)

# Make them into small widget windows to canvas
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=path_btn)
canvas.create_window(250, 390, window=download_btn)

screen.mainloop()
