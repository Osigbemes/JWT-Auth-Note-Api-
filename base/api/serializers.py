
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from base.models import Note, User


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class UserVmSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # extra_kwargs = {'password':{'write-only':True}}

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'phoneNumber', 'password', 'username']
        # extra_kwargs={'password':{'write-only':True}}

    # def create(self, validated_data):
    #     password = validated_data['password']
    #     password=  str(self.Meta.model.password)
    #     instance = self.Meta.model(**validated_data)
    #     if password is not None:
    #         instance.set_password(password)
    #     return instance

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
     password=validated_data['password'], email= validated_data['email'], name=validated_data['name'], 
     phoneNumber=validated_data['phoneNumber'])
        user.save()
        # newUser = User(user)
        return user

    #  def create(self, validated_data):
        #     user = User.objects.create(user_name=validated_data['user_name'], email= validated_data['email'])
    #     user.set_password(validated_data['password'])
    #     user.is_active=True
    #     user.save()
    #     return user