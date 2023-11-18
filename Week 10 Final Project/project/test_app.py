import pytest

def test_successful_registration(client):
    # Use your testing client (e.g., Flask's test_client)

    # Send a POST request to register a new user
    response = client.post('/register', data={'username': 'username', 'password': 'password', 'confirmation': 'password'})

    # Check if the status code is 200 for a successful registration
    assert response.status_code == 200

    # Additional assertions if needed
    assert b'Registered Successfully!' in response.data
