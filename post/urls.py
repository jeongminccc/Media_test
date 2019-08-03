from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'post'
urlpatterns = [
    path('', views.post, name='post'),
    path('post_detail/<int:post_id>/',views.post_detail, name='post_detail'),
    path('upload/',views.upload,name="upload"),
    path('<int:post_id>/post_delete/',views.post_delete, name="post_delete"),
    path('<int:post_id>/post_modify/',views.post_modify, name="post_modify"),
    # path('<int:post_id>/comment/', views.comment_upload, name='comment_upload'),
    path('<int:post_id>/result_upload/', views.result_upload, name="result_upload"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
