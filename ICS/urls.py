from django.urls import path
from ICS import views

urlpatterns = [
  path('v1/web/',views.ICSdualWeb.as_view(),),
  path('v1/desk/',views.ICSdualDesk.as_view(),),
]