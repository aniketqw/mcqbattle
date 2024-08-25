# # # from django.shortcuts import render
# # # from rest_framework import status
# # # from rest_framework.decorators import api_view
# # # from rest_framework.response import Response
# # # from .models import Game
# # # from .serializers import GameSerializer
# # #
# # # # decorator indicating create game is POST only
# # # @api_view(['POST'])
# # # def create_game(request):
# # #     if request.method == 'POST':
# # #         serializer = GameSerializer(data=request.data)  # store complex data (like fields and all)in serializer
# # #         if serializer.is_valid():  #validate the serializer
# # #             serializer.save(status='waiting')
# # #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# # #
# # # @api_view(['GET'])
# # # def list_games(request):
# # #     if request.method == 'GET':
# # #         games = Game.objects.filter(status='waiting')
# # #         serializer = GameSerializer(games, many=True)
# # #         return Response(serializer.data)
# # # views.py
# # from rest_framework import status
# # from rest_framework.decorators import api_view
# # from rest_framework.response import Response
# # from .models import Game
# # from .serializers import GameSerializer
# # from .pusher_client import pusher_client
# # from mcqs.models import MCQ
# #
# # # @api_view(['POST'])
# # # def create_game(request):
# # #     if request.method == 'POST':
# # #         serializer = GameSerializer(data=request.data)
# # #         if serializer.is_valid():
# # #             game = serializer.save(status='waiting')
# # #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# # #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# #
# # # @api_view(['POST'])
# # # def create_game(request):
# # #     mcq_ids = request.data.get('mcq_ids', [])
# # #     if not mcq_ids:
# # #         return Response({'error': 'No MCQ IDs provided'}, status=status.HTTP_400_BAD_REQUEST)
# # #
# # #     try:
# # #         mcqs = MCQ.objects.filter(id__in=mcq_ids)
# # #         if not mcqs:
# # #             return Response({'error': 'No valid MCQs found'}, status=status.HTTP_400_BAD_REQUEST)
# # #
# # #         game = Game.objects.create(status='waiting')
# # #         game.mcqs.set(mcqs)
# # #         game.save()
# # #
# # #         pusher_client.trigger(f'game-{game.gameId}', 'game-created', {
# # #             'gameId': game.gameId,
# # #             'status': game.status
# # #         })
# # #
# # #         serializer = GameSerializer(game)
# # #         return Response(serializer.data, status=status.HTTP_201_CREATED)
# # #     except Exception as e:
# # #         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# #
# # @api_view(['POST'])
# # def create_game(request):
# #     try:
# #         # Extract the data from the request
# #         name = request.data.get('name')
# #         gameId = request.data.get('gameId')
# #         playerId = request.data.get('playerId')
# #         adminId = request.data.get('adminId')
# #         mcq_ids = request.data.get('mcq_ids', [])
# #         status = request.data.get('status', 'waiting')
# #
# #         if not mcq_ids:
# #             return Response({'error': 'No MCQ IDs provided'}, status=status.HTTP_400_BAD_REQUEST)
# #
# #         # Validate and get the MCQs
# #         mcqs = MCQ.objects.filter(id__in=mcq_ids)
# #         if not mcqs.exists():
# #             return Response({'error': 'No valid MCQs found'}, status=status.HTTP_400_BAD_REQUEST)
# #
# #         # Create the game
# #         game = Game.objects.create(
# #             name=name,
# #             gameId=gameId,
# #             playerId=playerId,
# #             adminId=adminId,
# #             status=status
# #         )
# #         game.mcqs.set(mcqs)
# #         game.save()
# #
# #         # Trigger Pusher event
# #         pusher_client.trigger(f'game-{game.gameId}', 'game-created', {
# #             'gameId': game.gameId,
# #             'status': game.status
# #         })
# #
# #         # Serialize and return the response
# #         serializer = GameSerializer(game)
# #         return Response(serializer.data, status=status.HTTP_201_CREATED)
# #
# #     except Exception as e:
# #         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# # # @api_view(['POST'])
# # # def join_game(request):
# # #     game_id = request.data.get('gameId')
# # #     player_id = request.data.get('playerId')
# # #
# # #     try:
# # #         game = Game.objects.get(gameId=game_id, status='waiting')
# # #         pusher_client.trigger('natural-badlands-505', 'join-request', {
# # #             'gameId': game_id,
# # #             'playerId': player_id
# # #         })
# # #         return Response({'message': 'Join request sent'}, status=status.HTTP_200_OK)
# # #     except Game.DoesNotExist:
# # #         return Response({'error': 'Game not found or not in waiting status'}, status=status.HTTP_404_NOT_FOUND)
# #
# # @api_view(['GET'])
# # def list_games(request):
# #     if request.method == 'GET':
# #         games = Game.objects.filter(status='waiting')
# #         serializer = GameSerializer(games, many=True)
# #         return Response(serializer.data)
# #
# # def join_game(request):
# #     game_id = request.data.get('gameId')
# #     player_id = request.data.get('playerId')
# #
# #     try:
# #         game = Game.objects.get(gameId=game_id, status='waiting')
# #         pusher_client.trigger(f'game-{game_id}', 'join-request', {
# #             'gameId': game_id,
# #             'playerId': player_id
# #         })
# #         return Response({'message': 'Join request sent'}, status=status.HTTP_200_OK)
# #     except Game.DoesNotExist:
# #         return Response({'error': 'Game not found or not in waiting status'}, status=status.HTTP_404_NOT_FOUND)
#
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Game
# from .serializers import GameSerializer
# from .pusher_client import pusher_client
# from mcqs.models import MCQ
#
# @api_view(['POST'])
# def create_game(request):
#     try:
#         # Extract the data from the request
#         name = request.data.get('name')
#         gameId = request.data.get('gameId')
#         playerId = request.data.get('playerId')
#         adminId = request.data.get('adminId')
#         mcq_ids = request.data.get('mcq_ids', [])
#         status = request.data.get('status', 'waiting')
#
#         if not mcq_ids:
#             return Response({'error': 'No MCQ IDs provided'}, status=status.HTTP_400_BAD_REQUEST)
#
#         # Validate and get the MCQs
#         mcqs = MCQ.objects.filter(id__in=mcq_ids)
#         if not mcqs.exists():
#             return Response({'error': 'No valid MCQs found'}, status=status.HTTP_400_BAD_REQUEST)
#
#         # Create the game
#         game = Game.objects.create(
#             name=name,
#             gameId=gameId,
#             playerId=playerId,
#             adminId=adminId,
#             status=status
#         )
#         game.mcqs.set(mcqs)
#         game.save()
#
#         # Trigger Pusher event
#         pusher_client.trigger(f'game-{game.gameId}', 'game-created', {
#             'gameId': game.gameId,
#             'status': game.status
#         })
#
#         # Serialize and return the response
#         serializer = GameSerializer(game)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
# @api_view(['GET'])
# def list_games(request):
#     if request.method == 'GET':
#         games = Game.objects.filter(status='waiting')
#         serializer = GameSerializer(games, many=True)
#         return Response(serializer.data)
#
# @api_view(['POST'])
# def join_game(request):
#     game_id = request.data.get('gameId')
#     player_id = request.data.get('playerId')
#
#     try:
#         game = Game.objects.get(gameId=game_id, status='waiting')
#         pusher_client.trigger(f'game-{game_id}', 'join-request', {
#             'gameId': game_id,
#             'playerId': player_id
#         })
#         return Response({'message': 'Join request sent'}, status=status.HTTP_200_OK)
#     except Game.DoesNotExist:
#         return Response({'error': 'Game not found or not in waiting status'}, status=status.HTTP_404_NOT_FOUND)
from rest_framework import status as http_status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Game
from .serializers import GameSerializer
from .pusher_client import pusher_client
from mcqs.models import MCQ

