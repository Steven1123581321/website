from django.shortcuts import render

# main index view
def index(request):
    return render(request, "homepage.html", context={})
