from django.contrib import admin

from django_testing.polls.models import Poll
from django_testing.polls.models import Choice

#admin.site.register(Poll)
#admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_today', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('poll', 'choice', 'votes')
    list_filter = ['poll']
    search_fields = ['choice']

admin.site.register(Choice, ChoiceAdmin)