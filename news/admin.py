from django.contrib import admin
from .models import Uploads
from .models import Uploads, Commenting

# Register your models here.
admin.site.register(Uploads)
admin.site.register(Commenting)