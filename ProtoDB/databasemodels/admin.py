from django.contrib import admin

# Register your models here.

from databasemodels.models import User, Protocol, Comment



class CommentInline(admin.TabularInline):
    # TODO: make this work. currently same as tutorial
    model = Comment
    extra = 1 # should be expression for number of comments on the protocol

class ProtocolAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['title', 'description']}),
        #('Description',     {'fields': ['description']}),
        (None,              {'fields': ['publisher', 'pub_date']}),
        ('Keywords',        {'fields': ['keywords']}),
        ('Protocol',        {'fields': ['text']}),
    ]
    inlines = [CommentInline]
    list_display = ['title', 'description', 'publisher', 'pub_date'] #TODO: rating too
    search_fields = ['title'] #TODO: keywords too
    

admin.site.register(User)
admin.site.register(Protocol, ProtocolAdmin)