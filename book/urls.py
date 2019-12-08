from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from book.views import BookAPIView, BookCreateAPIView, BookUpdateDeleteAPIView

urlpatterns = [
    path('', BookAPIView.as_view(), name='book-list'),
    path('book/create/', BookCreateAPIView.as_view(), name='book-create'),
    path('book/update/<int:id>/', BookUpdateDeleteAPIView.as_view(), name='book-delete')
]