@api_view(['POST'])
def create_game(request):
    try:
        # Extract the data from the request
        name = request.data.get('name')
        gameId = request.data.get('gameId')
        playerId = request.data.get('playerId')
        adminId = request.data.get('adminId')
        mcq_ids = request.data.get('mcq_ids', [])
        game_status = request.data.get('status', 'waiting')  # Rename variable to avoid conflict

        if not mcq_ids:
            return Response({'error': 'No MCQ IDs provided'}, status=http_status.HTTP_400_BAD_REQUEST)

        # Validate and get the MCQs
        mcqs = MCQ.objects.filter(id__in=mcq_ids)
        if not mcqs.exists():
            return Response({'error': 'No valid MCQs found'}, status=http_status.HTTP_400_BAD_REQUEST)

        # Create the game
        game = Game.objects.create(
            name=name,
            gameId=gameId,
            playerId=playerId,
            adminId=adminId,
            status=game_status  # Use renamed variable here
        )
        game.mcqs.set(mcqs)
        game.save()

        # Trigger Pusher event
        pusher_client.trigger(f'game-{game.gameId}', 'game-created', {
            'gameId': game.gameId,
            'status': game.status
        })

        # Serialize and return the response
        serializer = GameSerializer(game)
        return Response(serializer.data, status=http_status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': str(e)}, status=http_status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def list_games(request):
    if request.method == 'GET':
        games = Game.objects.filter(status='waiting')
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def join_game(request):
    game_id = request.data.get('gameId')
    player_id = request.data.get('playerId')

    try:
        game = Game.objects.get(gameId=game_id, status='waiting')
        pusher_client.trigger(f'game-{game_id}', 'join-request', {
            'gameId': game_id,
            'playerId': player_id
        })
        return Response({'message': 'Join request sent'}, status=http_status.HTTP_200_OK)
    except Game.DoesNotExist:
        return Response({'error': 'Game not found or not in waiting status'}, status=http_status.HTTP_404_NOT_FOUND)
