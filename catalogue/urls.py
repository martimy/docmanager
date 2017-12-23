from django.urls import path
from . import views
#from . import models


urlpatterns = [
    path('', views.index, name='index'),
    #path('books/', views.list, name='list'),
    path('books/', views.DocListView.as_view(paginate_by=25), name='list'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('book/<int:pk>/update', views.BookUpdate.as_view(), name='book_update'),
    #path('book/<int:pk>/update', models.BookForm, name='book_update'),
]
