from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<title>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("history", views.history, name="history"),
    path("saveEntry", views.saveEntry, name="saveEntry"),
    path("editEntry/<title>", views.editEntry, name="editEntry")
]
