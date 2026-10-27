from fastapi import FastAPI, Request

app = FastAPI(
    title="JJ's Order Service",
    description=("Internal API for orders"),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)


@app.get(
    "/",
    summary="Root endpoint",
    description="Returns a welcome message and health status",
)
def read_root():
    """Root endpoint - Healthy"""
    # FastAPI converts this dict into JSON
    return {"message": "Welcome to JJ's order service", "status": "healthy"}


@app.get(
    "/about", summary="About the API", description="Returns metadata about the API"
)
def about():
    """Returns API metadata"""
    return {
        "service": "order-service",
        "team": "backend platform",
        "region": "ap-north-1",
        "version": "1.1.8",
    }


@app.get(
    "/orders",
    summary="List recent orders",
    description="Returns a list of recent orders with their status",
    tags=["orders"]
)
def list_orders():
    """List recent orders"""
    return {
        "orders": [
            {"id": 1, "item": "Protein powder", "status": "delivered"},
            {"id": 2, "item": "Creatine", "status": "delivered"},
            {"id": 3, "item": "Magnesium", "status": "processing"},
        ]
    }


@app.get(
    "/orders/status",
    summary="Get order status",
    description="Returns the total number of orders and the top product for the day",
    tags=["orders"]
)
def order_status():
    """Get order status"""
    return {"todays_total": 2_123_4938, "top_product": "Protein powder"}


@app.get(
    "/debug/request-info",
    summary="Debug request information",
    description="Returns information about the incoming request"
)
def request_info(request: Request):
    """Inspect the raw request data"""
    return {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "client": request.client.host,
        "query_params": dict(request.query_params),
        "path_params": request.path_params,
    }
