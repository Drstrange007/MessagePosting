from rest_framework import serializers
from .models import user
from .models import tweet
from .models import follower
from .models import tweet_likes


class userSerializer(serializers.ModelSerializer):

    class Meta:
        model= user
        fields= ('user_id', 'name', 'followers_count', 'folowing_count')
    

class tweetSerializer(serializers.ModelSerializer):

    class Meta:
        model= tweet
        fields= ( 'tweet_id', 'user_id', 'content', 'likes_count', 'retweet_count', 'parent_id')


class followerSerializer(serializers.ModelSerializer):

    class Meta:
        model=  follower
        fields= ('user_id','following_id')
    

class tweet_likesSerializer(serializers.ModelSerializer):

    class Meta:
        model= tweet_likes
        fields= ( 'tweet_id', 'liked_user_id', 'liked_at')


