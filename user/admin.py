from django.contrib import admin
from .models import user
from .models import tweet
from .models import follower
from .models import tweet_likes

admin.site.register(user)
admin.site.register(tweet)
admin.site.register(follower)
admin.site.register(tweet_likes)
