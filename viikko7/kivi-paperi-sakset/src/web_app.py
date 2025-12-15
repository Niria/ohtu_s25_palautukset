import os
from pathlib import Path
from uuid import uuid4

from flask import Flask, redirect, render_template, request, session, url_for

from game_controller import GameController

# Set up Flask with template directory
BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__, template_folder=BASE_DIR / "templates")
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret-key")

_games = {}


def _get_game() -> GameController | None:
    game_id = session.get("game_id")
    if game_id and game_id in _games:
        return _games[game_id]
    return None


@app.route("/", methods=["GET"])
def home():
    game = _get_game()
    return render_template("index.html", game=game)


@app.post("/start")
def start_game():
    mode = request.form.get("mode", "")
    if mode not in {"human", "ai", "ai_plus"}:
        return redirect(url_for("home"))

    game_id = str(uuid4())
    _games[game_id] = GameController(mode)
    session["game_id"] = game_id
    return redirect(url_for("play"))


@app.route("/play", methods=["GET", "POST"])
def play():
    game = _get_game()
    if not game:
        return redirect(url_for("home"))

    if request.method == "POST":
        action = request.form.get("action", "play")
        if action == "end":
            game.stop()
            return redirect(url_for("play"))

        player_one_move = request.form.get("p1_move", "").strip().lower()
        player_two_move = request.form.get("p2_move", "").strip().lower() if game.mode == "human" else None
        opponent_move = game.play_round(player_one_move, player_two_move)

        if opponent_move and game.mode != "human":
            game.message = f"Tietokone valitsi: {opponent_move}"

        return redirect(url_for("play"))

    return render_template("index.html", game=game)


@app.post("/reset")
def reset():
    game_id = session.pop("game_id", None)
    if game_id and game_id in _games:
        _games.pop(game_id, None)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
