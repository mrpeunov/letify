from django.contrib import admin


@admin.register(Attempt)
class AttemptAdmin(Attempt):
    pass