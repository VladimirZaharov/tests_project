from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from tests.models import TestCategory, Test
from users.models import User, UserStatistic
from tests.utils import start_testing, check_answer, ask_question, end_test_and_show_result


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
    context = {'tests': statistics}
    return render(request, 'users/statistic.html', context)


@login_required(login_url='tests:index')
def run(request, test_id=None):
    user = User.objects.get(username=request.user)
    if user.current_test:
        if request.method == "POST":
            context = check_answer(request, user)
            return render(request, 'tests/result.html', context)
        context = ask_question(user)
        if context:
            return render(request, 'tests/testing.html', context)
        context = end_test_and_show_result(user)
        return render(request, 'tests/result.html', context)
    else:
        # try:
            context = start_testing(request, test_id)
            return render(request, 'tests/testing.html', context)
        # except Exception as e:
        #     return render(request, 'tests/index.html')