from django.contrib import admin

# Register your models here.
from movie.models import Movie, Review

admin.site.register(Movie)
admin.site.register(Review)
