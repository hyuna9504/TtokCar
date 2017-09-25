#-*- coding: utf-8 -*-

from flask import Flask
from flask_ask import Ask, statement
import RPi.GPIO as GPIO
import time
import os
from omxplayer import OMXPlayer
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
p = GPIO.PWM(14, 50)

app = Flask(__name__)
ask = Ask(app, '/')

@app.route('/')
def homepage():
    return "Raspberry pi LED control"

@ask.launch
def start_skill():
    welcome_message = "Hi hyeona, Welcome to Raspberry pi."
    return statement(welcome_message)

@ask.intent("LEDOnIntent")
def led_on():
    GPIO.output(22, True)
    GPIO.output(17, True)
    time.sleep(0.5)
    text = "ok, LED was Turned on"
    return statement(text)

@ask.intent("LEDOffIntent")
def led_off():
    GPIO.output(22, False)
    GPIO.output(17, False)
    time.sleep(0.5)
    text = "ok, LED was Turned out"
    return statement(text)

@ask.intent("TrunkOpenIntent")
def trunk_open():
    GPIO.output(14, True)
    p.start(0)
    p.ChangeDutyCycle(7.5)
    time.sleep(1)
    p.stop(0)
    text = "ok, trunk was opened"
    return statement(text)

@ask.intent("TrunkCloseIntent")
def trunk_close():
    GPIO.output(14, True)
    p.start(0)
    p.ChangeDutyCycle(2.5)
    time.sleep(1)
    p.stop(0)
    text = "ok, trunk was closed"
    return statement(text)

@ask.intent("SongIntent")
def music():
    text = "wow, exciting song"
    file_path='/home/pi/music.mp3'
    player=OMXPlayer(file_path)
    player.play()
    sleep(7)
    player.pause()
    player.quit()
    return statement(text)

@ask.intent("JuneIntent")
def june():
    sleep(1)
    text = "he is a famous professor who teaches graduation project classes at Seoul Womens's University. and He will give you a A plus grade."
    return statement(text)

@ask.intent("HIntent")
def hyuna():
    sleep(1)
    text = " Sure, It's you."
    return statement(text)

    

if __name__ == "__main__":
    app.run(debug = True)

