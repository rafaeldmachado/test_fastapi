from fastapi import FastAPI, APIRouter

app = FastAPI(
    title="FastAPI test"
)

router = APIRouter()

@router.get('/', status_code=200)
def hello() -> root:
    """
    Root Get
    """
    return {'message': 'Hello World!'}

app.include_router(router)