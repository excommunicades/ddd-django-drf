import pytest

from rest_framework import status

@pytest.fixture
def register_user(client):

    url_register = '/auth/register'

    user_data = {
        "username": "testuser",
        "email": "testuser@gmail.com",
        "password": "password1%"
    }

    response = client.post(
        url_register,
        user_data,
        format='json'
    )
    assert response.status_code == status.HTTP_201_CREATED
    return user_data

@pytest.fixture
def register_another_user(client):

    url_register = '/auth/register'

    user_data = {
        "username": "testuser2",
        "email": "testuser2@gmail.com",
        "password": "password1%"
    }

    response = client.post(
        url_register,
        user_data,
        format='json'
    )
    assert response.status_code == status.HTTP_201_CREATED
    return user_data

@pytest.fixture
def obtain_token(client, register_user):

    url_login = '/auth/login'

    login_data = {
        "email": register_user["email"],
        "password": register_user["password"]
    }

    response = client.post(
        url_login,
        login_data,
        format='json'
    )

    assert response.status_code == status.HTTP_200_OK
    access_token = response.data.get('tokens', {}).get('access_token')
    refresh_token = response.data.get('tokens', {}).get('refresh_token')

    assert access_token is not None
    assert refresh_token is not None

    return access_token

@pytest.fixture
def obtain_second_token(client, register_another_user):

    url_login = '/auth/login'

    login_data = {
        "email": register_another_user["email"],
        "password": register_another_user["password"]
    }

    response = client.post(
        url_login,
        login_data,
        format='json'
    )

    assert response.status_code == status.HTTP_200_OK
    access_token = response.data.get('tokens', {}).get('access_token')
    refresh_token = response.data.get('tokens', {}).get('refresh_token')

    assert access_token is not None
    assert refresh_token is not None

    return access_token


@pytest.mark.django_db
def test_product_creation(client, obtain_token):

    access_token = obtain_token
    url_create_product = '/products/create'
    headers = {'Authorization': f'Bearer {access_token}'}

    response = client.post(
        url_create_product,
        {'title': 'test_title','description': 'test_description'},
        format='json',
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    response = client.post(
        url_create_product,
        {'title': 'test_title','description': 'test_description'},
        format='json',
        headers=headers
    )

    assert response.status_code == status.HTTP_201_CREATED

    assert response.data.get('title') == 'test_title'
    assert response.data.get('description') == 'test_description'

    response = client.post(
        url_create_product,
        {'title': 'test_title'},
        format='json',
        headers=headers
    )

    assert response.status_code == status.HTTP_201_CREATED

    assert response.data.get('title') == 'test_title'
    assert response.data.get('description') == None

    response = client.post(
        url_create_product,
        {},
        format='json',
        headers=headers
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.fixture
def create_product(client, obtain_token):

    access_token = obtain_token
    url_create_product = '/products/create'
    headers = {'Authorization': f'Bearer {access_token}'}

    response = client.post(
        url_create_product,
        {'title': 'test_title','description': 'test_description'},
        format='json',
        headers=headers
    )

    return response.data

@pytest.mark.django_db
def test_product_list_returning(client, obtain_token, create_product):

    access_token = obtain_token

    response = client.get(
        path='/products/all',
        format='json',
        headers={'Authorization': f'Bearer {access_token}'}
    )

    print(response.data)

    assert response.status_code == status.HTTP_200_OK
    assert response.data == [{'description': 'test_description', 'id': 3, 'owner': 'testuser', 'title': 'test_title'}]

@pytest.mark.django_db
def test_product_returning(client, obtain_token, create_product):

    access_token = obtain_token

    response = client.get(
        path='/products/1000',
        format='json',
        headers={'Authorization': f'Bearer {access_token}'}
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND

    response = client.get(
        path='/products/4',
        format='json',
        headers={'Authorization': f'Bearer {access_token}'}
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {'description': 'test_description', 'id': 4, 'owner': 'testuser', 'title': 'test_title'}

@pytest.mark.django_db
def test_product_updates(client, obtain_token, obtain_second_token,  create_product):

    access_token = obtain_token
    access_token2 = obtain_second_token

    response = client.get(
        path='/products/5',
        format='json',
        headers={'Authorization': f'Bearer {access_token}'}
    )

    assert response.status_code == status.HTTP_200_OK

    assert response.data == {'description': 'test_description', 'id':5, 'owner': 'testuser', 'title': 'test_title'}

    response = client.patch(
        path='/products/5',
        data={'title': 'updated_title', 'description': 'updated_description'},
        content_type='application/json',
        headers={'Authorization': f'Bearer {access_token}'}
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {'title': 'updated_title', 'description': 'updated_description'}

    response = client.patch(
        path='/products/5',
        data={'title': 'updated_title2'},
        content_type='application/json',
        headers={'Authorization': f'Bearer {access_token}'}
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {'title': 'updated_title2', 'description': 'updated_description'}

    response = client.patch(
        path='/products/5',
        data={},
        content_type='application/json',
        headers={'Authorization': f'Bearer {access_token}'}
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST

    response = client.patch(
        path='/products/5124',
        data={'title': 'updated_title2'},
        content_type='application/json',
        headers={'Authorization': f'Bearer {access_token}'}
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND

    response = client.patch(
        path='/products/5',
        data={'title': 'updated_title', 'description': 'updated_description'},
        content_type='application/json',
        headers={'Authorization': f'Bearer {access_token2}'}
    )
    print(response.data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.data == {'erorrs': 'You must to be an owner of this product for update operation.'}

@pytest.mark.django_db
def test_product_delete(client, obtain_token, obtain_second_token,  create_product):

    access_token = obtain_token
    access_token2 = obtain_second_token

    response = client.delete(
        path='/products/6',
        content_type='json',
        headers={'Authorization': f'Bearer {access_token2}'}
    )
    print(response.data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


    response = client.delete(
        path='/products/6',
        content_type='json',
        headers={'Authorization': f'Bearer {access_token}'}
    )
    print(response.data)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert response.data == {"message": "Product with id: 6 was deleted successfully!"}

    response = client.delete(
        path='/products/1000',
        content_type='json',
        headers={'Authorization': f'Bearer {access_token}'}
    )
    print(response.data)
    assert response.status_code == status.HTTP_404_NOT_FOUND
