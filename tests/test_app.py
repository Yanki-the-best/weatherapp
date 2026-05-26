from app import app

def test_city_weather():
    client = app.test_client()
    response = client.get('/weather/london')
    assert response.status_code == 200

def test_response_has_city():
    client = app.test_client()
    response = client.get('/weather/london')
    data = response.get_json()
    assert data['city'] == 'london'
