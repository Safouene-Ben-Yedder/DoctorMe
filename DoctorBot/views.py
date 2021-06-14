from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
import streamlit as st 


def DoctorBot(request):

    return render(request, 'DoctorBot.html')


def Doc(request):

                #Recognize the speech and words
            r = sr.Recognizer()
            #use microphone the source of questions
            def record_audio(ask = False):
                with sr.Microphone() as source:
                    if ask:
                        #print(ask)
                        alexis_speak(ask)
                    #Listen method --> pass our source ( microphone )
                    audio = r.listen(source)
                    #Create a variable for our voice data and pass the audio variable ( catch the voice data)
                    try:
                        voice_data = r.recognize_google(audio)
                #Step 1 : Listen and print it in the console 
                #Get what we say into the console and then print it in the console 
                #Get response and implement google text to speech
                #So Alexa can talk back ( google )
                    except sr.UnknownValueError:
                        #print('Sorry, I did not get that')
                        alexis_speak('Sorry, I did not get that')
                    except sr.UnknownValueError:
                        #print('Sorry, my speech service is down')
                        alexis_speak('Sorry, my speech service is down')
                    return voice_data

            def alexis_speak(audio_string):
                tts = gTTS( text = audio_string, lang='en')
                #we can use other languages 
                r = random.randint(1, 10000000)
                #create the audio file
                audio_file = 'audio-' + str(r)+ '.mp3'
                tts.save(audio_file)
                playsound.playsound(audio_file)
                print(audio_string)
                os.remove(audio_file)


            #Alexa will respond
            def respond(voice_data):
                if 'what is your name' in voice_data:
                    #print('My name is Alexis')
                    alexis_speak('My name is Alexis')
                if 'what time is it ' in voice_data:
                    #print(ctime())
                    alexis_speak(ctime())
                if 'search' in voice_data:
                    search = record_audio('What do you want to search for ')
                    url = 'https://google.com/search?q='+ search
                    webbrowser.get().open(url)
                    #print('Here is what I found ' + search)
                    alexis_speak('Here is what I found ' + search)
                if 'find location' in voice_data:
                    location = record_audio('What is the location')
                    url = 'https://google.nl/maps/place/'+ location + '/&amp;'
                    webbrowser.get().open(url)
                    #print('Here is the location of  ' + location)
                    alexis_speak('Here is the location of  ' + location)
                if 'exit' in voice_data:
                    exit()


            #time.sleep(1)
            #print('Hello, How can I help you')
            alexis_speak('Hello, How can I help you')
            while(1):
                voice_data = record_audio()
                respond(voice_data)
                #print(voice_data)

            return render(request, 'DoctorBoxTalk.html')


