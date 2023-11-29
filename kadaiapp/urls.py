from django.urls import path,include
from . import views
from django.contrib import admin
from .views import CreatePost
from .views import  BlogPostSuccessView
from .views import post_detail


# URLconfのURLパターンを逆引きできるようにアプリ名を登録
app_name = 'kadaiapp'

# URLパターンを登録するためのリスト
urlpatterns = [
    # http(s)://ホスト名/以下のパスが''(無し)の場合
    # viewsモジュールのIndexVieを実行
    # URLパターン名は'index'
    path('', views.IndexView.as_view(), name='index'),

    path(
        'blog-detail/<int:pk>/',
        views.BlogDetail.as_view(),
        name = 'blog_detail'
    ),

    path('post/', views.CreatePost.as_view(), name='post'), 

    path('post_suc/', views.BlogPostSuccessView.as_view(), name='post_suc'),

    
    path(
        'G1-list/',
        views.G1View.as_view(),
        name = 'G1_list'
    ),

    path(
        'G2-list/',
        views.G2View.as_view(),
        name = 'G2_list'
    ),

    path(
        'G3-list/',
        views.G3View.as_view(),
        name = 'G3_list'
    ),

      path(
        'user-list/',
        views.UserView.as_view(),
        name = 'user_list'
    ),

    path('mypage/', views.MypageView.as_view(), name = 'mypage'),


    path(
        'contact/',
        views.ContactView.as_view(),
        name = 'contact'
    ),


    
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('post_detail/<int:pk>/', post_detail, name='post_detail'),
    # 他のURLパターン    
]





