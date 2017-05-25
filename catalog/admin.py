# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# admin.site.register(Book)
# #admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(BookInstance)
# admin.site.register(Language)

# Define the admin class
class BooksInline(admin.TabularInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline] 


class GenreAdmin(admin.ModelAdmin):
    pass

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]    

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    #Slist_display = ('id','status', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
#admin.site.register(Book, BookAdmin)
#admin.site.register(BookInstance, BookInstanceAdmin)
#admin.site.register(Language, LanguageAdmin)
