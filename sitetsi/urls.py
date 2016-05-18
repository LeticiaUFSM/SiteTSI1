"""sitetsi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^noticias/$','noticias.views.index', name='noticias'),
    url(r'^noticias/(?P<id>[0-9]+)/$','noticias.views.lernoticia', name='lernoticia'),
    url(r'^noticias/media/(.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    url(r'^forum/$','forum.views.index', name='forum'),
    url(r'^forum/(?P<id>[0-9]+)/$','forum.views.lermensagens', name='lermensagens'),
    url(r'^forum/escrevermensagem/(?P<id>[0-9]+)/$','forum.views.escrevermensagem', name='escrevermensagem'),
    url(r'^forum/editarmensagem/(?P<id>[0-9]+)/(?P<msg_id>[0-9]+)/$','forum.views.escrevermensagem', name='editarmensagem'),
]
