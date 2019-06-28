import os
import django
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ask.settings")
django.setup()


from qa.models import Question, Answer

for i in range(1,50):
    q = Question()
    q.title = 'Вопрос #' + str(i)
    q.text = 'Это текст вопроса #' + str(i)
    q.rating = random.randint(0, 100)
    q.save()
    for j in range(1,5):
        a = Answer()
        a.question = q
        a.text = 'Это текст ответа #' + str(j) + ' на вопрос #' + str(i)
        a.save()

print(Question.objects.all())
