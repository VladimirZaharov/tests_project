from django.urls import path

from tests.views import index, categories, run, statistic

app_name = 'tests'

urlpatterns = [
    path('', categories, name='index'),
    path('<int:category_id>/', categories, name='category'),
    path('testing/<int:test_id>/', run, name='testing'),
    path('statistic', statistic, name='statistic'),
]
