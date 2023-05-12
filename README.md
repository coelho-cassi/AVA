The program was built using python v3.10.8

The required dependencies can be installed using: 
pip install customtkinter
pip install pillow
pip install librosa
pip install text2emotion
pip install spleeter
pip install git+https://github.com/openai/whisper.git 
pip install --upgrade numpy==1.23.5
pip install --upgrade emoji==1.6.3
pip install --upgrade numba==0.56.4
pip install --upgrade moviepy==1.0.3

NOTE: To execute the program, three preconditions must be met:

ffmpeg is installed
Blender 3.4 is installed
nltk has downloaded the required resources

To install ffmpeg follow this tutorial:
	https://phoenixnap.com/kb/ffmpeg-windows

Have NLTK update:
	1. Open AVA\Text2Emotion\Extra directory
	2. Execute: python getnltk.py

To run AVA:
	1. Open AVA directory in a terminal
	2. Execute: python AVA.py
