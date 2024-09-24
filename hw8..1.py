# start
players: list[float] = []
sum_players: float = 0.0
tallest_player: float = None
shortest_player: float = None
taller_than_two: int = 0

while True:
    height: float = float(input("Enter the player's height:"))

    if height == -999:
        break

    if height < 1.60 or height > 3.00:
        continue

    players.append(height)

    sum_players += height

    if tallest_player is None or height > tallest_player:
        tallest_player = height
    if shortest_player is None or height < shortest_player:
        shortest_player = height

    if height > 2.0:
        taller_than_two += 1


if players:
    average_height: float = sum_players / len(players)

    
    taller_than_average: int = sum(1 for h in players if h > average_height)


    print(f"\nNumber of players included in the sample: {len(players)}")
    print(f"Height of the tallest player: {tallest_player:.2f} meters")
    print(f"Height of the shortest player: {shortest_player:.2f} meters")
    print(f"Average height of all players: {average_height:.2f} meters")
    print(f"Number of players taller than 2.0 meters: {taller_than_two}")
    print(f"Number of players taller than average: {taller_than_average}")
else:
    print("No valid heights were entered.")
