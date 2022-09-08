from fastapi import APIRouter

router = APIRouter()


@router.get('/health')
def health_check() -> None:
    """
    Checks the health of a project.

    Returns: 
        200 if the project is healthy.
    """
