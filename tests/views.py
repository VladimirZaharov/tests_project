from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from tests.models import TestCategory, Test
from users.models import User, UserStatistic


def index(request):
    return render(request, 'tests/index.html' )


def categories(request, category_id=None):
    context = {'title': 'Тестирование - Каталог', 'categories': TestCategory.objects.all()}
    if category_id:
        tests = Test.objects.filter(category=category_id)
    else:
        tests = Test.objects.all()
    context['tests'] = tests
    return render(request, 'tests/categories.html', context)


def statistic(request):
    user = request.user
    statistics = UserStatistic.objects.filter(user=user.id)
    context = {'statistics': statistics}
    return render(request, 'users/statistic.html', context)


@login_required(login_url='tests:index')
def run(request, test_id=None):
    user = User.objects.filter(username=request.user).first()
    if user.current_test:
        return render(request, 'tests/testing.html')
    else:
        if test_id:
            return render(request, 'tests/testing.html')
        else:
            return render(request, 'tests/testing.html')
