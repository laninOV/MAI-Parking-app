import sys
import os
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app

client = TestClient(app)

def test_get_parking():
    mock_data = {"parking": ["Lot A", "Lot B", "Lot C"]}

    with patch("api.service.parking_service.get_parking_data", return_value=mock_data):
        response = client.get("/v1/parking/")
        assert response.status_code == 200
        assert response.json() == mock_data
