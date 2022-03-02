from django.contrib import admin

# Register your models here.
from .models import Movie, Payment, Profile, CustomUser, Video

# Register your models here

admin.site.register(Movie)
admin.site.register(Profile)
admin.site.register(Video)
admin.site.register(CustomUser)
admin.site.register(Payment)
