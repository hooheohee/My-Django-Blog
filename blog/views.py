from django.shortcuts import render
# from django.http import HttpResponse

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog post 1',
        'content': 'First blog content',
        'date_posted': 'August 10, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog post 2',
        'content': 'Second blog content',
        'date_posted': 'August 20, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
