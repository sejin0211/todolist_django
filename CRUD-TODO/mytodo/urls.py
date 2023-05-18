from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 관리자계정
    path('admin/', admin.site.urls),

    path('todo/', include('todo.urls'))
]
