from django.urls import path

from .views import add, delete, detail, edit, index

app_name = "contact"

urlpatterns = [
    path(route="", view=index, name="index"),
    path(route="<int:id>/", view=detail, name="detail"),
    path(route="add/", view=add, name="add"),
    path(route="edit/<int:id>", view=edit, name="edit"),
    path(route="delete/<int:id>", view=delete, name="delete"),
]
