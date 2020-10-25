from django.db import models


class user(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add= True,null=True)
    

class tweet(models.Model):
    tweet_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(user,to_field='user_id', db_column='user_id', on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add= True,null=True)
    likes_count = models.IntegerField(default=0)
    retweet_count = models.IntegerField(default=0)
    parent_id = models.ForeignKey(user,to_field='user_id',related_name='parent', on_delete=models.CASCADE)
    parent_tweet_id = models.IntegerField(null=True)


class follower(models.Model):
    user_id = models.ForeignKey(user,to_field='user_id', related_name='follow',db_column='user_id', on_delete=models.CASCADE)
    following_id = models.ForeignKey(user,to_field='user_id',db_column='following_id', on_delete=models.CASCADE)


class tweet_likes(models.Model):
    tweet_id = models.ForeignKey('tweet', to_field='tweet_id', db_column='tweet_id', on_delete=models.CASCADE)
    liked_user_id = models.ForeignKey('user',to_field='user_id',db_column='liked_user_id', on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add= True,null=True)



#dclass retweet(models.Model):
    

