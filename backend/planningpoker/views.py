from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Game, Card, Team, User
from .serializers import GameSerializer, CardSerializer, TeamSerializer, UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    @action(detail=True, methods=['delete'])
    def delete_game(self, request, pk=None):
        game = self.get_object()
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['get'])
    def cards(self, request, pk=None):
        game = self.get_object()
        cards = Card.objects.filter(game=game)
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer