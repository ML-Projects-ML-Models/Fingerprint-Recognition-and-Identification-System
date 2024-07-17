from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(FingerImage)
admin.site.register(FaceImage)
admin.site.register(PredictImage)