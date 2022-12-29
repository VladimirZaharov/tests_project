import random

from questions.models import Question
from tests.forms import TestForm
from tests.models import Test
from users.models import UserStatistic, User


def get_question(question_obj) -> dict:
    """
    Принимает вопрос-объект, возвращает словарь вопрос-ответы и форму для контекста
    """
    answers = question_obj.answers.all()
    answers_list = []
    for num, answer in enumerate(answers):
        if answer.name:
            a = {'num': num + 1, 'answer': answer.name}
            answers_list.append(a)
    question_dict = {'question_name': question_obj.name, 'answers': answers_list}
    if not question_obj.one_answer:
        form = TestForm()
        return {'question': question_dict, 'form': form}


def get_new_test(request) -> int:
    """
    Возвращает id непройденого случайного теста
    """
    user_statistic = UserStatistic.objects.filter(user=request.user)
    if user_statistic:
        pasted_tests = [usr.test for usr in user_statistic]
        tests = Test.objects.exclude(id in pasted_tests)
        test = random.choice(tests)
    else:
        test = Test.objects.all().first()
        test = test.id
    return test


def start_testing(request, test_id: int = None) -> dict:
    """
    Заполняет json поле пользователя с id вопросов, возвращает словарь вопрос-ответы
    """
    if not test_id:
        test_id = get_new_test(request)
    test = Test.objects.filter(id=test_id)
    questions = Question.objects.prefetch_related('answers').filter(test=test.id)
    questions_list = [question.id for question in questions]
    random.shuffle(questions_list)
    question = questions_list.pop()
    user = User.objects.filter(username=request.user)
    user.current_test = {'rest_questions': questions_list,
                          'history': {'question': question, 'right_answers': 0, 'wrong_answers': 0}}
    question = questions.get(id=question)
    context = get_question(question)
    user.questions['history']['answers'] = {a_dict['num']: a_dict['answer'] for a_dict in
                                            context['question']['answers']}
    user.save()
    return context


def check_answer(request, user_obj) -> str:
    """
    Проверяется правильность ответа, возвращает правильный ответ или нет
    """
    history = user_obj.questions.get('history')
    last_question = history.get('question')
    question = Question.objects.prefetch_related('answers').filter(id=last_question).first()
    answers = question.answers.all()
    right_answers = answers.filter(is_right=True)
    right_answers = [r_ans.name for r_ans in right_answers]
    right_answers.sort()
    form = TestForm(request.POST)
    if form.is_valid():
        user_answers = []
        form_keys = tuple(form.cleaned_data.keys())
        for answer_number in range(len(form_keys)):
            if form.cleaned_data.get(form_keys[answer_number]):
                user_answers.append(answers[answer_number])
        user_answers.sort()
        right_answers = []
        for q in answers:
            if q.is_right:
                right_answers.append(q.name)
        right_answers.sort()
        if user_answers == right_answers:
            user_questions = user_obj.current_test
            user_questions['history']['right_answers'] += 1
            user_questions['history']['question'] = {}
            user_obj.current_test = user_questions
            user_obj.save()
            return 'Ответ верный'
        else:
            user_questions = user_obj.current_test
            user_questions['history']['wrong_answers'] += 1
            user_questions['history']['question'] = {}
            user_obj.current_test = user_questions
            user_obj.save()
            return 'Ответ неверный'


def ask_question(user_obj) -> dict or None:
    """
    Извлекает вопрос из json-поля юзера, возвращает словарь вопрос-ответы контекста или None если вопросы закончились
    """
    history = user_obj.current_test.get('history')
    question = history.get('question')
    if question:
        question = Question.objects.prefetch_related('answers').filter(id=question).first()
        context = get_question(question)
        return context
    elif not question and user_obj.questions.get('rest_questions'):
        question = user_obj.questions['rest_questions'].pop()
        user_obj.questions['history']['question'] = question
        user_obj.save()
        question = Question.objects.prefetch_related('answers').filter(id=question).first()
        context = get_question(question)
        user_obj.questions['history']['answers'] = {a_dict['num']: a_dict['answer'] for a_dict in
                                                context['question']['answers']}
        user_obj.save()
        return context
    else:
        return None


def end_test_and_show_result(user_obj) -> str:
    """
    Очищает json-поле юзера, добавляет результат в статистику пользователя, возвращает итоговый процент результата теста
    """
    history = user_obj.questions.get('history')
    right = history['right_answers']
    wrong = history['wrong_answers']
    try:
        percent = int(int(right) / (int(right) + int(wrong)) * 100)
    except ZeroDivisionError:
        percent = 0
    finally:
        result = str(percent)
        return result
