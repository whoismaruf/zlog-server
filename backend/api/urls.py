from django.urls import include, path


urlpatterns = [
    path('blog/', include('blog.urls'), name='blog'),
    path('user/', include('user.urls'), name='user'),
    path('api_auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
