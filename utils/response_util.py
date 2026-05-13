def success_response(data=None, message: str = "Request successful"):
    return {
        "status": "success",
        "message": message,
        "data": data
    }