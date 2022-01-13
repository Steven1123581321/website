import json
import os
from django.shortcuts import render
from cv.models import Cv2

# main index view
def index(request):
    cv = Cv2.objects.all()
    context = {"cv": cv}
    return render(request, "cv_index.html", context)
