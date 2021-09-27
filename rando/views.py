from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def rand(request):
   if request.method == "GET":
      request.session['randomNum'] = "[Click below to generate a random string]"
      request.session['counter'] = 0
      return render(request, "random_word.html")
   if request.method == "POST":
      request.session['randomNum'] = get_random_string(14)
      request.session['counter'] += 1
      return render(request, "random_word.html")

def reset(request):
   request.session['counter'] = 0
   return redirect("/random_word")