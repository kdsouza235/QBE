from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import csv

# Define FastAPI app
app = FastAPI()

# Define models for request payloads
class ValidateRequest(BaseModel):
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
