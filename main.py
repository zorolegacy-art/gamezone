from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="GameZone API")


# Allow React frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------
# GAME DATA
# -------------------------

games = [
    {
        "id": 1,
        "name": "Snake",
        "category": "Arcade",
        "description": "Classic Snake game",
        "icon": "🐍",
    },
    {
        "id": 2,
        "name": "Tic-Tac-Toe",
        "category": "Strategy",
        "description": "Classic 3x3 battle",
        "icon": "⭕",
    },
    {
        "id": 3,
        "name": "Memory Match",
        "category": "Puzzle",
        "description": "Find matching pairs",
        "icon": "🧠",
    },
]


# -------------------------
# PLAYER DATA
# -------------------------

player = {
    "username": "GameMaster",
    "level": 12,
    "xp": 8450,
    "games_played": 127,
    "wins": 84,
    "achievements": [
        "First Victory",
        "Snake Master",
        "100 Games",
        "High Scorer",
    ],
}


# -------------------------
# LEADERBOARD DATA
# -------------------------

leaderboard = [
    {
        "rank": 1,
        "username": "ShadowX",
        "level": 42,
        "score": 98250,
    },
    {
        "rank": 2,
        "username": "DragonSlayer",
        "level": 38,
        "score": 87400,
    },
    {
        "rank": 3,
        "username": "GameMaster",
        "level": 12,
        "score": 84500,
    },
    {
        "rank": 4,
        "username": "NightWolf",
        "level": 31,
        "score": 76900,
    },
    {
        "rank": 5,
        "username": "CyberGhost",
        "level": 27,
        "score": 71200,
    },
]


# -------------------------
# HOME API
# -------------------------

@app.get("/")
def root():
    return {
        "message": "GameZone API is running!"
    }


# -------------------------
# ALL GAMES
# -------------------------

@app.get("/api/games")
def get_games():
    return games


# -------------------------
# SINGLE GAME
# -------------------------

@app.get("/api/games/{game_id}")
def get_game(game_id: int):

    for game in games:
        if game["id"] == game_id:
            return game

    return {
        "error": "Game not found"
    }


# -------------------------
# LEADERBOARD
# -------------------------

@app.get("/api/leaderboard")
def get_leaderboard():
    return leaderboard


# -------------------------
# PLAYER PROFILE
# -------------------------

@app.get("/api/player")
def get_player():
    return player