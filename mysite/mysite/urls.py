"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path  # 这里引入include()方法
from django.conf import settings
from django.conf.urls.static import static
from utils.upload import upload_file   # 富文本编辑器上传图片方法

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('users/', include('users.urls')),
    # path('', include('blog.urls')),

    # path('uploads/', upload_file, name='uploads')   # 上传图片url

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # 配置静态文件url


# 配置用户上传文件url
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# admin.site.site_header = "Management back office"
# admin.site.index_title = "Management back office"
# admin.site.site_title = "The administrator is logged in."