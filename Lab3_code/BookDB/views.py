from django.http import HttpResponse
from django.shortcuts import render_to_response
from BookDB.models import Author,Book

def bookdb_hello(request):
    return render_to_response('bookdb_hello.html')

def bookdb_begin(request):
    return render_to_response('bookdb_begin.html')

def author_test(request):
    list_all = Author.objects.all()
    return render_to_response('author_list.html', locals())

def search_author(request):
    error = False
    Author_all_list = Author.objects.all()
    if 'author' in request.GET:
        q_author = request.GET['author']
        query = q_author
        if not q_author:
            error = True
        else:            
            Author_find = Author.objects.filter(Name = q_author)
            Book_all = Book.objects.filter(AuthorID = Author_find)
            return render_to_response('author_list.html', locals())
    elif 'delete' in request.GET:
        book_delete = request.GET['delete']
        Author_find = Book.objects.filter(Title = book_delete)[0].AuthorID#!!!
        Book_all = Book.objects.filter(AuthorID = Author_find)
        query = Book_all[0].AuthorID.Name
        Book.objects.filter(Title = book_delete).delete()
        return render_to_response('author_list.html', locals())
    return render_to_response('search_author.html', locals())

def search_author_book(request,offset):
    book_request = Book.objects.filter(Title = offset)
    try:
        author_find = book_request[0].AuthorID#!!!
    except IndexError:
        return HttpResponse("Error ~ ~ ~ Sorry")
    return render_to_response('book_list.html',locals())

def add_book(request):
    errors = []
    add_check = False
    author_add = False
    if request.POST:
        post = request.POST
        if Book.objects.filter(ISBN = post['ISBN']):
            errors.append('This ISBN has been in BookDB !')
        elif Book.objects.filter(Title = post['Title']):
            errors.append('This Book has been in BookDB !')
        else:
            try:
                author = Author.objects.filter(AuthorID = post['AuthorID'])
                Book.objects.create(
                    ISBN = post['ISBN'],
                    Title = post['Title'],
                    AuthorID = author[0],
                    Publisher = post['Publisher'],
                    PublishDate = post['PublishDate'],
                    Price = post['Price']
                )
                add_check = True
            except IndexError:
                errors.append('Do not find the author!' )
                author_add = True
            except :
                errors.append('Please input by the correct way ! ')
                errors.append('Make sure input all things')
    return render_to_response('add_book.html',locals())

def add_author(request):
    errors = []
    add_check = False
    if request.POST:
        post = request.POST
        if Author.objects.filter(AuthorID=post['AuthorID']):
            errors.append('This AuthorID has been used !')
        elif Author.objects.filter(Name=post['Name']):
            errors.append('This author has been in the Author_list !')
        elif post['AuthorID']!='' and post['Name']!='' and post['Age']!='' and post['Country']!='': 
            try:
                Author.objects.create(
                    AuthorID = post['AuthorID'],
                    Name = post['Name'],
                    Age = post['Age'],
                    Country = post['Country']
                )
                add_check = True
            except:
                errors.append('Please input by the correct way ! ')
        else :
            errors.append('Make sure input all things !')
    return render_to_response('add_author.html',locals())

def update_book(request,offset):
    errors = []
    update_check = False
    author_update = False
    update_book = Book.objects.get(Title = offset)
    if request.POST:
        try:
            post = request.POST
            author = Author.objects.filter(AuthorID = post['AuthorID'])
            Book.objects.filter(Title = offset).update(
                AuthorID = author[0],
                Publisher = post['Publisher'],
                PublishDate = post['PublishDate'],
                Price = post['Price']
            )
            update_check = True
        except IndexError:
            errors.append('Do not find the author!' )
            author_update = True
        except :
            errors.append('Please input by the correct way ! ')
            errors.append('Make sure input all things')
        
    return render_to_response('update_book.html',locals())
# Create your views here.
#test for Lab4
