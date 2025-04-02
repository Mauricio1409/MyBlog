from rest_framework.serializers import ModelSerializer
from comments.models import Comments
from User.api.serializers import UserSerializer
from post.api.serializers import PostSerializer

class CommentsSrializer(ModelSerializer):
    user = UserSerializer()
    post = PostSerializer()

    class Meta:
        model = Comments
        fields = ['content', 'user', 'post', 'created_at']