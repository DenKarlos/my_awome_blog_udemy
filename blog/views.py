from django.shortcuts import render


def showblog(request):
    context = {
        'title': 'BLOG',
    }
    return render(request, 'blog/index.html', context)
