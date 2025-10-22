from django.urls import path
from .views import *

urlpatterns = [
    path("course-list/",course_list,name="course_list"),
    path("add-course/",add_course,name="add_course"),
    path("update-course/<int:id>/",update_course,name="update_course"),
    path("delete-course/<int:id>/",delete_course,name="delete_course")
]
