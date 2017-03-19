from django.shortcuts import render


def about(request):
	return render(request, "about.html", {})


def location(request):
	return render(request, "location.html", {})

def failure(request):
	return render(request, "failure.html", {})
