from django.shortcuts import render
def index(request):
    return render(request, 'search/index.html',)
def resp(request):
    keywd=request.POST.get('search',False)
    return render(request,'search/resp.html',{'keywd':keywd})
