from django.shortcuts import render_to_response
from models import Book

# Create your views here.
def index(request):
	all_books = Book.objects.all()
	book_data = {'books' : all_books} 

	return render_to_response('recommend_all/all.html', book_data)
