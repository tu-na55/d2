"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

# add include
from django.urls import path, include

# 今回は使う
from django.conf.urls import url

# from django.urls import path, include, re_path
# re_path(r'admin/', admin.site.urls),

####################
# => core.urlsで宣言するので不要？
# DefaultRouter
from core.urls import router

####################
# debug用
# MEDIA_URL, MEDIA_ROOT
from django.conf import settings
from django.conf.urls.static import static

####################
# swagger
from rest_framework import permissions, authentication
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# use _jwt
from rest_framework_jwt.views import obtain_jwt_token
####################


# schema_view = get_swagger_view(title="API Lists")
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="ver.1.0",
        description="Test description",
        # terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="contact@snippets.local"),
        # license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
    authentication_classes=(authentication.SessionAuthentication,),
)
####################
# admin/
# api/
# ^swagger/$ [name='schema-swagger-ui']
# api-auth/
# ^media/(?P<path>.*)$
####################
urlpatterns = [
    # url(r'^.+/$', views.path, name="path")
    # パス指定なしでルートディレクトリにアクセスした時のルート
    # url(r"^$", views.hoge),
    # 「何も入力がない1」が入力されたら「マッチした」という状態に遷移するオートマトン」
    # url(r"", include(fuga)),
    ####################
    path("admin/", admin.site.urls),
    ####################
    # core.url => index
    # http://127.0.0.1:8000/hello/
    # http://127.0.0.1:8000/
    # path("index/", include("core.urls")),
    # path("api/", include("core.urls")),
    path("api/", include("router.urls")),
    ####################
    # JWT認証
    # 01 use _jwt
    path("api/auth/", obtain_jwt_token),
    # 02 use: simple_jwt & djoser
    # api/authアプリケーションのURLconf読み込み
    # path("api/auth/", include("djoser.urls.jwt")),
    ####################
    # swagger
    # import old module
    # path("swagger/", schema_view),
    url(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]

# このルートで既存の読み取り・更新・削除が実行可能
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
