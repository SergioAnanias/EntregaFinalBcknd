from django.urls import include, path


urlpatterns = [
    path('', include('api.urls')),
    path('',include('app.urls'))
]