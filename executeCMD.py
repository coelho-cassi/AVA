import os
import subprocess
from moviepy.editor import *

# ***************************************
# Main function used for testing purposes
# NOTE:
#  All paths are hard-coded and need to
#  changed depending on the computer
#  used for execution. Run using the
#  execute function for dynamic
#  execution.
#
# ***************************************
def main():
    # First, I run blender to edit the template.blend file
    subprocess.run(args=["C:\\Program Files\\Blender Foundation\\Blender 3.4\\blender","--background", "--python", "C:\\Users\\jnchi\\Documents\\Current_Classes\\CS-4391_(Senior_Project_II)\\Workplace\\runBlender.py", "--", "C:\\Users\\jnchi\\Documents\\Current_Classes\\CS-4391_(Senior_Project_II)\\Workplace\\template.blend", "C:\\Users\\jnchi\\Documents\\Current_Classes\\CS-4391_(Senior_Project_II)\\Workplace\\test.blend", "C:\\Users\\jnchi\\Documents\\Current_Classes\\CS-4391_(Senior_Project_II)\\Workplace\\sample1.mp3", "C:\\Users\\jnchi\\Documents\\Current_Classes\\CS-4391_(Senior_Project_II)\\Workplace\\vocals.wav", "C:\\Users\\jnchi\\Documents\\Current_Classes\\CS-4391_(Senior_Project_II)\\Workplace\\accompaniment.wav"],shell=True)
       
    
    # Second, I rerun blender using the edited file and generate the frames
    subprocess.run(args=["C:\\Program Files\\Blender Foundation\\Blender 3.4\\blender", "--background", "C:\\Users\\jnchi\\Documents\\Current_Classes\\CS-4391_(Senior_Project_II)\\Workplace\\test.blend","-o","//temp\\png-######","-a"],shell=True)


# *********************************************
# Execute function used for dynamic execution
# *********************************************
def execute(directoryPATH):
    # directoryPATH must be a raw string or have '\\' instead of '\'
    
    # Defining the files
    blenderPY = directoryPATH + "\\runBlender.py"
    template = directoryPATH + "\\template.blend"
    test = directoryPATH + "\\test.blend"     # "test.blend" does not have to exist in the directory, all other files must be present 
    mainMP3 = directoryPATH + "\\sample1.mp3" # Might need to rename the given audio sample to a certain name so that this script can find it.
    lyricMP3 = directoryPATH + "\\vocals.wav"
    accompMP3 = directoryPATH + "\\accompaniment.wav"
    
    # Run Blender with the Template file and bake the mp3s to the Avatar
    subprocess.run(args=["C:\\Program Files\\Blender Foundation\\Blender 3.4\\blender","--background", "--python", blenderPY, "--", template, test, mainMP3, lyricMP3, accompMP3],shell=True)
    
    # Rerun Blender with the modified file from the previous step and generate the frames in a folder temp
    subprocess.run(args=["C:\\Program Files\\Blender Foundation\\Blender 3.4\\blender", "--background", test,"-o","//__temp\\png-######","-a"],shell=True)
    
    # Creating the Video from the Images and Adding Audio    
    frameFolder = directoryPATH + "\\__temp"
    frame_files = [os.path.join(frameFolder,file)
               for file in os.listdir(frameFolder)
               if file.endswith(".png")]
    clip = ImageSequenceClip(frame_files,fps=24)
    clip.write_videofile("test.mp4",fps=24,audio="sample1.mp3")
    
    # Cleaning Up
    try:
        # Delete Frames from Local Memory
        os.chdir(frameFolder)
        temp = ""
        for fname in os.listdir():
            temp = frameFolder + "\\"
            temp = temp + fname
            os.remove(temp)
        os.chdir(directoryPATH)
        # Remove the now empty temp directory
        os.rmdir(frameFolder)
        
        # Delete pycache folder
        cache = directoryPATH + "\\__pycache__"
        os.chdir(cache)
        for fname in os.listdir():
            temp = cache + "\\"
            temp = temp + fname
            os.remove(temp)
        os.chdir(directoryPATH)
        # Remove the now empty cache directory
        os.rmdir(cache)
        
        # Lastly, remove the test.blend file.
        os.remove(test)
    except OSError as E:
        print("Error during Deletion:\n")
        print(E)
        
    
   
if __name__ == "__main__":
    main()