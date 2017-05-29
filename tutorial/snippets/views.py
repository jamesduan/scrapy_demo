# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics


# Create your views here.
from django.contrib.auth.models import User, Group
from serializers import UserSerializer, GroupSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
