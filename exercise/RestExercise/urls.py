from django.urls import path, include
from rest_framework.routers import DefaultRouter
from RestExercise import views
from rest_framework_extensions.routers import NestedRouterMixin


class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedDefaultRouter()
category_router = router.register(r'category', views.CategoryViewSet)
category_router.register(r'items', views.ItemsViewSet,
                basename='category_items',
                parents_query_lookups=['category']
                )

urlpatterns = [
    path('', include(router.urls)),

]
