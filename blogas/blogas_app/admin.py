from django.contrib import admin
from . import models


class CommentInline(admin.StackedInline):
    model = models.Comment
    can_delete = True
    extra = 0


class PostInline(admin.StackedInline):
    model = models.Post
    can_delete = True
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "display_posts", "display_comments")
    list_display_links = ("first_name", "last_name") # sukurs linkus stulpeliams
    search_fields = ("first_name", "last_name")
    inlines = (CommentInline, PostInline)


class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "display_post", "display_date")
    list_filter = ("author","date")
    search_fields = ("author",)
    search_fields = ("author__first_name", "author__last_name")
    inlines = (CommentInline,)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "display_comment", "display_date") # sukurs stulpelius
    list_filter = ("author", ) # filtravimas


# Register your models here.
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment, CommentAdmin)
