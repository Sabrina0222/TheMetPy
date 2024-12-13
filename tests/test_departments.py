from themetpy import get_departments

# test to fetch the list of all departments info
def test_get_departments():
    departments = get_departments()
    assert isinstance(departments, list)
    assert all('departmentId' in dept and 'displayName' in dept for dept in departments)