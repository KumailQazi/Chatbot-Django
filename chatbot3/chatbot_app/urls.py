# new url file created
from django.urls import path, include
from chatbot_app.views import chat

# from . import views

app_name = 'chatbot_app'

urlpatterns = [
    # path('', views.home, name='home'),
    path('chat/', chat, name='chat'),
    # path('chatbot_app/', include('chatbot_app.urls')),
    # other paths here
]
