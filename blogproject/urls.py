"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('blogapp.urls')),
    path("",RedirectView.as_view(url="/blog/",permanent=True)),     #만약 아무것도 없이 진입했을때 blog/를 타고 들어오게하는 코드
]
#static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)    
#->js,css,이미지파일 등 정적파일들을 처리하는 코드
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)    
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)    
