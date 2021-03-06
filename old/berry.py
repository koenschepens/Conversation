#!/usr/bin/python
import pyvona
import time
import os
import RPi.GPIO as GPIO
import subprocess
from subprocess import call
import signal

hoorn = 11
#buzzer = 26
	
runningPid = -1

stdin_path = '/dev/null'
stdout_path = '/dev/tty'
stderr_path = '/dev/tty'
pidfile_path =  '/tmp/barry.pid'
pidfile_timeout = 5

#v = pyvona.create_voice("GDNAIRN4SS66PRNKPQZQ","2gURBTiaqnkjxEXZX+cslGhkJ+OVKTzWCZg7mvpp")
#v.speak("Hello! How nice of you to drop by.")

#GPIO.setup(buzzer, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(hoorn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
new=True
while True:
            if(GPIO.input(hoorn) == 1):
                rang=False
		print("Picked up the phone")
                #say hello
                #call(["/home/osmc/Pi/PiAUISuite/ReadSpeaker/sayhello"])
		print("Starting voice command")
                #call voicecommand daemon
		os.system('pkill voicecommand')
		voicecommand = subprocess.Popen(["/home/osmc/Pi/PiAUISuite/VoiceCommand/voicecommand", "-c",  "-f", "/home/osmc/Pi/PiAUISuite/VoiceCommand/.commands.conf"])
		runningPid = voicecommand.pid;
		print("wait until hanging up...")
		while(GPIO.input(hoorn) == 1):
	                #call(["/home/osmc/Pi/PiAUISuite/ReadSpeaker/anythingelse"])
	                #voicecommand = subprocess.Popen(["/home/osmc/Pi/PiAUISuite/VoiceCommand/voicecommand", "-c", "-f", "/home/osmc/Pi/PiAUISuite/VoiceCommand/.commands.conf"])
			#runningPid = voicecommand.pid;
			time.sleep(1)
            if(GPIO.input(hoorn) == 0):
		os.system('pkill voicecommand')
		if(new):
			print("Phone is down")
			new=False
		else:
			print("Hung up")
	                subprocess.Popen(["/home/osmc/Pi/PiAUISuite/KodiTools/say","Bye!"])
		while (GPIO.input(hoorn) == 0):
			#wait until someone picks up the phone
			time.sleep(1)

	    GPIO.cleanup()

