import requests

def test_get_factors_endpoint():
    # Define the payload with a valid subset
    valid_payload = {
        "data": [
            {"var_name": "country", "category": "UK"},
            {"var_name": "age_group", "category": "18-30"}
        ]
    }

    # Send POST request to the /get_factors endpoint with valid subset
    response = requests.post("http://127.0.0.1:8000/get_factors", json=valid_payload)

    # Assert the response status code is 200 (OK)
    assert response.status_code == 200

    # Print factors from the response
    factors = response.json()
    print("Factors:", factors)

    # Assert the response content
    expected_response = {
        "results": [
            {"var_name": "country", "category": "UK", "factor": 0.25},
            {"var_name": "age_group", "category": "18-30", "factor": 0.33}
        ]
    }
    assert factors == expected_response

    # Define the payload with an invalid category
    invalid_payload = {
        "data": [
            {"var_name": "country", "category": "UK"},
            {"var_name": "age_group", "category": "40-60"}  # Invalid category
        ]
    }

    # Send POST request to the /get_factors endpoint with invalid category
    response = requests.post("http://127.0.0.1:8000/get_factors", json=invalid_payload)

    # Assert the response status code is 400 (Bad Request)
    assert response.status_code == 400

    # Print response content
    print("Factor Detail:", response.json()["detail"])

    # Print "Test Passed" if both assertions pass
    print("Test Passed")

# Run the test for invalid category
test_get_factors_endpoint()
