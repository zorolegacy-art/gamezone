from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


# ==========================================
# APP
# ==========================================

app = FastAPI(
    title="GameZone API",
    description="Backend API for the GameZone gaming platform",
    version="1.0.0",
)


# ==========================================
# CORS
# ==========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================
# TEMPORARY IN-MEMORY DATA
# No database required
# ==========================================

player = {
    "username": "GameMaster",
    "level": 12,
    "xp": 2450,
    "games_played": 24,
    "wins": 18,
}


games = [
    {
        "id": 1,
        "name": "Snake",
        "description": "Classic Snake game. Eat food, grow longer and beat your high score.",
        "category": "Arcade",
        "icon": "🐍",
    },
    {
        "id": 2,
        "name": "Tic-Tac-Toe",
        "description": "Battle the computer in the classic 3x3 strategy game.",
        "category": "Strategy",
        "icon": "❌",
    },
    {
        "id": 3,
        "name": "Memory Match",
        "description": "Find all matching pairs using as few moves as possible.",
        "category": "Puzzle",
        "icon": "🧠",
    },
]


leaderboard = [
    {
        "rank": 1,
        "username": "Shadow",
        "level": 28,
        "game": "Snake",
        "score": 9850,
    },
    {
        "rank": 2,
        "username": "PixelMaster",
        "level": 24,
        "game": "Memory Match",
        "score": 8720,
    },
    {
        "rank": 3,
        "username": "GameMaster",
        "level": 12,
        "game": "Snake",
        "score": 7450,
    },
    {
        "rank": 4,
        "username": "CyberNinja",
        "level": 19,
        "game": "Tic-Tac-Toe",
        "score": 6210,
    },
    {
        "rank": 5,
        "username": "Dragon",
        "level": 17,
        "game": "Memory Match",
        "score": 5580,
    },
]


# ==========================================
# REQUEST MODELS
# ==========================================

class ScoreSubmission(BaseModel):
    username: str
    game: str
    score: int


# ==========================================
# ROOT
# ==========================================

@app.get("/")
def root():
    return {
        "message": "🎮 GameZone API is running!",
        "status": "online",
        "version": "1.0.0",
    }


# ==========================================
# HEALTH CHECK
# ==========================================

@app.get("/health")
def health():
    return {
        "status": "healthy",
    }


# ==========================================
# PLAYER
# ==========================================

@app.get("/api/player")
def get_player():
    return player


# ==========================================
# GAMES
# ==========================================

@app.get("/api/games")
def get_games():
    return games


@app.get("/api/games/{game_id}")
def get_game(game_id: int):

    for game in games:

        if game["id"] == game_id:
            return game

    return {
        "error": "Game not found",
    }


# ==========================================
# LEADERBOARD
# ==========================================

@app.get("/api/leaderboard")
def get_leaderboard():
    return leaderboard


# ==========================================
# SUBMIT SCORE
# ==========================================

@app.post("/api/scores")
def submit_score(submission: ScoreSubmission):

    new_score = {
        "rank": 0,
        "username": submission.username,
        "level": player["level"],
        "game": submission.game,
        "score": submission.score,
    }

    leaderboard.append(new_score)

    # Highest scores first
    leaderboard.sort(
        key=lambda item: item["score"],
        reverse=True,
    )

    # Keep top 10
    del leaderboard[10:]

    # Recalculate ranks
    for index, item in enumerate(leaderboard):
        item["rank"] = index + 1

    # Update current player
    if submission.username == player["username"]:

        player["games_played"] += 1

        player["xp"] += submission.score

    return {
        "message": "Score submitted successfully",
        "score": submission.score,
        "game": submission.game,
        "leaderboard": leaderboard,
    }


# ==========================================
# RESET DATA
# ==========================================

@app.post("/api/reset")
def reset_data():

    global leaderboard

    leaderboard = [
        {
            "rank": 1,
            "username": "Shadow",
            "level": 28,
            "game": "Snake",
            "score": 9850,
        },
        {
            "rank": 2,
            "username": "PixelMaster",
            "level": 24,
            "game": "Memory Match",
            "score": 8720,
        },
        {
            "rank": 3,
            "username": "GameMaster",
            "level": 12,
            "game": "Snake",
            "score": 7450,
        },
        {
            "rank": 4,
            "username": "CyberNinja",
            "level": 19,
            "game": "Tic-Tac-Toe",
            "score": 6210,
        },
        {
            "rank": 5,
            "username": "Dragon",
            "level": 17,
            "game": "Memory Match",
            "score": 5580,
        },
    ]

    return {
        "message": "GameZone data reset successfully",
    }