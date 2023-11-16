from django.http import HttpResponse

def main(request):
    return HttpResponse('Hello, i am your main page in this site!')

def about(reguest):
    return HttpResponse('It is a page that consist a main information about function of Django')\

def profile(reguest, username):
    return HttpResponse(f'Hey, {username}, it is your own page on the site')


def article(request, article):
    return HttpResponse(f'Presentation of parts of one article. Article consist dinamic part: {article}')

def article_comment(reguest, article):
    return HttpResponse(f'Here you can add your comment. Article consist dinamic part: {article}')    

def article_update(request, article):
    return HttpResponse(f'Here you can update article on the site. Article consist dinamic part: {article}')    

def article_delete(request, article_update):
    return HttpResponse(f'Here you can delete article on the site. Article consist dinamic part: {article}')


def topics(request):
    return HttpResponse('List of available themes on the site')

def topics_subscribe(request, topic):
    return HttpResponse(f'views for subscribing to a topic. Your topic: {topic}')

def topics_unsubscribe(request, topic):
    return HttpResponse(f'views for unsubscribing to a topic. Your topic: {topic}')


def set_password(request):
    return HttpResponse('Change your personal accounting data')

def set_userdata(request):
    return HttpResponse('Change your personal data')

def deactivate(request):
    return HttpResponse('Deactivate your personal data')

def register(request):
    return HttpResponse('Page for registration')

def login(request):
    return HttpResponse('Page for login')

def logout(request):
    return HttpResponse('Page for logout')