from django.urls import path
from musician.views import musicians,showmusician,editmusician,deletemusician

urlpatterns = [
    path("addmusician/",musicians, name='musician'),
    path("",showmusician, name='home'),
    path("edit/<int:id>",editmusician, name='edit'),
    path("delete/<int:id>",deletemusician, name='delete'),
]
