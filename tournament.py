class Player:
    def __init__(self, pid, name):
        self.id = pid
        self.name = name
        self.score = 0
        self.played = set()


# -------- SWISS SYSTEM --------
def swiss_pairing(players, rounds):

    for r in range(1, rounds + 1):

        print("\n===== ROUND", r, "=====")

        # Merge Sort Equivalent (Python built-in stable sort)
        players.sort(key=lambda x: (-x.score, x.id))

        used = set()
        pairings = []

        for i in range(len(players)):
            if players[i].id in used:
                continue

            for j in range(i + 1, len(players)):
                if players[j].id not in used and \
                   players[j].id not in players[i].played:

                    pairings.append((players[i], players[j]))

                    players[i].played.add(players[j].id)
                    players[j].played.add(players[i].id)

                    used.add(players[i].id)
                    used.add(players[j].id)
                    break

        # Bye Handling
        for p in players:
            if p.id not in used:
                print(p.name, "gets a BYE (+1 point)")
                p.score += 1

        print("\nMatch Pairings:")

        for a, b in pairings:
            print(a.name, "vs", b.name)

        print("\nEnter updated scores")

        for p in players:
            s = float(input("Score of " + p.name + ": "))
            p.score = s

    print("\nFINAL STANDINGS")

    players.sort(key=lambda x: -x.score)

    for p in players:
        print(p.name, "Score:", p.score)


# -------- ROUND ROBIN --------
def round_robin(players):

    n = len(players)

    print("\nROUND ROBIN SCHEDULE\n")

    for i in range(n):
        for j in range(i + 1, n):
            print(players[i].name, "vs", players[j].name)


# -------- KNOCKOUT --------
def knockout(players):

    round_no = 1

    while len(players) > 1:

        print("\n===== ROUND", round_no, "=====")

        winners = []

        for i in range(0, len(players), 2):

            if i + 1 >= len(players):
                print(players[i].name, "gets BYE")
                winners.append(players[i])
                continue

            a = players[i]
            b = players[i + 1]

            print(a.name, "vs", b.name)

            w = input("Winner name: ")

            if w == a.name:
                winners.append(a)
            else:
                winners.append(b)

        players = winners
        round_no += 1

    print("\nChampion is:", players[0].name)


# -------- MAIN --------

print("HYBRID CHESS TOURNAMENT SYSTEM")

mode = input(
"Choose Mode (Swiss / RoundRobin / Knockout): ").lower()

n = int(input("Number of Players: "))

players = []

for i in range(n):
    name = input("Player Name: ")
    players.append(Player(i, name))


if mode == "swiss":

    rounds = int(input("Number of Rounds: "))
    swiss_pairing(players, rounds)

elif mode == "roundrobin":

    round_robin(players)

elif mode == "knockout":

    knockout(players)

else:
    print("Invalid Mode")
