from django.shortcuts import render


menu
def index(request):
    return render(request, 'tour/content/index.html')

def about(request):
    return render(request, 'tour/content/about.html')

def bad_request(request, exception=None):
    return render(request,'tour/content/error400.html')
def permission_denied(request, exception=None):
    return render(request,'tour/content/error403.html', {})
def page_not_found(request,exception):
    return render(request, 'tour/content/error404.html', {})
def server_error(request,exception=None):
    return render(request,'tour/content/error500.html',{})
def login(request):
    pass
def addservice(request):
    pass
def contact(request):
    pass
def show_service(request):
    return render(request, 'tour/content/show.html',)
