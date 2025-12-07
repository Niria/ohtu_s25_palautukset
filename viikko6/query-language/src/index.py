from statistics import Statistics
from player_reader import PlayerReader
from matchers import All, And, HasAtLeast, HasFewerThan, Not, Or, PlaysIn
from query_builder import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    # matcher = And(
    #     HasAtLeast(5, "goals"),
    #     HasAtLeast(20, "assists"),
    #     PlaysIn("PHI")
    # )

    # matcher = And(
    #     Not(HasAtLeast(2, "goals")),
    #     PlaysIn("NYR")
    # )

    # matcher = And(
    #     HasFewerThan(2, "goals"),
    #     PlaysIn("NYR")
    # )


    # filtered_with_all = stats.matches(All())
    # print(len(filtered_with_all))

    # matcher = Or(
    #     HasAtLeast(45, "goals"),
    #     HasAtLeast(70, "assists")
    # )

    # matcher = And(
    #     HasAtLeast(70, "points"),
    #     Or(
    #         PlaysIn("COL"),
    #         PlaysIn("FLA"),
    #         PlaysIn("BOS")
    #     )
    # )

    query = QueryBuilder()

    # matcher = query.build()
    # matcher = query.plays_in("NYR").build()

    # matcher = (
    #     query
    #     .plays_in("NYR")
    #     .has_at_least(10, "goals")
    #     .has_fewer_than(20, "goals")
    #     .build()
    #     )
    
    matcher = (
        query
            .one_of(
                query.plays_in("PHI")
                     .has_at_least(10, "assists")
                     .has_fewer_than(10, "goals"),
                query.plays_in("EDM")
                     .has_at_least(50, "points")
            )
            .build()
    )

    for player in stats.matches(matcher):
        print(player)



if __name__ == "__main__":
    main()
