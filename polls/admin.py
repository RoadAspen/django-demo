from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'pub_date')


@admin.register(models.Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'choice_text', 'votes')
