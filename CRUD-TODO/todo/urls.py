from django.urls import path
from . import views

urlpatterns = [
    # 런서버하고 todo/ 붙이면 views에 있는 todo_list 함수가 실행된다는 뜻 
    # (mytodo의 urls.py에서 todo/로 연결시켜 놓았으므로)
    path('', views.todo_list, name='todo_list')
]