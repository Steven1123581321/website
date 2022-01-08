import json
import os
from django.shortcuts import render
from cv.models import Cv2

# main index view
def index(request):
    # file_path = "./cv/static/configuration/configuration.json"
    # with open(file_path) as f:
    #     configuration = json.loads(f.read())
    # return render(request, "cv_index.html", configuration)
    file_path = "./cv/configuration/configuration.json"
    with open(file_path) as f:
        configuration = json.loads(f.read())
    cv = Cv2.objects.all()
    context = {"cv": cv}
    context.update(configuration)
    return render(request, "cv_index_2.html", context)
