from django.contrib import admin
from quizzes.models import Exam, Question, Options

class OptionsInline(admin.TabularInline):
    model= Options
    extra= 3

class QuestionInline(admin.TabularInline):
    model= Question
    extra= 2

class ExamAdmin(admin.ModelAdmin):
    fieldsets = [
	('Exam Information', {'fields': ['description', 'deadline']}), 
	('Result', {'fields': ['score'], 'classes': ['collapse']})
    ]
    inlines=[QuestionInline]
    search_fields= ['description']
    list_filter= ['deadline']
    list_display = ('description', 'deadline', 'valid_date','id',)

class QuestionAdmin(admin.ModelAdmin):
    fields = [ 'text' ]
    inlines=[OptionsInline]
    search_fields= ['text']
    list_filter=['exam']
    list_display = ('text', 'exam',)


admin.site.register(Exam, ExamAdmin)
admin.site.register(Question, QuestionAdmin)
