from django.urls import path
from .views import two,rectangle


urlpatterns = [
    path('<int:one>',two),
    path('<int:one>/<int:two>/',rectangle),

]




