from django.db import models

class DualDeskRequest(models.Model):
    user = models.CharField(max_length=255)
