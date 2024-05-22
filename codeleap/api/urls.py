# todo/todo_api/urls.py : API urls.py
from django.urls import path
from .views import (
    ApiView,
    ApiViewObjectId
)

urlpatterns = [
    path('v1/', ApiView.as_view()),
    path('v1/<str:id>/', ApiViewObjectId.as_view()),
]