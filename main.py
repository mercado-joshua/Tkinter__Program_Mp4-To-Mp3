#===========================
# Imports
#===========================

import tkinter as tk
from tkinter import Label, ttk, colorchooser, Menu, Spinbox, scrolledtext, messagebox as mb, filedialog as fd

import os
from glob import glob

#===========================
# Main App
#===========================

class App(tk.Tk):
    """Main Application."""
    #===========================================
    def __init__(self):
        super().__init__()
        self.style = ttk.Style(self)
        self.init_UI()
        self.init_events()

    #===========================================
    def init_events(self):
        self.listbox.bind('<Double-Button>', self.evt__add_to_entry)

    def init_UI(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        label = ttk.Label(self.main_frame, text='Select video to convert:')
        label.pack(side=tk.TOP, anchor=tk.W)

        self.listbox = tk.Listbox(self.main_frame)
        self.listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for file in list(glob('*.mp4')):
	        self.listbox.insert(tk.END, file)

        self.filename = tk.StringVar()
        self.entry = ttk.Entry(self.main_frame, textvariable=self.filename, state=tk.DISABLED)
        self.entry.pack(side=tk.TOP, anchor=tk.W, fill=tk.X, expand=True)

        button = ttk.Button(self.main_frame, text='Convert to .mp3', command=self.m__get_audio)
        button.pack(side=tk.RIGHT, anchor=tk.E, padx=5, pady=5)

    # EVENTS -----------------------------------
    def evt__add_to_entry(self, event):
        n = self.listbox.curselection()
        item = self.listbox.get(n)
        self.filename.set(item)

    # INSTANCE METHODS -------------------------
    def m__get_audio(self):
        string = f'ffmpeg -i {self.filename.get()} -f mp3 -ab 192000 -vn audio.mp3'
        os.system(string)
        os.startfile('audio.mp3')


#===========================
# Start GUI
#===========================

def main():
    app = App()
    app.resizable(False, False)
    app.style.theme_use('clam')
    app.title('Mp4 to Mp3 Converter Version 1.0')
    app.iconbitmap('python.ico')
    app.mainloop()

if __name__ == '__main__':
    main()