from django.shortcuts import render

def login_page(request):
    return render(request, 'students/login.html')

def manageuser_page(request):
    return render(request, 'adminuet/manageuser.html')

def trainingframework_page(request):
    return render(request, 'adminuet/trainingframework.html')

def subject_page(request):
    return render(request, 'adminuet/subject.html')

def learningoutcome_page(request):
    return render(request, 'adminuet/learningoutcome.html')

def suggestioncourse_page(request):
    return render(request, 'adminuet/suggestioncourse.html')

def scoreforecast_page(request):
    return render(request, 'adminuet/scoreforecast.html')

def statistical_page(request):
    return render(request, 'adminuet/statistical.html')