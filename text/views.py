from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from user.models import User
from .models import Text


def cheak_login(func):
    def wapper(request, *args, **kwargs):
        if 'username' not in request.session or 'uid' not in request.session:
            c_username = request.COOKIES.get('username')
            c_id = request.COOKIES.get('uid')
            if not c_username or not c_id:
                return HttpResponseRedirect('/index')
            else:
                request.session['username'] = c_username
                request.session['uid'] = c_id
        return func(request, *args, **kwargs)

    return wapper


# Create your views here.

@cheak_login
def text(request):
    c_username = request.session.get('username')
    user = User.objects.get(username=c_username)
    texts = user.text_set.filter(is_active=True)
    return render(request, 'text/text.html', locals())


@cheak_login
def up(request):
    if request.method == 'GET':
        return render(request, 'text/up.html')
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        username = request.session.get('username')
        try:
            user_id = User.objects.get(username=username).id
        except:
            pass
        Text.objects.create(title=title, content=content,
                            user_id=user_id)
        return HttpResponseRedirect('/text')


def delete(request):
    del_id = request.GET.get('text_id')
    text1 = Text.objects.get(id=del_id, is_active=True)
    text1.is_active = False
    text1.save()
    return HttpResponseRedirect('/text')


def change(request):
    if request.method == 'GET':
        try:
            c_id = request.GET.get('text_id')
            text = Text.objects.get(id=c_id)
            return render(request, 'text/change.html', locals())
        except:
            return HttpResponse('error')

    if request.method == 'POST':
        c_id = request.GET.get('text_id')
        text = Text.objects.get(id=c_id)
        text.title = request.POST.get('title')
        text.content = request.POST.get('content')
        text.save()
        return HttpResponseRedirect('/text')
