from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="GameZone API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------
# Temporary data
# -------------------------

games = [
    {
        "id": 1,
        "name": "Snake",
        "category": "Arcade",
        "description": "Classic snake game. Eat the food and grow!",
        "icon": "🐍",
    },
    {
        "id": 2,
        "name": "Tic-Tac-Toe",
        "category": "Strategy",
        "description": "Beat your opponent in the classic 3x3 battle.",
        "icon": "⭕",
    },
    {
        "id": 3,
        "name": "Memory Match",
        "category": "Puzzle",
        "description": "Find all matching pairs as quickly as possible.",
        "icon": "🧠",
    },
]

leaderboard = [
    {"rank": 1, "username": "ShadowX", "score": 9850, "level": 25},
    {"rank": 2, "username": "NightWolf", "score": 8720, "level": 22},
    {"rank": 3, "username": "CyberAce", "score": 7640, "level": 19},
    {"rank": 4, "username": "DragonPro", "score": 6930, "level": 17},
    {"rank": 5, "username": "PixelKing", "score": 5840, "level": 15},
]

player = {
    "username": "PlayerOne",
    "level": 8,
    "xp": 1240,
    "games_played": 42,
    "wins": 27,
    "achievements": [
        "First Win",
        "Game Master",
        "High Scorer",
    ],
}


class Score(BaseModel):
    username: str
    score: int
    game: str


# -------------------------
# API
# -------------------------

@app.get("/")
def root():
    return {
        "message": "GameZone API is running!"
    }


@app.get("/api/games")
def get_games():
    return games


@app.get("/api/games/{game_id}")
def get_game(game_id: int):

    for game in games:
        if game["id"] == game_id:
            return game

    return {
        "error": "Game not found"
    }


@app.get("/api/leaderboard")
def get_leaderboard():
    return leaderboard


@app.get("/api/player")
def get_player():
    return player


@app.post("/api/scores")
def submit_score(score: Score):

    leaderboard.append({
        "rank": len(leaderboard) + 1,
        "username": score.username,
        "score": score.score,
        "level": 1,
    })

    leaderboard.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    for index, item in enumerate(leaderboard):
        item["rank"] = index + 1

    return {
        "message": "Score submitted",
        "score": score.score
    }