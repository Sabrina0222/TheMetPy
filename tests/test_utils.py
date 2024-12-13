from themetpy import handle_missing_data

# test to show warning that a field is missing
def test_handle_missing_log(caplog):
    data = {'title': 'Sunflowers'}
    required_fields = ['title', 'artistDisplayName']
    result = handle_missing_data(data, required_fields, handle_missing='log')
    assert result is not None
    assert result['artistDisplayName'] is None
    assert 'Missing fields: artistDisplayName' in caplog.text

# test to show None as placeholder for missing field
def test_handle_missing_filter():
    data = {'title': 'Sunflowers'}
    required_fields = ['title', 'artistDisplayName']
    result = handle_missing_data(data, required_fields, handle_missing='filter')
    assert result is None

# test to show unknown as placeholder for missing field
def test_handle_missing_replace():
    data = {'title': 'Sunflowers'}
    required_fields = ['title', 'artistDisplayName']
    result = handle_missing_data(data, required_fields, handle_missing='replace', replace_value='Unknown')
    assert result['artistDisplayName'] == 'Unknown'