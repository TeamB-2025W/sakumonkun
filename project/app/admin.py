from django.contrib import admin
from .models import User, Test, Question, QuestionChoice, Session, Answer


admin.site.register(User)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(QuestionChoice)
admin.site.register(Session)
admin.site.register(Answer)