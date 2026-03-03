from django.urls import path
from .views import HomeView, InstrucoesView, NotificationSetReadView, NotificationListView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('primeiros-passos/', InstrucoesView.as_view(), name='tela_de_instrucoes'),
    path('notification/set-read/', NotificationSetReadView.as_view(), name='notification_set_read'),
    path("notification/all/", NotificationListView.as_view(), name="notifications_list"),
]