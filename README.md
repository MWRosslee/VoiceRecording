# VoiceRecording
This program records audio from the default input device, allowing the user to pause, resume, or exit the recording using specific key presses. It then saves the recorded audio to a file with a timestamp.

This is how it works

Check Administrator Privileges:
The script checks if it is running with administrator privileges using os.geteuid(). If not, it prints a message and exits.

Import Libraries:
Various libraries are imported to handle sound recording, file writing, threading, keyboard input, and time manipulation.
Define Recording Function:
The record_audio function handles audio recording. It reads audio data from the input device in chunks and appends it to a buffer.

Get Input Device Information:
The default input device is identified, and its capabilities (such as the maximum number of input channels) are queried.

Set Parameters:
Parameters like sample rate, number of channels, and chunk size are set.

Initialize Variables:
Buffer and flags for controlling recording (pause and exit) are initialized.

User Input for Recording Time:
The user is asked to input the recording time in seconds.

Start Recording Thread:
The record_audio function is started in a separate thread, allowing parallel execution with the main program.

Monitor Keypresses:
A loop monitors for keypresses to control recording:
Spacebar: Toggles pause and resume.
Esc key: Exits the recording.

Control Timing:
time.sleep is used to control the timing of the recording chunks, synchronizing with the sample rate.

Stop Recording:
The recording thread is joined, ensuring all audio data is captured.

Compile Recorded Data and Save:
The recorded audio data in the buffer is compiled into a single array.
The current date and time are formatted into a string.
The recording is saved to a file named output_<timestamp>.wav.

Print Completion Message:
A completion message is printed to the console, confirming the successful recording and filename.
This script integrates various functionalities to provide a flexible audio recording tool, allowing the user to control the recording process interactively. It demonstrates a combination of threading, sound processing, and user interaction in Python.
