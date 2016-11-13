from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    if not 'numsubmissions' in request.session:
        request.session['numsubmissions'] = 0

    return render(request, 'surveyinfo/index.html')

def processPost(request):
    request.session['your_name'] = request.POST['your_name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comments'] = request.POST['comments']
    request.session['numsubmissions'] += 1
    return redirect('/show_info')

def show_info(request):
    return render(request, 'surveyinfo/show_info.html')
