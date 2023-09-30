import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pytube import YouTube


def download_video():
    video_url = url_entry.get()
    try:
        yt = YouTube(video_url)
        title_label.config(text="Title: " + yt.title)
        views_label.config(text="Views: " + str(yt.views))

        yd = yt.streams.get_highest_resolution()
        cleaned_title = ''.join(c if c.isalnum() or c in [' ', '-', '_'] else '' for c in yt.title)
        download_filename = cleaned_title + '.mp4'
        download_path = os.path.join(destination_folder, download_filename)
        yd.download(output_path=download_path)

        messagebox.showinfo("Download Complete", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", "An error occurred:\n" + str(e))


destination_folder = r'C:\Users\asus\Downloads\YouTube'
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

root = tk.Tk()
root.title("YouTube Video Downloader")

youtube_red = "#FF0000"  # Replace with the actual color code
youtube_black = "#282828"  # Replace with the actual color code

style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', padding=10, font=('Helvetica', 12), background=youtube_red, foreground="white")
style.configure('TLabel', font=('Helvetica', 14), background=youtube_black, foreground="white")
style.configure('TEntry', font=('Helvetica', 12), padding=10)

url_label = ttk.Label(root, text="Enter YouTube URL:")
url_label.pack(pady=10)

url_entry = ttk.Entry(root, width=50)
url_entry.pack(pady=5)

download_button = ttk.Button(root, text="Download Video", command=download_video)
download_button.pack(pady=10)

title_label = ttk.Label(root, text="Title:")
title_label.pack()

views_label = ttk.Label(root, text="Views:")
views_label.pack()

root.mainloop()

