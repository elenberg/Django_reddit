from django.contrib import admin
from .models import Link, Vote, Comment

class LinkAdmin(admin.ModelAdmin):
    pass
admin.site.register(Link, LinkAdmin)

class VoteAdmin(admin.ModelAdmin):
    pass
admin.site.register(Vote, VoteAdmin)


class CommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Comment, CommentAdmin)