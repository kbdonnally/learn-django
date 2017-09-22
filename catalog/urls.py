# catalog/urls.py

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^books/$', views.BookListView.as_view(), name='books'),
	url(r'^books/(?P<slug>[-\w]+)$', views.BookDetailView.as_view(), name='book-detail'), # pk -> slug; d+ -> [-\w]+
	url(r'^authors/$', views.AuthorListView.as_view(), name='authors')
]
