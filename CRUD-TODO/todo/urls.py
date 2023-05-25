from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'), # 런서버하고 todo/ 붙이면 views에 있는 todo_list 함수가 실행된다는 뜻 (mytodo의 urls.py에서 todo/로 연결시켜 놓았으므로)
    path('<int:pk>/', views.todo_detail, name='todo_detail'), # url을 /pk/로 설정하여 사용자가 선택한(id=pk) 해당 Todo를 연결하도록 함
    path('post/', views.todo_post, name='todo_post'), # 생성 url은 post/로 지정
    path('<int:pk>/edit/', views.todo_edit, name='todo_edit'), # 수정 url은 /edit/로 지정
    path('done/', views.done_list, name='done_list'),
    path('done/<int:pk>/', views.todo_done, name='todo_done'),
]