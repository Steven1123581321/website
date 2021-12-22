import json
import os
from django.shortcuts import render
from personal_portfolio import settings

# main index view
def index(request):
    file_path = "./cv/static/configuration/configuration.json"
    with open(file_path) as f:
        configuration = json.loads(f.read())
    return render(request, "cv_index.html", configuration)
