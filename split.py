import subprocess

songfile = "Radiohead_Spectre.mp3"
command = "spleeter separate --verbose -d 500 -o audio_output " + songfile
subprocess.run(command,shell=True)