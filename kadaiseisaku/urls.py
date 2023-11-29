from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kadaiapp.urls', namespace='kadaiapp')),
    path('', include('accounts.urls', namespace='accounts')),
    # 他のパスや名前空間があればここに追加
]
