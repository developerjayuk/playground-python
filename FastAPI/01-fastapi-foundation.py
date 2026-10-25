from fastapi import FastAPI

app = FastAPI(
    title="JJ's Order Service",
    description=("Internal API for orders"),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)


@app.get("/")
def read_root():
    """Root endpoint - Healthy"""
    # FastAPI converts this dict into JSON
    return {"message": "Welcome to JJ's order service", "status": "healthy"}


@app.get("/about")
def about():
    """Returns API metadata"""
    return {
        "service": "order-service",
        "team": "backend platform",
        "region": "ap-north-1",
        "version": "1.1.8",
    }


@app.get("/orders")
def list_orders():
    """List recent orders"""
    return {
        "orders": [
            {"id": 1, "item": "Protein powder", "status": "delivered"},
            {"id": 2, "item": "Creatine", "status": "delivered"},
            {"id": 3, "item": "Magnesium", "status": "processing"}
        ]
    }
    
@app.get("/orders/status")
def order_status():
    """Get order status"""
    return {
        "todays_total": 2_123_4938,
        "top_product": "Protein powder"
    }
