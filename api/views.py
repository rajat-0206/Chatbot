from django.shortcuts import render,HttpResponse

from chatterbot import ChatBot

from chatterbot.trainers import ChatterBotCorpusTrainer

import risp.views

from rest_framework import status

from rest_framework.response import Response

from rest_framework.decorators import api_view

englishbot = ChatBot("Chatterbot", storage_adapter = "chatterbot.storage.SQLStorageAdapter")

trainer = ChatterBotCorpusTrainer(englishbot)

trainer.train("chatterbot.corpus.english")

# Create your views here.
@api_view(["GET",])
def askrisp(request):
    query = request.GET["query"]
    if(query=="bye"):
        ans = ending()
        return Response(ans,status=status.HTTP_200_OK)
    ans = str(englishbot.get_response(query))
    if(ans=='Artificial Intelligence is the branch of engineering and science devoted to constructing machines that think.'):
            ans = wiki(query)
            if(ans==False):
                return Response("Sorry I did not get that ",status=status.HTTP_200_OK)
            else:
                return Response(ans,status=status.HTTP_200_OK)
    else:
        return Response(ans,status=status.HTTP_200_OK)