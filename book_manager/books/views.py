from django.shortcuts import render
from .models import BookInfo
from .forms import BookForm
# Create your views here.
def add_book(request):
    if request.POST:
        frm = BookForm(request.POST,request.FILES)
        if frm.is_valid:      
            frm.save()
            frm = BookForm()   # this deletes the user input in the form fields after succesful submission
    else:                                 # if the request is GET, an empty form should be rendered.
        frm = BookForm()
    return render(request,'addbook.html',{'frm':frm})
def display_books(request):
    recent_visited = request.session.get('recent_visits',[])
    recent_movie_set = BookInfo.objects.filter(pk__in = recent_visited)
    all_books = BookInfo.objects.all() #all_books is a QuerySet- analogous to SELECT statement in SQL
    all_books_2019 = all_books.filter(title = 'new book',year = 2019) #using filter on QuerySet to filter out books in 2019, analogous to WHERE statement in SQL
    # filter, exclude, orderby, field lookups : year__gt, year__lt etc
    return render(request, 'display.html', {'books':all_books, 'recent_visited':recent_movie_set})  # new query set can be passed to render
def edit(request, pk):
    instance_edit = BookInfo.objects.get(pk = pk)
    if request.POST:
        frm = BookForm(request.POST, request.FILES, instance=instance_edit)
        if frm.is_valid:
            frm.save()
        frm = BookForm()
    else:
        recents = request.session.get('recent_visits',[])
        recents.insert(0,pk)
        request.session['recent_visits'] = recents
        frm = BookForm(instance = instance_edit)
    return render(request,'edit.html',{'frm':frm})

def homepage(request):
    return render(request, 'homepage.html')
def delete(request, pk):
    instance_delete = BookInfo.objects.get(pk = pk)
    instance_delete.delete()
    all_books = BookInfo.objects.all()
    return render(request, 'display.html', {'books':all_books})
