#Updated on 11-15

from tkinter import *
import customtkinter
import tkinter as tk

from PIL import Image, ImageTk
import time
import os
import shutil
from tkinter import filedialog

import tempoDetect
import genreDetect
import subprocess
import whisper

#Import Mood module from another folder:
import sys
PROGRAM_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))
new_path = os.path.join(PROGRAM_DIR, "Text2Emotion")
sys.path.insert(1, new_path)
import Text2Emotion


#Set the overall theme of our app
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
song_name = "x" #global variable that will store name of the song we are analyzing

# Create the windows template class
class windows(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        customtkinter.CTk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Audio Visualization Analyzer (AVA)")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # creating a frame and assigning it to container
        container = customtkinter.CTkFrame(self, height=1100, width=720)
        # specifying the region where the frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # we'll create the frames themselves later but let's add the components to the dictionary.
        for F in (HomePage, OptionsPage, AnalysisPage, PerformancePage):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
            
        # Using a method to switch frames
        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        #raises the current frame to the top
        frame.tkraise()

    def on_closing(self, event=0):
        self.destroy()

#Define the Home Page
class HomePage(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)

        #self.label = customtkinter.CTkLabel(master=self, text= "Home Page")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #Objects within the Homepage 

        #============================================================#
        #Create text bubble Ava's introduction as an image object
        self.intro = Image.open("pixel-speech-bubble.png")
        self.resize_intro = self.intro.resize((600,200))
        self.img2 = ImageTk.PhotoImage(self.resize_intro)

        # Create a Label Widget to display the text or Image object
        self.label = customtkinter.CTkLabel(self, image = self.img2)
        self.label.grid(row=0,column=0, columnspan=4, padx=200) #text bubble placement
        #============================================================#

        #Walle
        self.file="walle5.0.gif"
        self.info = Image.open( self.file) #Read in GIF

        self.frames = self.info.n_frames  # gives total number of frames that gif contains

        # creating list of PhotoImage objects for each frames
        self.im = [PhotoImage(file=self.file,format=f"gif -index {i}") for i in range(self.frames)]

        self.count = 0
        self.anim = None

        #Create a loop that will iterate through the frames of the animation
        def animation(count):
            global anim
            self.im2 = self.im[self.count]

            self.gif_label.configure(image=self.im2)
            self.count += 1
            if self.count == self.frames:
                self.count = 0
            anim = self.after(50,lambda :animation(self.count))


        self.gif_label = customtkinter.CTkLabel(self, image="")
        self.gif_label.grid(row=1,column=0, columnspan = 2, padx=100) #walle placement
        #Run the animation 
        animation(self.count)
        #============================================================#
        #Open File method
        def open_file():
            global song_name
            self.song = filedialog.askopenfilename(filetypes=(("mp3 Files", "*.mp3"), ))
            shutil.copy(self.song, os.getcwd())
            song_name = str(os.path.basename(self.song))
            self.text = customtkinter.CTkLabel(self, text=song_name + " ...Successfully uploaded")
            self.text.grid(row=2,column=1,columnspan = 1, sticky = "W")

        #Initialize and place the "Open file" button
        self.open_file_button = customtkinter.CTkButton(self,text="Open File", command=open_file)
        self.open_file_button.grid(row=2,column=0, columnspan = 1, sticky = "W", pady =2 )
        
        #============================================================#
        #"Remove" button function
        def remove_song():
            self.path = os.getcwd()
            for file in os.listdir(self.path):
                if file.endswith(".mp3"):
                    song_name = file
                    os.remove(file)

            self.text = customtkinter.CTkLabel(self, text=song_name+" ... Successfully removed")
            self.text.grid(row=4,column=1,columnspan = 1, sticky = "W")

        #Initialize and place the "Remove" button
        self.remove_button = customtkinter.CTkButton(self,text="Remove Song", command=remove_song)
        self.remove_button.grid(row=4,column=0, columnspan = 1, sticky = "W", pady =2 )
        #============================================================#

        #We use the switch_window_button in order to call the show_frame()
        switch_window_button = customtkinter.CTkButton(
            self,
            text = "Options Page",
            command = lambda: controller.show_frame(OptionsPage),)
        #switch_window_button.pack(side = "bottom", fill = tk.X)
        switch_window_button.grid(row=6,column=0, columnspan=4, sticky = "W", pady =2)

#Define the Options Page
class OptionsPage(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        label = customtkinter.CTkLabel(self, text="Options Page")
        label.grid(row=0,column=0, columnspan=4, sticky = "NSEW", pady =2)

        #============================================================#
        #Create text bubble Ava's introduction as an image object
        self.intro = Image.open("options-speech-bubble.png")
        self.resize_intro = self.intro.resize((600,200))
        self.img2 = ImageTk.PhotoImage(self.resize_intro)

        # Create a Label Widget to display the text or Image object
        self.label = customtkinter.CTkLabel(self, image = self.img2)
        self.label.grid(row=1,column=0, columnspan=4, padx=200) #text bubble placement
        #============================================================#

        #Walle
        self.file="walle5.0.gif"
        self.info = Image.open( self.file) #Read in GIF

        self.frames = self.info.n_frames  # gives total number of frames that gif contains

        # creating list of PhotoImage objects for each frames
        self.im = [PhotoImage(file=self.file,format=f"gif -index {i}") for i in range(self.frames)]

        self.count = 0
        self.anim = None

        #Create a loop that will iterate through the frames of the animation
        def animation(count):
            global anim
            self.im2 = self.im[self.count]

            self.gif_label.configure(image=self.im2)
            self.count += 1
            if self.count == self.frames:
                self.count = 0
            anim = self.after(50,lambda :animation(self.count))


        self.gif_label = customtkinter.CTkLabel(self, image="")
        self.gif_label.grid(row=2,column=0, columnspan = 2, padx=100) #walle placement
        #Run the animation 
        animation(self.count)

        #=============================================================
        #Button that takes us to Performance Mode
        performance_button = customtkinter.CTkButton(
            self,
            text="Performance Mode",
            command=lambda: controller.show_frame(PerformancePage),
        )
        performance_button.grid(row=5,column=2, columnspan=4, sticky = "W", pady =2)

        #=============================================================
        #Button that takes us to Analysis Mode
        analysis_button = customtkinter.CTkButton(
            self,
            text="Analysis Mode",
            command=lambda: controller.show_frame(AnalysisPage),
        )
        analysis_button.grid(row=5,column=1, columnspan=4, sticky = "W", pady =2)


#Define the Analysis Page
class AnalysisPage(customtkinter.CTkFrame):

    def get_results(self):
        #Function that calls genreDetect,tempoDetect,Text2Emotion to retrieve the results and displays them on the UI
        #========================================================================================================        
        #create an empty array that stores the fetched results
        self.bpm_arr = []
        self.genre_arr = []
        self.mood_arr = []
        
        #Fetch MP3 File name using global variable song_name
        file = song_name

        #Fetch BPM
        #========================================================================================================
        bpm_song = tempoDetect.detect_tempo(file)
        bpm_result ="{:.2f}".format(bpm_song[0])
        
        #store fetched BPM in the results array
        self.bpm_arr.append(bpm_result) #BPM   results[0]   Will always be 1 element
        

        #Fetch Genre 
        #========================================================================================================
        genre_result = genreDetect.execute(file,30) # Splits example1.mp3 into 30 second seqments
        
        #Genre has multiple elements
        for element in genre_result:
            self.genre_arr.append(element)            #add fetched results onto results array
            
        print("1:" + str(self.genre_arr))
            
        genre_string ='\n'.join(map(str, self.genre_arr)) #formats the array
        #print("2:" +genre_string)
        #genre_string = genre_string.split('\n')   #stores the results array in a formated string
        #print("3:" +str(genre_string))
        
        #Split Vocals/Instruments from file
        temp_tuple = os.path.splitext(file) #create a tuple [song_name, .mp3]
        
        songname = file
        command = "spleeter separate -d 900 -o audio_output " + songname
        subprocess.Popen(command,shell=True)
        time.sleep(70)   
        print("Spleeter finished execution")
        
        #Transcribe vocal file into a text file
        temp = str(temp_tuple[0])
        filein = "audio_output/" + temp + "/vocals.wav"
        fileout = "audio_output/"+ temp + "/lyrics.txt"
        model = whisper.load_model("small")
        result = model.transcribe(filein, fp16=False, language = 'English')    # takes ~5mins
        #print(result["text"])
        vocal_output = open(fileout, "w")
        vocal_output.write(result["text"].strip())
        vocal_output.close()
        
        #Fetch Mood
        #========================================================================================================  
        lyrics_path = "audio_output/"+temp+"/lyrics.txt"        
        
        mood_result = Text2Emotion.checkLyrics(lyrics_path)
        self.mood_arr.append(mood_result)      #Mood  results[1] May be multiple elements
        
        
        #Fetch Lyrics (Current naming convention for lyrics file is <mp3_file_name.txt>)
        #========================================================================================================       
        
        with open(lyrics_path, "r") as f:   #open path and read into a variable to later use in our UI for display
            lyrics = f.read()
        
        split_lyrics = lyrics.split(" ")
        new_lyrics = ""
        for i in range(len(split_lyrics)):
            if i % 5 == 0:
                new_lyrics += " ".join(split_lyrics[i-5:i]) + "\n"         
    
        new_lyrics = new_lyrics.strip()
            
        #Display the results on Tkinter Labels
        #========================================================================================================
        #Display BPM
        self.BPM_result = customtkinter.CTkLabel(master=self.bpm_frame, text=self.bpm_arr[0], text_font=("Roboto Medium", -14))
        self.BPM_result.grid(column=1, row=1, sticky="nwe", padx=15, pady=15)
        #Display mood
        self.mood_result = customtkinter.CTkLabel(master=self.mood_frame, text=self.mood_arr[0], text_font=("Roboto Medium", -14))
        self.mood_result.grid(column=0, row=1, sticky="nwe", padx=15, pady=15)
        #Display genre
        self.genre_result = customtkinter.CTkLabel(master=self.genre_frame, text=genre_string, text_font=("Roboto Medium", -14))
        self.genre_result.grid(column=1, row=1, sticky="nwe", padx=15, pady=15)
        #Display Lyrics
        self.lyrics_box = customtkinter.CTkLabel(master = self.border_frame2, text = new_lyrics, text_font=("Roboto Medium", -12), height=100, corner_radius=6, fg_color = ("white", "gray38"))
        self.lyrics_box.grid(column=1, row=2, sticky ="nesw")        


    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)

        #Create a button that allows the user to switch to another window
        switch_window_button = customtkinter.CTkButton(
            self, text="Return to Home Page", command=lambda: controller.show_frame(HomePage)
        )
        switch_window_button.grid(row=8,column=0, columnspan=4, sticky= "sw")

        #Create a border frame for aesthetic
        self.border_frame = customtkinter.CTkFrame(self)
        self.border_frame.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        #Create a frame where our main bulk of the page will lie
        self.border_frame2 = customtkinter.CTkFrame(self.border_frame)
        self.border_frame2.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        #Create a button that sparks the program to analyze the mp3 file in the directory
        analyze_button = customtkinter.CTkButton(
            self.border_frame2, text="Analyze", command=self.get_results
        )
        analyze_button.grid(column = 1, row = 6, sticky = "nesw", pady=5)

        #title
        self.title_label = customtkinter.CTkLabel(master=self.border_frame2, text="Analysis", text_font=("Roboto Medium", -20))
        self.title_label.grid(column=1, row=0, sticky="nesw", padx=5, pady=5)
        
        
        #progress bar for later implementation
        #self.progressbar = customtkinter.CTkProgressBar(master=self.border_frame2)
        #self.progressbar.grid(row=2, column=1, sticky="nesw")

        #Create mood, bpm, genre frames to lay on top
        self.mood_frame = customtkinter.CTkFrame(self.border_frame2)
        self.mood_frame.grid(column = 0, row = 0, pady=40)
        self.bpm_frame = customtkinter.CTkFrame(self.border_frame2)
        self.bpm_frame.grid(column = 1, row = 0)
        self.genre_frame = customtkinter.CTkFrame(self.border_frame2)
        self.genre_frame.grid(column = 2, row = 0)

        #Configure mood, bpm, genre grid manager
        self.mood_frame.rowconfigure(0, weight=1)
        self.mood_frame.columnconfigure(0, weight=1)

        self.bpm_frame.rowconfigure(0, weight=1)
        self.bpm_frame.columnconfigure(0, weight=1)

        self.bpm_frame.rowconfigure(0, weight=1)
        self.bpm_frame.columnconfigure(0, weight=1)

        #Create Labels within each mini-frame
        self.mood_label = customtkinter.CTkLabel(master=self.mood_frame, text="Mood", text_font=("Roboto Medium", -18))
        self.mood_label.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)
        self.bpm_label = customtkinter.CTkLabel(master=self.bpm_frame, text="BPM", text_font=("Roboto Medium", -18))
        self.bpm_label.grid(column=1, row=0, sticky="nwe", padx=15, pady=15)
        self.genre_label = customtkinter.CTkLabel(master=self.genre_frame, text="Genre", text_font=("Roboto Medium", -18))
        self.genre_label.grid(column=1, row=0, sticky="nwe", padx=15, pady=15)


        self.border_frame2.columnconfigure(1, weight=1)
        self.border_frame2.rowconfigure(1, weight=1)

        self.border_frame.columnconfigure(1, weight=1)
        self.border_frame.rowconfigure(1, weight=1)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)


class PerformancePage(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        label = customtkinter.CTkLabel(self, text="Performance Page, we did it!")
        label.pack(padx=10, pady=10)

        switch_window_button = customtkinter.CTkButton(
            self, text="Return to Home Page", command=lambda: controller.show_frame(HomePage)
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


if __name__ == "__main__":
    testObj = windows()
    testObj.geometry("1100x720")
    testObj.mainloop()