from django.urls import path
from publisher.views import PublisherListview,RetrieveUpdateDestroy,PublisherCreate


urlpatterns = [ 
    path("publishercreate/", PublisherCreate.as_view()),
    path("publisherlist/", PublisherListview.as_view()),
    path("publisher/<pk>", RetrieveUpdateDestroy.as_view()),
]
