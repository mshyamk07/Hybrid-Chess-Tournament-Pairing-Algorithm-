# Hybrid Chess Tournament Pairing System

A Python-based system that implements three different tournament formats for chess and game competitions: Swiss System, Round Robin, and Knockout (Single Elimination).

## Features

### 1. **Swiss System**
- Players are ranked by score, then paired with the highest-ranked opponents they haven't played yet
- Automatically handles bye assignments for unpaired players
- Updates scores round by round
- Ideal for tournaments with moderate number of players

### 2. **Round Robin**
- Every player plays every other player exactly once
- Generates a complete schedule of all possible pairings
- Best for smaller tournaments where comprehensive comparison is needed

### 3. **Knockout (Single Elimination)**
- Players are paired and winners advance to the next round
- Continues until one champion remains
- Includes bye handling for odd player counts

## Usage

### Basic Installation
No external dependencies required. Just Python 3.x

### Running the Program

```bash
python tournament.py
```

### Interactive Prompts

1. **Choose Tournament Mode**: Enter one of:
   - `swiss` - Swiss System
   - `roundrobin` - Round Robin
   - `knockout` - Knockout

2. **Number of Players**: Enter the total number of players

3. **Player Names**: Enter each player's name when prompted

4. **Additional Configuration**:
   - For Swiss System: Enter the number of rounds

5. **Score Input**: 
   - For Swiss: After each round, input the score for each player
   - For Knockout: After each match, enter the winner's name

## Example Session

```
HYBRID CHESS TOURNAMENT SYSTEM
Choose Mode (Swiss / RoundRobin / Knockout): swiss
Number of Players: 4
Player Name: Alice
Player Name: Bob
Player Name: Charlie
Player Name: Diana
Number of Rounds: 2

===== ROUND 1 =====

Match Pairings:
Alice vs Bob
Charlie vs Diana

Enter updated scores
Score of Alice: 1
Score of Bob: 0
Score of Charlie: 1
Score of Diana: 0

===== ROUND 2 =====
[continues...]

FINAL STANDINGS
Charlie Score: 2.0
Alice Score: 1.0
Diana Score: 0.0
Bob Score: 0.0
```

## Data Structure

### Player Class
```python
class Player:
    id          # Unique player identifier
    name        # Player name
    score       # Current score
    played      # Set of opponent IDs already played
```

## Algorithm Details

### Swiss Pairing Algorithm
1. Sort players by score (descending) and ID (ascending for tie-breaking)
2. Iterate through sorted players
3. For each unpaired player, find the highest-ranked opponent they haven't played
4. Mark both players as used and record pairing
5. Assign byes to any remaining unpaired players

**Time Complexity**: O(r × n²) where r = rounds, n = number of players

### Round Robin
- Generates all combinations of player pairings
- Time Complexity: O(n²)

### Knockout
- Single elimination bracket
- Time Complexity: O(n)

## Recommendations for Enhancement

- Add persistent data storage (JSON/CSV) for tournament history
- Implement advanced tie-breaking rules for Swiss system
- Add input validation for player counts and scores
- Create a GUI for better user experience
- Add support for double elimination tournaments
- Implement ELO rating system integration
- Add tournament scheduling to avoid conflicts
- Create automated score tracking from game results

## Requirements

- Python 3.6+
- No external libraries required

## License

Open source

## Contributing

Feel free to fork, modify, and submit improvements!
