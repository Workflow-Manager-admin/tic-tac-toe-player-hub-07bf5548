from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# NOTE: If you encounter import errors, ensure you launch as a module with the correct PYTHONPATH, e.g.:
#  uvicorn src.api.main:app --reload --app-dir=./tic_tac_toe_backend
# or ensure 'src' is on the PYTHONPATH so 'src.api.game' is importable.

from src.api.game import router as game_router
from src.api.leaderboard import router as leaderboard_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the game and leaderboard routers for route structure scaffolding
app.include_router(game_router)
app.include_router(leaderboard_router)

@app.get("/")
def health_check():
    """Health check endpoint."""
    return {"message": "Healthy"}
