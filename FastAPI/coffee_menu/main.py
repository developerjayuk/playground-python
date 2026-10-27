import uvicorn
from data import menu_items
from models import MenuItem, MenuResponse

from fastapi import FastAPI, HTTPException, Query

app = FastAPI(
    title="Coffee Menu API",
    description="An API to get data for a read only menu",
)


@app.get("/")
def root():
    return {"message": "Welcome to the Coffee Menu API!"}


@app.get("/menu", response_model=MenuResponse)
def get_menu(
    category: str | None = Query(
        default=None, description="Filter menu items by category"
    ),
):
    if category:
        filtered = [
            item for item in menu_items if item["category"].lower() == category.lower()
        ]
        if not filtered:
            raise HTTPException(
                status_code=404, detail=f"No menu items found for category '{category}'"
            )
        return MenuResponse(items=filtered, count=len(filtered))

    return MenuResponse(items=menu_items, count=len(menu_items))

@app.get("/menu/{item_id}", response_model=MenuItem)
def get_item(item_id: int):
    for item in menu_items:
        if item["id"] == item_id:
            return item

    raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
