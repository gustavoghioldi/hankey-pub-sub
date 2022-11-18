from django.urls import path
from publisher.views import PublisherListview,RetrieveUpdateDestroy


urlpatterns = [ 
    path("publisher/", PublisherListview.as_view()),
    path("publisher/<pk>", RetrieveUpdateDestroy.as_view()),
]
