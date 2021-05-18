from django.urls import path

from .views import index, createEntry, deleteEntry

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('new/', createEntry.as_view(), name='create'),
    path('<int:pk>/delete/', deleteEntry.as_view(), name='delete')
]
