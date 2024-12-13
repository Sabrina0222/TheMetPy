import pytest
import requests
from themetpy import get_all_object_ids, get_object

# test to fetch all object ids
def test_get_all_object_ids():
    object_ids = get_all_object_ids(departmentIds=1)
    assert isinstance(object_ids, list)
    assert all(isinstance(obj_id, int) for obj_id in object_ids)

# test to get one specific object's information -- successful
def test_get_object_success():
    objectID = 45734  # Known valid Object ID
    data = get_object(objectID, handle_missing='log')
    assert isinstance(data, dict)
    assert data['objectID'] == objectID

# test to get one specific object's information with invalid id -- failed
def test_get_object_invalid_id():
    objectID = 999999999  # Invalid Object ID
    with pytest.raises(ValueError):
        get_object(objectID)

# test to get one specific object's information with missing data -- using mocking to simulate missing data object
def test_get_object_missing_data(mocker):
    objectID = 12345  # Arbitrary Object ID

    # Mock response data with missing fields
    mock_response = {
        "objectID": objectID,
        "title": "Sunflowers",
        # "artistDisplayName" is intentionally set to be missing
        "primaryImage": "",
        "objectDate": "1907",
        "medium": "Oil on canvas",
        "dimensions": "24 x 36 in.",
        "department": "Paintings",
        "culture": "American"
    }

    # Mock the requests.get call within get_object
    mocker.patch('requests.get', return_value=MockResponse(mock_response, 200))

    data = get_object(objectID, handle_missing='replace', replace_value='Unknown', verbose=True)
    assert data is not None
    assert data['artistDisplayName'] == 'Unknown'

# use a mock to simulate a request and response
class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code
        self.ok = self.status_code == 200

    def json(self):
        return self.json_data

    def raise_for_status(self):
        if not self.ok:
            raise requests.exceptions.HTTPError(f"{self.status_code} Error")