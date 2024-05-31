from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import csv

# Define FastAPI app
app = FastAPI()

# Define models for request payloads
class ValidateRequest(BaseModel):
    data: List[dict]
    
class GetFactorsRequest(BaseModel):
    data: List[dict]

# Load data from CSV
def read_csv(file_path):
    data = []
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append({
                "var_name": row["var_name"],
                "category": row["category"],
                "factor": float(row["factor"])  # Convert factor to float
            })
    return data

# Define API endpoints
@app.post("/validate")
async def validate(payload: ValidateRequest):
    """
    Validates the JSON payload.
    """
    print("Received request:", payload)  # Server Log statement
    csv_data = read_csv("data.csv")
    print("CSV Data:", csv_data)  # Server Log statement

    # Create a set of all valid categories for each variable name
    valid_categories = {}
    for entry in csv_data:
        var_name = entry["var_name"]
        category = entry["category"]
        if var_name not in valid_categories:
            valid_categories[var_name] = set()
        valid_categories[var_name].add(category)

    print("Valid categories:", valid_categories)  # Server Log statement

    # Check if each item in payload.data has both a valid variable name and category
    for item in payload.data:
        print("Validating item:", item)  # Server Log statement
        var_name = item.get("var_name")
        category = item.get("category")
        if var_name not in valid_categories:
            raise HTTPException(status_code=400, detail=f"Invalid variable name: {var_name}")
        if category not in valid_categories[var_name]:
            raise HTTPException(status_code=400, detail=f"Invalid category '{category}' for variable name '{var_name}'")
    
    print("Validation completed successfully.")  # Server Log statement
    return {"message": "Data is valid."}

@app.post("/get_factors")
async def get_factors(payload: GetFactorsRequest):
    """
    Maps the factors and returns the results in JSON format.
    """
    print("Received request:", payload)  # Server Log statement
    csv_data = read_csv("data.csv")
    print("CSV Data:", csv_data)  # Server Log statement

    # Create a dictionary to store the factors
    factors = {}

    # Iterate over the items in the payload
    for item in payload.data:
        var_name = item.get("var_name")
        category = item.get("category")

        print(f"Checking factor for variable name '{var_name}' and category '{category}'")  # Server Log statement

        # Find the factor corresponding to the given variable name and category
        for entry in csv_data:
            if entry["var_name"] == var_name and entry["category"] == category:
                factors.setdefault("results", []).append({
                    "var_name": var_name,
                    "category": category,
                    "factor": entry["factor"]
                })
                break
        else:
            raise HTTPException(status_code=400, detail=f"No factor found for variable name '{var_name}' and category '{category}'")

    print("Factors:", factors)  # Server Log statement
    return factors
