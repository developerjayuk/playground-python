import uvicorn
from data import pincode_db
from exceptions import (
    PinCodeInvalidException,
    PinCodeNotFoundException,
    pincode_invalid_handler,
    pincode_not_found_handler,
)
from models import BulkRequest, BulkResponse, LocationResponse, PincodeRequest

from fastapi import FastAPI

app = FastAPI(
    title="Pincode Lookup API",
    description="An API to get data for a read only pincode lookup",
)

# regist the custom exception handlers
app.add_exception_handler(PinCodeInvalidException, pincode_invalid_handler)
app.add_exception_handler(PinCodeNotFoundException, pincode_not_found_handler)


@app.get("/")
def root():
    return {"message": "Welcome to the Pincode Lookup API!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/pincode/{pincode}", response_model=LocationResponse)
def lookup_pincode(pincode: str):

    # validate pincode format
    if len(pincode) != 6 or not pincode.isdigit():
        raise PinCodeInvalidException(pincode)

    # lookup pincode in the database
    if pincode not in pincode_db:
        raise PinCodeNotFoundException(pincode)

    return pincode_db[pincode]


@app.post("/pincode/bulk", response_model=BulkResponse)
def bulk_lookup_pincode(request: BulkRequest):
    results = []
    missing = []

    for code in request.pincodes:
        if code in pincode_db:
            results.append(pincode_db[code])
        else:
            missing.append(code)

    return BulkResponse(
        found=len(results),
        not_found=len(missing),
        results=[LocationResponse(**result) for result in results],
        missing=missing,
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
