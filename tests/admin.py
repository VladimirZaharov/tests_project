from django.contrib import admin

from tests.models import TestCategory, Test


admin.site.register(TestCategory)


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)
