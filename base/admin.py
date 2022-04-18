from django.contrib import admin
from .models import Note, User

# Register your models here.
admin.site.register(Note)
admin.site.register(User)
# admin.site.register(Notepad)