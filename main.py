from fastapi import FastAPI
import re

app = FastAPI()

@app.get("/convert/{num_str}")
async def convert_to_int(num_str: str):
    # Remove non-integer characters
    num_str = re.sub(r'[^0-9]', '', num_str)
    
    # Convert to int if not empty, otherwise return None
    if num_str:
        try:
            return int(num_str)
        except ValueError:
            return None
    else:
        return None