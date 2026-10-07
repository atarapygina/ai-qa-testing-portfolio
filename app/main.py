from fastapi import FastAPI

app = FastAPI(title="AI Customer Support API")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/orders/{order_id}")
def get_order(order_id: str):
    return {
        "order_id": order_id,
        "status": "shipped",
        "tracking_number": "TRK123456",
        "estimated_delivery": "2026-10-05"
    }
