from django.shortcuts import render

from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import user, tweet, follower, tweet_likes
from .serializers import userSerializer, tweetSerializer, followerSerializer, tweet_likesSerializer
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from rest_framework.decorators import action


class users(APIView):
    
    def get(self, request):

        user1 = user.objects.all()
        serializer = userSerializer(user1, many=True)
        return Response(data= serializer.data)

class followerinfo(APIView):
    
    def get(self, request, userId):

        user1 = follower.objects.filter(user_id=userId).only('following_id').all()
        serializer = followerSerializer(user1, many=True)
        return Response(data= serializer.data)

class followinginfo(APIView):
    
    def get(self, request, userId):
        
        user1 = follower.objects.filter(following_id=userId).only('user_id').all()
        serializer = followerSerializer(user1, many=True)
        return Response(data= serializer.data)

class timeline(APIView):

    def get(self, request, usersId, duration):

        tweet1 = tweet.objects.filter(user_id__in = follower.objects.filter(user_id=usersId).values_list('following_id'),
         created_at__gte= (timezone.now()- timedelta(days=duration)))
        serializer = tweetSerializer(tweet1, many = True)
        return Response(data= serializer.data)


class tweetlike(APIView):

    def put(self, request, userId,tweetId):
        
        tweet1 = tweet.objects.filter(tweet_id=tweetId).first()
        user1 = user.objects.filter(user_id=userId).first()
        
        if tweet1 in [None, ''] :
            return Response(data="No such Tweet Exists")
        else :
            tweet2 = tweet_likes.objects.filter(liked_user_id=userId,tweet_id=tweetId).first()
            if tweet2 in [None, ''] :
                serializer = tweetSerializer(tweet1, data={'likes_count': tweet1.likes_count+1}, partial =True )
                tweet3 = tweet_likes(liked_user_id=user1, tweet_id=tweet1)
                if serializer.is_valid():
                    serializer.save()
                    tweet3.save()
                    return Response("success")
                return Response("wrong paramente")
            return Response("already liked")

    def get(self, request, userId, tweetId):
        tweetliked1 = tweet_likes.objects.filter(liked_user_id__in = follower.objects.filter(user_id=userId).values_list('following_id'), 
        tweet_id=tweetId)
        serializer = tweet_likesSerializer(tweetliked1, many=True)
        return Response(data= serializer.data)


class retweet(APIView):

    def put(self, request, userId,tweetId):
        
        tweet1 = tweet.objects.filter(tweet_id=tweetId).first()
        #print( str(tweet1.user_id.user_id))
        if tweet1 in [None, ''] :
            return Response(data="No such Tweet Exists")
        else :
            user1 = user.objects.filter(user_id=userId).first()
            serializer = tweetSerializer(tweet1, data={'retweet_count': tweet1.retweet_count+1}, partial =True )
            user2 = user.objects.filter(user_id=getattr(tweet1.user_id , 'user_id')).first()
    
            tweet2 = tweet.objects.filter(user_id=userId,parent_tweet_id=tweetId).first()
            if tweet2 in [None, ''] : 
                if serializer.is_valid():
                    serializer.save()
                    tweet3 = tweet(user_id=user1, parent_id = user2,parent_tweet_id=tweetId, content=tweet1.content)
                    tweet3.save()
                    return Response("success")
                return Response("wrong paramente")
            return Response("already retweeted")
    
    def get(self, request, userId, tweetId):
        
        retweet1 = tweet.objects.filter(user_id__in = follower.objects.filter(user_id=userId).values_list('following_id'), 
        parent_tweet_id=tweetId).only('user_id')
        serializer = tweetSerializer(retweet1, many=True)
        return Response(data= serializer.data)


class tweets(APIView):

    def get(self, request):

        user1 = tweet.objects.all()
        serializer = tweetSerializer(user1, many=True)
        return Response(data= serializer.data)




             



   

        







