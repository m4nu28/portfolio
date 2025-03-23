from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    dark_mode = request.session.get('dark_mode', False)
    return render(request, 'home.html', {'dark_mode': dark_mode})

def toggle_theme(request):
    dark_mode = request.session.get('dark_mode', False)
    request.session['dark_mode'] = not dark_mode
    return redirect('home')