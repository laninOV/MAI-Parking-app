import pytest
from unittest.mock import mock_open, patch

import json
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from api.service.parking_service import get_parking_data

@pytest.mark.asyncio
async def test_get_parking_data_file_exists():
    mock_data = {"parking": ["Lot A", "Lot B", "Lot C"]}

    with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))), patch("os.path.exists", return_value=True):
        result = await get_parking_data()
        assert result == mock_data


@pytest.mark.asyncio
async def test_get_parking_data_file_not_found():
    with patch("os.path.exists", return_value=False):
        result = await get_parking_data()
        assert result == {"error": "File not found"}
