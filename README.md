# Brycemodem

I wanted to revive some knowledge from my past life as an electrical engineer, so I started making a modem in Python.  Idea is that two computers could communicate using their speaker and micorphone, across a room, with random acoustic conditions.  I used the simplest form of everything so I could get it working in an afternoon, which I did.


The first swing looks like this

* Not realtime opertation, not streaming.
* Uses pyaudio, which has event-driven access to read/write binary data to the audio devices.
* AM modulation
* Use FIR/sinc filters, because they are easy to design and cost nothing if I'm not running real-time.
* No equalization.
* No error correction, channel coding, diversity.
* No PLLs or other syncronization
* No AGC in the usual sense, though it is not sensitive to the level of the signal.
* 2 khz carrier, 10 baud.  


The next steps

* Make into a real-time streaming system which can transmit a stream from one computer to another (or support PPP, if it were fast-enough).
* Make moduler-enough that adapting various parts of it isn't all that diffiult:  Try to decouple the different pieces to the extent possible.


Modules might be

* Carrier PLL
* Channel coding
* Channel equalization 
* Chip PLL
* Modulation scheme/constelation 
* Configurable generic mixers, or something which can bring a signal down to baseband.
* Diagnostics


It's been years since I've fussed with this stuff.  I had such a fun time doing it, I reckon I'll press on.
