from django.contrib import admin

from polls.models import Question, Osoba

admin.site.register(Osoba, Osoba.OsobaAdmin)

admin.site.register(Question)
# admin.site.register(Osoba)
