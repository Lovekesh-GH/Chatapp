from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('<str:room>/',views.room,name= 'room'),
    path('checkview',views.checkview,name='checkview'),
    path('send',views.send,name='send'),
    path('getMessages/<str:room>/',views.getMessages,name='getMessages'),
    path(
        "manifest.json",
        TemplateView.as_view(
            template_name="pwa/manifest.json", content_type="text/plain"
        ),
        name='manifest',
    ),
    path(
        "serviceworker.js",
        TemplateView.as_view(
            template_name="pwa/serviceworker.js", content_type="text/javascript"
        ),
        name='serviceworker',
    ),
]