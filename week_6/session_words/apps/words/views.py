# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.
def reroute(request):
    return redirect('/session_words')

def index(request):

    return render(request, 'words/index.html')

def add(request):
    # print request.POST
    new_word = {}
    for key, value in request.POST.iteritems():
        if key == "big":
            new_word['big'] = "big"
        if key != "big":
            new_word[key] = value

    new_word['created_at'] = datetime.now().strftime("%I:%M %p, %B %d, %Y")
    
    try:
        request.session['word']
    except KeyError:
        request.session['word'] = []

    temp_list = request.session['word']
    temp_list.append(new_word)
    request.session['word'] = temp_list


    # word = request.POST['word']
    # color = request.POST['color']
    # time = datetime.now().strftime("%I:%M %p, %b %d %Y" ) #correct to format: 9:15:23pm June 4th, 2017
    # # big = request.POST['big_font']

    # session_word = {
    #     'word': word,
    #     'color': color,
    #     'time': time
    # }    

    # temp_word = request.session['word']
    # temp_word.append(session_word)
    # request.session['word'] = temp_word
    # new_word = request.session['word']
    
    

    return redirect('/session_words')

def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/session_words')
