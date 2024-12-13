from themetpy import search

# test basic search function
def test_search_basic():
    results = search(query="sunflowers")
    print(results)
    assert isinstance(results, list)

# test search with filters
def test_search_with_filters():
    results = search(
        query="sunflowers",
        isHighlight=True,
        medium="Paintings",
        hasImages=True,
        dateBegin=1800,
        dateEnd=1900
    )
    print(results)
    assert isinstance(results, list)

# test the search with no returned results
def test_search_no_results():
    results = search(query="asldkfjasldkfj")  
    print(results)
    assert isinstance(results, list)
    assert len(results) == 0