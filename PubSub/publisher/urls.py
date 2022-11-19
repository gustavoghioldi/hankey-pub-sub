from django.urls import path
from publisher.views import (
    PublisherListview,
    RetrieveUpdateDestroy, 
    MessageListCreateview,
    MessageRetrieve
    )

urlpatterns = [ 
    path("", PublisherListview.as_view()),
    path("<pk>", RetrieveUpdateDestroy.as_view()),
    path("message/", MessageListCreateview.as_view()),
    path("message/<pk>", MessageRetrieve.as_view()),
]
