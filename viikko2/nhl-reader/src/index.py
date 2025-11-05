from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    season = Prompt.ask("Season", default="2024-25", choices=["2018-19", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26"])

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    while True:
        nationality = Prompt.ask("Nationality", default="", choices=["USA", "FIN", "CAN", "SWE", "CZE", "RUS", "SLO", "FRA", "GBR", "SVK", "DEN", "NED", "AUT", "BLR", "GER", "SUI", "NOR", "UZB", "LAT", "AUS"])
 
        if not nationality:
            break
        
        table = Table(title=f"[italic]Season {season} players from {nationality}")
        table.add_column("Player", style="cyan")
        table.add_column("teams", style="magenta")
        table.add_column("goals", justify="right", style="green")
        table.add_column("assists", justify="right", style="green")
        table.add_column("points", justify="right", style="green")
        for p in stats.top_scorers_by_nationality(nationality):
            table.add_row(p.name, p.team, str(p.goals), str(p.assists), str(p.goals+p.assists))

        console = Console()
        console.print(table)

if __name__ == "__main__":
    main()