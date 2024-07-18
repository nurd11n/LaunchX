from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Min, Max
from drf_spectacular.utils import extend_schema
from apps.games.models.submit_games_models import SubmitGame
from apps.games.models.games import Game, GameApplication, Tags
from .filter import GameFilter
from .pagination import Game_Pagination
from .serializers import *


@extend_schema(tags=['Game'])
class GameApiView(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = GameFilter
    pagination_class = Game_Pagination

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.status_code = status.HTTP_201_CREATED
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.status_code = status.HTTP_200_OK
        return response

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


@extend_schema(tags=['Game Card'])
class GameCardApiView(viewsets.GenericViewSet,
                      mixins.ListModelMixin):
    queryset = Game.objects.all()
    serializer_class = GameCardSerializer


@extend_schema(tags=['Favorite Game'])
class SubmitApiView(viewsets.GenericViewSet,
                          mixins.ListModelMixin):
    serializer_class = SubmitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SubmitGame.objects.filter(user=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def submit(self, request, pk=None):
        game = Game.objects.get(pk=pk)
        submit, created = SubmitGame.submit(request.user, game)
        if created:
            return Response({'status': 'added'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'already exists'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def remove_submit(self, request, pk=None):
        game = Game.objects.get(pk=pk)
        SubmitGame.remove_submit(request.user, game)
        return Response({'status': 'removed'}, status=status.HTTP_204_NO_CONTENT)


@extend_schema(tags=['Game Tags'])
class GameTagsApiView(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = Game.objects.all()
    serializer_class = TagSerializer


    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.status_code = status.HTTP_201_CREATED
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response.status_code = status.HTTP_200_OK
        return response

    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema(tags=['Game Recomendation'])
class GameRecommendationsApiView(viewsets.GenericViewSet,
                          mixins.ListModelMixin,
                          mixins.RetrieveModelMixin):
    serializer_class = GameSerializer
    pagination_class = Game_Pagination

    def get_queryset(self):
        queryset = Game.objects.order_by('-views')
        return queryset


@extend_schema(tags=['Game Application'])
class GameApplicationApiView(viewsets.GenericViewSet,
                             mixins.ListModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.CreateModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin):
    queryset = GameApplication.objects.all()
    serializer_class = GameApplicationSerializers


@extend_schema(tags=['Game Search'])
class GameSearchView(APIView):
    def get(self, request):
        query = request.GET.get('q')
        if query:
            games = Game.objects.filter(title__icontains=query)
            serializer = GameSerializer(games, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "No query provided"}, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(tags=['Price Range'])
class PriceRangeApiView(APIView):
    def get(self, request):
        prices = Game.objects.aggregate(min_price=Min('price'), max_price=Max('price'))
        return Response(prices, status=status.HTTP_200_OK)