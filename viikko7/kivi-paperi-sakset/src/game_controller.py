from tuomari import Tuomari
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu


class GameController:
    """Manages a game session with win condition and game state."""

    WIN_TARGET = 3

    def __init__(self, mode: str):
        """Initialize a new game.
        
        Args:
            mode: Game mode - 'human', 'ai', or 'ai_plus'
        """
        self.mode = mode
        self.tuomari = Tuomari()
        self.history = []
        self.ended = False
        self.message = ""
        
        if mode == "ai":
            self.ai = Tekoaly()
        elif mode == "ai_plus":
            self.ai = TekoalyParannettu()
        else:
            self.ai = None

    def _valid_move(self, move: str) -> bool:
        """Check if a move is valid."""
        return move in {"k", "p", "s"}

    def stop(self, reason: str = "Peli lopetettu.") -> None:
        """End the game with a message."""
        self.ended = True
        self.message = reason

    def _check_win_condition(self) -> None:
        """Check if either player has reached the win target."""
        if self.tuomari.ekan_pisteet >= self.WIN_TARGET:
            self.stop(f"Peli päättyi! Pelaaja 1 voitti {self.WIN_TARGET} peliin.")
        elif self.tuomari.tokan_pisteet >= self.WIN_TARGET:
            self.stop(f"Peli päättyi! Pelaaja 2 voitti {self.WIN_TARGET} peliin.")

    def play_round(self, player_one_move: str, player_two_move: str | None = None) -> str | None:
        """Play a single round.
        
        Args:
            player_one_move: Move by player 1 (k, p, or s)
            player_two_move: Move by player 2 (required for human mode)
            
        Returns:
            The opponent's move, or None if game ended or invalid input.
        """
        self.message = ""

        if self.ended:
            self.message = "Peli on jo päättynyt. Aloita uusi peli jatkaaksesi."
            return None

        if not self._valid_move(player_one_move):
            self.stop("Virheellinen siirto lopetti pelin.")
            return None

        if self.mode == "human":
            if not self._valid_move(player_two_move):
                self.stop("Virheellinen siirto lopetti pelin.")
                return None
            opponent_move = player_two_move
        else:
            opponent_move = self.ai.anna_siirto()

        self.tuomari.kirjaa_siirto(player_one_move, opponent_move)

        # TekoalyParannettu learns from previous moves
        if self.ai and hasattr(self.ai, "aseta_siirto"):
            self.ai.aseta_siirto(player_one_move)

        self.history.append((player_one_move, opponent_move))
        self._check_win_condition()

        return opponent_move

    def scoreboard(self) -> str:
        """Get the current scoreboard."""
        return str(self.tuomari)

    def summary(self) -> dict:
        """Get a summary of the game state."""
        return {
            "player_one": self.tuomari.ekan_pisteet,
            "player_two": self.tuomari.tokan_pisteet,
            "ties": self.tuomari.tasapelit,
            "rounds": len(self.history),
        }
