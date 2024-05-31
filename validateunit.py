import requests

def test_validate_endpoint():
    # Create a payload that should be validated
    valid_payload = {
        "data": [
            {"var_name": "country", "category": "Australia"},
            {"var_name": "age_group", "category": "50+"}
        ]
    }

    # Send POST request to the /validate endpoint to test valid_payload
    response_valid = requests.post("http://127.0.0.1:8000/validate", json=valid_payload)

    # Assert the response status code is 200 (OK) for valid data
    assert response_valid.status_code == 200

    # Print out the validation details
    print("Validation detail for valid payload:", response_valid.json()["message"])

    # Define the payload with invalid data
    invalid_payload = {
        "data": [
            {"var_name": "country", "category": "UK"},
            {"var_name": "age_group", "category": "invalid_category"}  # Invalid category
        ]
    }

    # Send POST request to the /validate endpoint to test invalid_payload
    response_invalid = requests.post("http://127.0.0.1:8000/validate", json=invalid_payload)

    # Assert the response status code is 400 (Bad Request) for invalid category
    assert response_invalid.status_code == 400

    # Print out the validation details for the invalid payload
    print("Validation detail for invalid payload:", response_invalid.json()["detail"])

    # Print "Test Passed" if both assertions pass
    print("Test Passed")

# Run the test
test_validate_endpoint()
