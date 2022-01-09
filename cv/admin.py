from django.contrib import admin

# Register your models here.
from django.contrib import admin
from cv.models import Cv2


class CvAdmin(admin.ModelAdmin):
    fields = ["welcome_title", "welcome_text", "video"]


admin.site.register(Cv2, CvAdmin)
