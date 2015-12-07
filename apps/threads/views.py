from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from .forms import RegistrationForm
from django.views.generic import ListView
from django.template.defaultfilters import slugify
from .models import Link, Vote, Subreddit, Comment
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView
from django.http import HttpResponse


class LinkListView(ListView):
    model = Link

    def get_context_data(self, **kwargs):
        context = super(LinkListView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            voted = Vote.objects.filter(voter=self.request.user)
            links_in_page = [link.id for link in context["object_list"]]
            voted = voted.filter(link_id__in=links_in_page) 
            voted = voted.values_list('link_id', flat=True)
            context["voted"] = voted
        return context

def logout_view(request):
    logout(request)
    return redirect('/')

def auth(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
        else:
            return redirect('/login')
    else:
        return redirect('/login')


def subreddit_view(request):
    return render(request, 'sub_list.html', {'subreddits':Subreddit.objects.all()})

def subreddit_selector(request, sub):
    slug = slugify(sub)
    subreddit = Subreddit.objects.filter(slug=slug)
    print subreddit.count()
    if subreddit.count() > 0:
        return render(request, 'subreddit.html', {'subreddit': slug,
                                                   'links': subreddit[0].links.all()
                                                   })
    else:
        if request.method == 'POST':
            Sub = Subreddit.objects.create(title=sub, slug=slug, creator=request.user)
        return render(request, 'new_sub.html', {'subreddit': slug})

def link_discuss(request, link):
    slug = slugify(link)
    links = Link.objects.filter(internal=slug)
    totals = Vote.objects.filter(voter=request.user)
    comment_votes = []
    for item in totals:
        if item.comment != None:
           comment_votes.append(item.comment.id) 
    if request.method == 'POST':
        information =  request.POST.get('button').split()
        print information
        if information[0] == 'l':
            parent = Link.objects.get(id=information[1])
            reply = Comment.objects.create(link=parent, submitter=request.user,
             description=request.POST.get('new_comment'))
            reply.save()
        elif information[0] == 'c':
            parent = Comment.objects.get(id=information[1])
            reply = Comment.objects.create(comments=parent, submitter=request.user,
             description=request.POST.get('new_comment'))
            reply.save()
        if links.count() > 0:
            return render(request, 'link.html', {'link':links[0],
                                         'comments': links[0].replies.all(),
                                         'vote_list': comment_votes
                                         })
        else:
             return redirect('#')
    else:
        if links.count() > 0:
            return render(request, 'link.html', {'link':links[0],
                                         'comments': links[0].replies.all(),
                                         'vote_list': comment_votes
                                         })
        else:
             return redirect('/')

def submit_link(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        url = request.POST.get('url')

        if url[:3] != 'http':
            url = "http://" + url
        if Link.objects.filter(url=url).exists():
            return render(request, 'threads/link_list.html', {
            'object_list': Link.objects.all(),
            'repost': True,
            })    
        else: 
            description = request.POST.get('description')
            Link.objects.create(submitter=user, internal=slugify(title), title=title, url=url, description=description)
            return render(request, 'threads/link_list.html', {
                'object_list': Link.objects.all(),
                'submit': True,
                })
    else:
        return render(request, 'submit_link.html')


def register(request):
    '''
    Request View
    '''
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegistrationForm()
    return render_to_response('register.html', {
        'form': form,
    }, context_instance=RequestContext(request))

def vote_comment(request, comment_id):
    if request.method == 'POST':
        print request.path
        if request.user.is_authenticated:
            comment = Comment.objects.get(id=comment_id)
            if Vote.objects.filter(comment_id=comment_id).exists():
                Vote.objects.filter(comment_id=comment_id).delete()
                return redirect(request.path)
            else:
                Vote.objects.create(voter=request.user, comment=comment)
                return redirect(request.path)
        else:
            return redirect('/login')
    else:
        return redirect('/')


def vote_link(request, link_id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            link = Link.objects.get(id=link_id)
            if Vote.objects.filter(link_id=link_id).exists():
                Vote.objects.filter(link_id=link_id).delete()
                return HttpResponse('Removed')
            else:
                Vote.objects.create(voter=request.user, link=link)
                return HttpResponse('Added')
        else:
            return HttpResponse('Invalid')
        
    else:
        return redirect('/')
