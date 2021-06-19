from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
import random
from mysite.models import Post, 食譜, 食材
from django.contrib import auth

def index(request):
	posts= Post.objects.all()
	myname = "peggy"
	data=[i for i in range(1, 43)]
	random.shuffle(data)
	lotto_numbers = data[0:6]
	special_number=data[6]
	return render(request, 'index.html', locals())

def show(request, id):
	try:
		target=Post.objects.get(id=id)
	except:
		return redirect("/")
	return render(request, "showpost.html", locals())

def logout(request):
	auth.logout(request)
	return redirect("/")

def rank(request):
	食材 = 食譜.objects.all()
	return render(request, "rank.html", locals())