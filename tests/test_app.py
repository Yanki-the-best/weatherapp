from app import app
from unittest.mock import patch, MagicMock

def test_city_weather():
    mock_conn = MagicMock()
    mock_conn.cursor.return_value.fetchone.return_value = (22, 'sunny')
    
    with patch('app.get_pg_connection', return_value=mock_conn), \
         patch('app.get_mongo_db', return_value=MagicMock()):
        client = app.test_client()
        response = client.get('/weather/london')
        assert response.status_code == 200

def test_response_has_city():
    mock_conn = MagicMock()
    mock_conn.cursor.return_value.fetchone.return_value = (22, 'sunny')
    
    with patch('app.get_pg_connection', return_value=mock_conn), \
         patch('app.get_mongo_db', return_value=MagicMock()):
        client = app.test_client()
        response = client.get('/weather/london')
        data = response.get_json()
        assert data['city'] == 'london'
