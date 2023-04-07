# new url file created
from django.urls import path, include
from chatbot_app.views import chat, chatbot, chat2, chat3

# from . import views

app_name = 'chatbot_app'

urlpatterns = [
    # path('', views.home, name='home'),
    path('chat/', chat, name='chat'),
    path('chatbot/', chatbot, name='chatbot'),
    path('chat2/', chat2, name='chat2'),
    path('chat3/', chat3, name='chat3'),
    # path('chatbot_app/', include('chatbot_app.urls')),
    # other paths here
]
