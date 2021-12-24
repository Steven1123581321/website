from django.db import models

# Create your models here.
class Cv2(models.Model):
    Name = models.CharField(max_length=100)
    Surname = models.CharField(max_length=100)
    avatar = models.FilePathField(path="/img")
    role = models.CharField(max_length=100, default="Research Scientist")
    github = models.URLField(
        max_length=100, default="https://github.com/Steven1123581321"
    )
    linkedin = models.URLField(
        max_length=100, default="https://linkedin.com/in/steven-pauly-80760b48"
    )
    research_gate = models.URLField(
        max_length=100, default="https://www.researchgate.net/profile/Steven-Pauly"
    )
    welcome_title = models.TextField()
    welcome_text = models.TextField()
