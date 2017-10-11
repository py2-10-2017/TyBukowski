from django.shortcuts import render, redirect

# Create your views here.
def survey(request):

    return render(request,"surveys/survey.html")

def process(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1

    request.session['name'] = request.POST['name']
    request.session['dojo_location'] = request.POST['dojo_location']
    request.session['fav_language'] = request.POST['fav_language']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')

def result(request):
    post_info = {
        'name':request.session['name'],
        'dojo_location':request.session['dojo_location'],
        'fav_language':request.session['fav_language'],
        'comment':request.session['comment']
    }

    return render(request,"surveys/result.html", post_info)
