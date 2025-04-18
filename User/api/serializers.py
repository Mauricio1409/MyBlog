from rest_framework.serializers import ModelSerializer
from User.models import User

class UserRegisterSerializer(ModelSerializer):
    class Meta : 
        model = User
        fields = ['email', 'username', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance
    
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'username', 'first_name', 'last_name']

class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']