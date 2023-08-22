import os

# Check if the script is running with administrator privileges
if os.geteuid() != 0:
    print("This script must be run as administrator. Please restart with 'sudo'.")
    exit()

import sounddevice as sd
import threading
import numpy as np
from scipy.io.wavfile import write
import keyboard
import time
from datetime import datetime

def record_audio(buffer, samplerate):
    with sd.InputStream(samplerate=samplerate) as stream:
        print("Recording...")
        while not exit_recording:
            if not pause_recording:
                frames, _ = stream.read(chunk_size)
                buffer.extend(frames)

input_device = sd.default.device[0]
device_info = sd.query_devices(input_device, 'input')

samplerate = 44100
channels = device_info['max_input_channels']
chunk_size = 1024

buffer = []
pause_recording = False
exit_recording = False

seconds = int(input("Enter recording time in seconds: "))
total_chunks = int(seconds * samplerate / chunk_size)

recording_thread = threading.Thread(target=record_audio, args=(buffer, samplerate))
recording_thread.start()

for _ in range(total_chunks):
    if exit_recording:
        break

    if keyboard.is_pressed('space'):
        pause_recording = not pause_recording
        print("Paused" if pause_recording else "Resumed")
        while keyboard.is_pressed('space'):
            pass

    if keyboard.is_pressed('esc'):
        exit_recording = True
        print("Exiting...")
        break

    time.sleep(chunk_size / samplerate)

exit_recording = True
recording_thread.join()
recorded_data = np.vstack(buffer)

current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_filename = f"output_{current_time}.wav"
write(output_filename, samplerate, recorded_data)

print(f"Done. Recording saved as {output_filename}")
