from django.urls import include, path
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("profiles", views.UserProfileViewSet)


urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path("", include(router.urls)),
    ]
