# urls.py
from django.contrib import admin
from django.urls import path

from auth_app.views import LoginView, ProtectedView, RegisterView
from mcqs.views import MCQListCreateView, MCQRetrieveUpdateDestroyView
from game.views import create_game, list_games,join_game

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register", RegisterView.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),
    path("protected", ProtectedView.as_view(), name="protected"),
    path("mcqs", MCQListCreateView.as_view(), name="mcq-list-create"),
    path("mcqs/<uuid:pk>", MCQRetrieveUpdateDestroyView.as_view(), name="mcq-detail"),
    #
    path('game/create-game/', create_game, name='create-game'),
    path('game/list-games/', list_games, name='list-games'),
    path('game/join-game/', join_game, name='join-game'),
]
