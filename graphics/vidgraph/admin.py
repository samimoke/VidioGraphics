from django.contrib import admin
from .models import Contactus, Blog,User

# Register your models here.
admin.site.register(Contactus)
admin.site.register(Blog)
admin.site.register(User)