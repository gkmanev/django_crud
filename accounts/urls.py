from rest_framework.routers import DefaultRouter
from accounts import views
from django.urls import path

app_name = 'accounts'
router = DefaultRouter()

router.register(r'clients', views.ClientViewset, basename='friends')

urlpatterns = [
    path('upload/', views.UploadFileView.as_view(), name='upload-file'),
]

urlpatterns += router.urls
