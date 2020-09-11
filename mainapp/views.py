from django.shortcuts import render

def profile_page(request):
    return render(request, 'students/profile.html')

def transcript_page(request):
    return render(request, 'students/transcript.html')

def changepassword_page(request):
    return render(request, 'students/changepassword.html')

def suggestioncourse_page(request):
    return render(request, 'students/suggestioncourse.html')

def scoreforecast_page(request):
    return render(request, 'students/scoreforecast.html')

def statistical_page(request):
    return render(request, 'students/statistical.html')