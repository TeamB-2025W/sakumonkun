from django.contrib import admin
from .models import User, Test, Question, QuestionChoice, Examination, Answer


admin.site.register(User)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(QuestionChoice)
admin.site.register(Examination)
admin.site.register(Answer)