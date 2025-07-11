from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# PUBLIC_INTERFACE
class UserCreate(BaseModel):
    """User registration and login model."""
    username: str = Field(..., description="Unique username for the user")
    password: str = Field(..., description="User password (hashed in storage)")


# PUBLIC_INTERFACE
class UserInDB(UserCreate):
    """User as stored in the database."""
    id: int = Field(..., description="Unique user ID")
    hashed_password: str = Field(..., description="Hashed password")
    created_at: datetime = Field(..., description="Account creation timestamp")
    last_login: Optional[datetime] = Field(None, description="Most recent login timestamp")


# PUBLIC_INTERFACE
class UserStats(BaseModel):
    """User statistics for the leaderboard."""
    wins: int = Field(0, description="Number of games won")
    losses: int = Field(0, description="Number of games lost")
    draws: int = Field(0, description="Number of games drawn")
    games_played: int = Field(0, description="Total number of games played")


# PUBLIC_INTERFACE
class GameBoard(BaseModel):
    """Represents a Tic Tac Toe board (3x3)."""
    cells: List[List[Optional[str]]] = Field(
        ..., description="3x3 grid representing the board. Values: X, O, or None."
    )


# PUBLIC_INTERFACE
class GameCreate(BaseModel):
    """Game creation input."""
    creator_id: int = Field(..., description="ID of player creating the game")
    opponent_id: Optional[int] = Field(None, description="ID of invited opponent, optional")


# PUBLIC_INTERFACE
class GameInDB(BaseModel):
    """Game as stored in the database."""
    id: int = Field(..., description="Unique game ID")
    player_x: int = Field(..., description="User ID of X player")
    player_o: int = Field(..., description="User ID of O player")
    board: GameBoard = Field(..., description="Current board state")
    current_turn: str = Field(..., description="'X' or 'O'")
    is_active: bool = Field(..., description="Is game currently active?")
    winner: Optional[str] = Field(None, description="Winner symbol ('X', 'O', or None for draw)")
    started_at: datetime = Field(..., description="Game start timestamp")
    ended_at: Optional[datetime] = Field(None, description="Game end timestamp")


# PUBLIC_INTERFACE
class MoveCreate(BaseModel):
    """Player move input."""
    game_id: int = Field(..., description="ID of the game")
    player_id: int = Field(..., description="ID of the player making the move")
    row: int = Field(..., description="Board row index (0, 1, or 2)")
    col: int = Field(..., description="Board column index (0, 1, or 2)")


# PUBLIC_INTERFACE
class MoveInDB(MoveCreate):
    """Move as stored in the database."""
    id: int = Field(..., description="Unique move ID")
    symbol: str = Field(..., description="'X' or 'O'")
    created_at: datetime = Field(..., description="Timestamp of the move")


# PUBLIC_INTERFACE
class GameHistory(BaseModel):
    """Game history record for a user."""
    game_id: int
    opponent: str
    result: str  # 'win', 'loss', 'draw'
    played_at: datetime


# PUBLIC_INTERFACE
class LeaderboardEntry(BaseModel):
    """Leaderboard entry for a user."""
    user_id: int
    username: str
    stats: UserStats


# PUBLIC_INTERFACE
class Leaderboard(BaseModel):
    """Leaderboard - list of leaderboard entries"""
    entries: List[LeaderboardEntry]

