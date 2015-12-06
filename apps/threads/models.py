from django.db import models
from django.db.models import Count
from django.contrib.auth.models import User


class LinkVoteCountManager(models.Manager):
    def get_queryset(self):
        return super(LinkVoteCountManager, self).get_queryset().annotate(votes=Count('vote')).order_by('-votes')

class CommentVoteCountManager(models.Manager):
    def get_queryset(self):
        return super(CommentVoteCountManager, self).get_queryset().annotate(votes=Count('vote')).order_by('-votes')

class Subreddit(models.Model):
    title = models.TextField(max_length=30)
    slug = models.TextField(max_length=30, null=True)
    creator = models.ForeignKey(User, null=True)

class Link(models.Model):
    title = models.TextField("Headline", max_length=100)
    internal = models.TextField("Internal Link", max_length=100)
    submitter = models.ForeignKey(User)
    date_submitted = models.DateTimeField(auto_now_add=True)
    subreddit = models.ForeignKey(Subreddit, null=True, related_name="links")
    rank = models.FloatField(default=0.0) # Used for displaying links
    url = models.URLField("URL", max_length=100, blank=True)
    description = models.TextField("Description", blank=True)
    objects = LinkVoteCountManager()

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    submitter = models.ForeignKey(User)
    date_submitted = models.DateTimeField(auto_now_add=True)
    rank = models.FloatField(default=0.0) # Used for displaying links
    description = models.TextField("Description", blank=True)
    link = models.ForeignKey(Link, blank=True, null=True, related_name="replies")
    comments = models.ForeignKey('self', blank=True, null=True, related_name="replies")
    objects = CommentVoteCountManager()

    def __unicode__(self):
        return self.description

class Vote(models.Model):
    voter = models.ForeignKey(User)
    link = models.ForeignKey(Link, null=True, blank=True, related_name="vote")
    comment = models.ForeignKey(Comment, null=True, blank=True, related_name="vote")

    def __unicode__(self):
        return self.voter.username
