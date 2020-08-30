from django.shortcuts import render,HttpResponse

import datetime

import json

import wikipedia

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

englishbot = ChatBot("Chatterbot", storage_adapter = "chatterbot.storage.SQLStorageAdapter")

trainer = ChatterBotCorpusTrainer(englishbot)

trainer.train("chatterbot.corpus.english")


def greeting():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
         return "Good Morning"
    elif hour>=12 and hour<18:
        "Good Afternoon"
    else:
        speak("Good Evening")
    speak("I am Jarvis. How may I help you")

def ending():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour <3 or hour>=20 and hour<=23):
        return "Byeeee see you tomorrow. Good Night"
    else:
        return "Byeeeee. Have a good day ahead"

def wiki(query):
    try:
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences =2)
        return "According to wikipedia " + results
    except:
        return False

def askrisp(request):
    query = request.GET["query"]
    if(query=="bye"):
        ans = ending()
        return HttpResponse(ans)
    ans = str(englishbot.get_response(query))
    if(ans=='Artificial Intelligence is the branch of engineering and science devoted to constructing machines that think.'):
            ans = wiki(query)
            if(ans==False):
                return HttpResponse("Sorry I did not get that")
            else:
                return HttpResponse(ans)
    else:
        return HttpResponse(ans)

def home(request):
    return render(request,"home.html")

def temp(request):
    return render(request,'risp.html')
