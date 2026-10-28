from pydantic import BaseModel, field_validator


class PincodeRequest(BaseModel):
    pincode: str

    # pincode must be 6 characters long and only contain digits
    @field_validator("pincode")
    @classmethod
    def validate_pincode(cls, v):
        if len(v) != 6 or not v.isdigit():
            raise ValueError("Pincode must be 6 digits long")
        return v


class LocationResponse(BaseModel):
    pincode: str
    city: str
    state: str
    country: str


# bulk request, max of 20 values
class BulkRequest(BaseModel):
    pincodes: list[str]

    @field_validator("pincodes")
    @classmethod
    def validate_pincodes(cls, v):
        if not v:
            raise ValueError("Pincodes list cannot be empty")
        if len(v) > 20:
            raise ValueError("Pincodes list cannot contain more than 20 values")
        for pincode in v:
            if len(pincode) != 6 or not pincode.isdigit():
                raise ValueError(f"Pincode {pincode} must be 6 digits long")
        return v


class BulkResponse(BaseModel):
    status: str = "success"
    found: int
    not_found: int
    results: list[LocationResponse]
    missing: list[str]
