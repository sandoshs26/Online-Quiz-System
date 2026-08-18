from django.urls import path
from .import views

urlpatterns = [
    path("admin-dashboard",views.admin_dashboard,name="admin_dashboard"),
    path("teacher-dashboard",views.teacher_dashboard,name="teacher_dashboard"),
    path("student-dashboard",views.student_dashboard,name="student_dashboard"),
    path("teacher/create-quiz/",views.create_quiz,name="create_quiz"),
    path("teacher/edit-quiz/<int:quiz_id>/",views.edit_quiz,name="edit_quiz"),
    path("teacher/delete-quiz/<int:quiz_id>/",views.delete_quiz,name="delete_quiz"),
    path("teacher/add-question/<int:quiz_id>/",views.add_question,name="add_question"),
    path("teacher/view-question/<int:quiz_id>/",views.view_questions,name="view_questions"),
    path("teacher/edit-question/<int:question_id>",views.edit_question,name="edit_question"),
    path("teacher/delete-question/<int:question_id>",views.delete_question,name="delete_question"),
    path("teacher-results/",views.teacher_results,name="teacher_results"),
    path("manage-users/",views.manage_users,name="manage_users"),
    path("leaderboard/",views.leaderboard,name="leaderboard"),
]

