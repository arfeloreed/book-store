from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg
# from django.http import Http404


# Create your views here.
# view page for the home page
def index(request):
    books = Book.objects.all().order_by("-rating")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    return render(
        request,
        "book_outlet/index.html",
        {
            "books": books,
            "total_books": num_books,
            "avg_rating": avg_rating,
        }
    )


# view page for the book info
def book_info(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    # else:
    #     return render(
    # request,
    # "book_outlet/book_info.html",
    # {
    #     "title": book.title,
    #     "author": book.author,
    #     "rating": book.rating,
    #     "is_bestseller": book.is_bestseller,
    # }
    #     )
    book = get_object_or_404(Book, slug=slug)
    return render(
        request,
        "book_outlet/book_info.html",
        {
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
            "is_bestseller": book.is_bestseller,
        }
    )
