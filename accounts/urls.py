from django.urls import path
# viewsモジュールをインポート
from . import views
# viewsをインポートしてauth_viewという記名で利用する
from django.contrib.auth import views as auth_views

# URLパターンを逆引きできるように名前を付ける
app_name = 'accounts'

# URLパターンを登録するための変数
urlpatterns = [
    # サインアップページのビューの呼び出し
    # 「http(s)://<ホスト名>/signup/」へのアクセスに対して、
    # viewsモジュールのSignUpViewをインスタンス化する
    path('signup/',
         views.SignUpView.as_view(),
         name='signup'),
    

    # サインアップ完了ページのビューの呼び出し
    # 「http(s)://<ホスト名>/signup_success/」へのアクセスに対して、
    # viewsモジュールのSignUpSuccessViewをインスタンス化する
    path('signup_success/',
         views.SignUpSuccessView.as_view(),
         name='signup_success'),
    
    # ログインページの表示
    # 「http(s)://<ホスト名>/signup/」へのアクセスに対して、
    # django.contrib.auth.views.LoginViewをインスタンス化して
    # ログインページを表示する
    path('login/',
         # ログイン用のテンプレート(フォーム)をレンダリング
         auth_views.LoginView.as_view(template_name='login.html'),
         name='login'
         ),
    
    # ログアウトを実行
    # 「http(s)://<ホスト名>/logout/」へのアクセスに対して、
    # django.contrib.auth.views.logoutViewをインスタンス化して
    # ログアウトさせる
    path('logout/',
         auth_views.LogoutView.as_view(template_name='logout.html'),
         name='logout'
         ),
 # urls.py

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

        
]