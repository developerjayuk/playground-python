from fastapi.responses import JSONResponse

from fastapi import Request


class PinCodeNotFoundException(Exception):
    def __init__(self, pincode: str):
        self.pincode = pincode


class PinCodeInvalidException(Exception):
    def __init__(self, pincode: str, reason: str = "Pincode has invalid format"):
        self.pincode = pincode
        self.reason = reason


# custom handlers
async def pincode_not_found_handler(request: Request, exc: PinCodeNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "error": "pincode_not_found",
            "message": f"Pincode {exc.pincode} not found",
        },
    )

async def pincode_invalid_handler(request: Request, exc: PinCodeInvalidException):
    return JSONResponse(
        status_code=400,
        content={
            "error": "invalid_pincode",
            "message": f"Pincode {exc.pincode} is invalid: {exc.reason}",
        },
    )
