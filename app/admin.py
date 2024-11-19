from django.contrib import admin
from .models import Questions, Voted
# Register your models here.
admin.site.register(Questions)
admin.site.register(Voted)