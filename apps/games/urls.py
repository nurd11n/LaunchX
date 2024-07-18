from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.games.views import (SubmitApiView, GameApiView,
                             GameApplicationApiView, GameCardApiView,
                             GameRecommendationsApiView, GameSearchView,
                             GameTagsApiView, PriceRangeApiView)

router = DefaultRouter()
router.register('Game_card', GameCardApiView, basename='game-card')
router.register('Game', GameApiView, basename='games')
router.register('submit-games', SubmitApiView, basename='submit-games')
router.register('game-recommendation', GameRecommendationsApiView, basename='game-recommendation')
router.register('game-tags', GameTagsApiView, basename='game-tags')
router.register('game-application', GameApplicationApiView, basename='game-application')

urlpatterns = [
    path('', include(router.urls)),
    path('search/', GameSearchView.as_view(), name='game-search'),
    path('price-range/', PriceRangeApiView.as_view(), name='price-range'),
]

urlpatterns = router.urls + urlpatterns
