  
from django.urls import path
from yokii import views
app_name="yokii"

urlpatterns = [
    path('trail/',views.trial,name="Trial"),
    path('profile/',views.profile,name="profile"),
]
