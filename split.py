import subprocess

songfile = "spleeter/dontstopbelieving.mp3"
command = "spleeter separate -o audio_output " + songfile
subprocess.run(command,shell=True)