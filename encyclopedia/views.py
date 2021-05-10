from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import util
import markdown

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

edit_title = ""
edit_content = ""

def entry_view(request,slug):
    global edit_title,edit_content
    slug_file = util.get_entry(slug)
    edit_title = slug
    edit_content = slug_file
    if slug_file==None:

        return HttpResponse('There is no such article')
    
    return render(request,'encyclopedia/entrypage.html',{'content':markdown.markdown(slug_file)})

def search(request):
    ad = request.POST['q']
    list_of_entries = [i.lower() for i in util.list_entries()]
    if ad in list_of_entries:
        return redirect('encyclopedia:entry_view',ad)
    else:
        similarities = [i for i in list_of_entries if ad in i]

        return render(request,'encyclopedia/doesntexist.html',{'similarities':similarities})

def random_page(request):
    import random
    list_of_entries = [i.lower() for i in util.list_entries()]
    page = random.choice(list_of_entries)
    return redirect('encyclopedia:entry_view',page)


def create_entry(request):
    if request.method=='POST':
        title = request.POST['title']
        area = request.POST['area']
        if title and area:
            title = title.split()
            title = "".join(title).lower()
            if util.get_entry(title)==None:
                util.save_entry(title,area)
            else:
                return HttpResponse("there is already a page named {}".format(title))
    return render(request,'encyclopedia/create.html')


def edit_entry(request):
    global edit_title,edit_content
    if request.method=='POST':
        title = request.POST['title']
        area = request.POST['area']
        if title and area:
            title = title.split()
            title = "".join(title).lower()
            util.save_entry(title,area)
            
    
    return render(request,'encyclopedia/edit.html',{'title':edit_title,'content':edit_content})
