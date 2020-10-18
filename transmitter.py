

import pyaudio
import time
import numpy as np
import wave
import random
import string

# my code
import common as c


message = "Bryce is a sexy bitch. And he adores Cody more than anything!!!" 

letters = string.ascii_lowercase
message = "".join( random.choice(letters) for i in range(0,len(message)*500 ) )

fs = 16000

one_amplitude = 1.0
zero_amplitude = 0.25
baud = 3000
chip_period = 1 / baud # in seconds

carrier_freq = 3000
sync_freq = 500

# let's start by assembling the whole signal a priori and sending at once

# structure of the signal:
# (1) 250ms of 500 hz + 250ms of silence + 250ms of 500 hz + 250ms of silence
# (2) 250ms of 2 khz carrier 
# (3) AM modulated carrier, baud rate is 10 (for now)
# (4) 250ms of silence
# (5) 250ms of 500 hz + 250ms of silence + 250ms of 500 hz + 250ms of silence

signal = []

signal.append( c.make_sine_wave(0.25, fs=fs, freq=sync_freq ) )
signal.append( c.make_silence(0.25, fs=fs ) )
signal.append( c.make_sine_wave(0.25, fs=fs, freq=sync_freq ) )
signal.append( c.make_silence(0.25, fs=fs ) )

signal.append( c.make_sine_wave(0.25, fs=fs, freq=carrier_freq ) )

for bit in c.string_to_binary(message):

	signal.append( ( one_amplitude if bit else zero_amplitude ) * 
		c.make_sine_wave( chip_period, fs=fs, freq=carrier_freq ) )

signal.append( c.make_silence(0.25, fs=fs ) )

signal.append( c.make_sine_wave(0.25, fs=fs, freq=sync_freq ) )
signal.append( c.make_silence(0.25, fs=fs ) )
signal.append( c.make_sine_wave(0.25, fs=fs, freq=sync_freq ) )
signal.append( c.make_silence(0.25, fs=fs ) )


signal_bytes = c.normalized_wf_to_bytes( np.concatenate( signal ) )

print(signal_bytes)


# save the file for good measure

with wave.open("out.wav","wb") as ww:

	ww.setnchannels(1)
	ww.setsampwidth(2)
	ww.setframerate(fs)
	ww.writeframes( signal_bytes )




if False:




	# instantiate PyAudio (1)
	p = pyaudio.PyAudio()

	# define callback (2)
	def callback(in_data, frame_count, time_info, status):

	    print(frame_count)

	    data = wf.readframes(frame_count)
	    return (data, pyaudio.paContinue)

	# open stream using callback (3)
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
	                channels=wf.getnchannels(),
	                rate=wf.getframerate(),
	                output=True,
	                stream_callback=callback)

	# start the stream (4)
	stream.start_stream()

	# wait for stream to finish (5)
	while stream.is_active():
	    time.sleep(0.1)

	# stop stream (6)
	stream.stop_stream()
	stream.close()
	wf.close()

	# close PyAudio (7)
	p.terminate()