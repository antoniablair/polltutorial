from django.contrib import admin
from polls.models import Choice, Question

# Register your models here.
# To register a new related object do: 
# admin.site.register(Question)

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):

	fieldsets = [
		(None,				{'fields': ['question_text']}),
		('Date information',{'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]

	# Adds a Filter Sidebar to filter by the publication date instead of default
	list_filter = ['pub_date']

	#Add a search field to the top of the page. Hollaaaa
	search_fields = ['question_text']

	# Fields that will show up in the cms by Questions
	list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Question, QuestionAdmin)