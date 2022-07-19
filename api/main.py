from fastapi import FastAPI, APIRouter

from typing import Optional

RECIPES = [
    {
        "id": 1,
        "label": "Chicken Vesuvio",
        "source": "Serious Eats",
        "url": "http://www.seriouseats.com/recipes/2011/12/chicken-vesuvio-recipe.html",
    },
    {
        "id": 2,
        "label": "Chicken Paprikash",
        "source": "No Recipes",
        "url": "http://norecipes.com/recipe/chicken-paprikash/",
    },
    {
        "id": 3,
        "label": "Cauliflower and Tofu Curry Recipe",
        "source": "Serious Eats",
        "url": "http://www.seriouseats.com/recipes/2011/02/cauliflower-and-tofu-curry-recipe.html",
    },
]

app = FastAPI(
    title="FastAPI test"
)

router = APIRouter()

@router.get('/', status_code=200)
def hello() -> dict:
    """
    Root Get
    """
    return {'message': 'Hello World!'}

@router.get('/recipe/{id}', status_code=200)
def get_recipe(*, id: int) -> dict:
    """
    Fetch a single recipe by ID
    """
    result = [recipe for recipe in RECIPES if recipe["id"] == id]
    if result:
        return result[0]

@router.get('/search/', status_code=200)
def search_recipe_keyword(keyword: Optional[str] = None, max_results: Optional[int] = 10) -> dict:
    """
    Search a recipe by a keyword
    """
    if not keyword:
        return {"results": RECIPES[:max_results]}

    results = filter(lambda recipe: keyword.lower() in recipe['label'].lower(), RECIPES)
    return {'results': list(results)[:max_results]}

app.include_router(router)