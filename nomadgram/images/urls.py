# from django.urls import path
from django.conf.urls import url
from . import views

app_name="images"
urlpatterns = [
    #path("all/",view=views.ListAllImages.as_view(),name="all_images")
    url(
        regex=r"^all/$",
        view=views.ListAllImages.as_view(),
        name="all_images"
    )
]
