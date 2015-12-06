from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from .forms import RegistrationForm
from django.views.generic import ListView
from django.template.defaultfilters import slugify
from .models import Link, Vote, Subreddit, Comment
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect, render

class LinkListView(ListView):
    model = Link


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
                                         'comments': links[0].replies.all()
                                         })
        else:
             return redirect('#')
    else:
        if links.count() > 0:
            return render(request, 'link.html', {'link':links[0],
                                         'comments': links[0].replies.all()
                                         })
        else:
             return redirect('/')

def submit_link(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        url = request.POST.get('url')
        description = request.POST.get('description')
        Link.objects.create(submitter=user, internal=slugify(title), title=title, url=url, description=description)
        return render(request, 'threads/link_list.html', {
            'object_list': Link.objects.all(),
            'submit': True
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
