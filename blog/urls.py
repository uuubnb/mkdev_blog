from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.flatpages import views
from posts.views import (index, PostListView, PostDetailView, search, post_create, post_update, post_delete)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', PostListView.as_view(), name='post-list'),
    path('search/', search, name='search'),
    path('create/', post_create, name='post-create'),
    # path('post/<id>/', post, name='post-detail'),
    path('post/<pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<pk>/update/', post_update, name='post-update'),
    path('post/<pk>/delete/', post_delete, name='post-delete'),
    path('tinymce/', include('tinymce.urls')),
    
    path('pages/', include('django.contrib.flatpages.urls')),
    # path('<path:url>', views.flatpage),
    # path('about/', views.flatpage, {'url': '/about/'}, name='about'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)