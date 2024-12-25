import pytest

from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_registration(client):

    url = '/auth/register'

    response = client.post(url,{},format='json') # register with blank fields
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {"username":["This field is required."],"email":["This field is required."],"password":["This field is required."]}

    response = client.post( # invalid email
                    url,{"username": "testuser","email": "testusergmail.com","password": "password1%"},format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {"email": ["Enter a valid email address."]}

    response = client.post( # password less then 8 char
                    url,{"username": "testuser","email": "testuser@gmail.com","password": "pass"},format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {"password": ["Ensure this field has at least 8 characters."]}

    response = client.post( # successfully registration
                    url,{"username": "testuser","email": "testuser@gmail.com","password": "password1%"},format='json')
    assert response.status_code == status.HTTP_201_CREATED

    response = client.post(url,{"username": "testuser","email": "testuser@gmail.com","password": "password1%"},format='json') # email already taken
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {"error": "User with this email already exist."}

@pytest.mark.django_db
def test_user_authorization(client):

    create_user = client.post( # create new user with id 2
                    '/auth/register',
                    {"username": "testuser","email": "testuser@gmail.com","password": "password1%"},
                    format='json')

    url = '/auth/login'

    response = client.post(url,{}, format='json') # login with blank fields
    assert response.data == {"email":["This field is required."],"password":["This field is required."]}

    response = client.post( # password less then 8 char
                    url,{"email": "testuser@gmail.com","password": "pass"},format='json')

    response = client.post(url,{"email": "testuser@gmail.com","password": "password1%"}, format='json') # success login
    assert response.status_code == status.HTTP_200_OK
    assert response.data.get('user') == {"id":2,"username":"testuser","email":"testuser@gmail.com"}
    assert response.data.get('tokens', {}).get('refresh_token')
    assert response.data.get('tokens', {}).get('access_token')

    response = client.post(url,{"email": "testuser@gmail.com","password": "password1"}, format='json') # failure login
    assert response.status_code == status.HTTP_400_BAD_REQUEST
