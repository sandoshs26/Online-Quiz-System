from django.urls import path
from .import views

urlpatterns = [
    path("",views.quiz_list,name="quiz_list"),
    path("<int:quiz_id>/",views.quiz_detail,name="quiz_detail"),
    path("results/",views.result_history,name="result_history"),
]

