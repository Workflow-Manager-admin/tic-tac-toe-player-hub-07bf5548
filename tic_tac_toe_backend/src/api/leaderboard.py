from fastapi import APIRouter, Depends, HTTPException
from src.api.models import Leaderboard
from src.api.auth import get_current_user
from src.api.models import UserInDB

router = APIRouter(
    prefix="/api",
    tags=["Leaderboard"]
)

# Leaderboard calculation logic (stub)
class LeaderboardManager:
    """Logic for retrieving and calculating the leaderboard."""

    # PUBLIC_INTERFACE
    def get_leaderboard(self) -> Leaderboard:
        """Calculate and return the current leaderboard."""
        # TODO: Actual implementation with leaderboard aggregation
        raise NotImplementedError

leaderboard_manager = LeaderboardManager()

# PUBLIC_INTERFACE
@router.get("/leaderboard", response_model=Leaderboard, summary="Get leaderboard")
async def get_leaderboard_endpoint(user: UserInDB = Depends(get_current_user)):
    """Return the top players in the leaderboard."""
    # TODO: Actual implementation
    raise HTTPException(status_code=501, detail="Not Implemented")
