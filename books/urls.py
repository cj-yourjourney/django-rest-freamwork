from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet


## ✅ Using ViewSet (Short & Clean)
router = DefaultRouter()
router.register(r"books", BookViewSet)


## /api/books/ GET POST
## /api/books/id/ GET PUT PATCH DELETE 

urlpatterns = [
    path("", include(router.urls)),
]


## ❌ Without ViewSet (More Code) ✅ Better for full control

# from django.urls import path
# from .views import BookListCreate, BookDetail

# urlpatterns = [
#     path("books/", BookListCreate.as_view()),
#     path("books/<int:pk>/", BookDetail.as_view()),
# ]
