from fastapi import FastAPI, HTTPException
import csv

# Define FastAPI app
app = FastAPI()

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
