from django.contrib import admin

from questions.models import Question, Answer

admin.site.register(Question)

@admin.register(Answer)
class TestAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_right')
    search_fields = ('name',)