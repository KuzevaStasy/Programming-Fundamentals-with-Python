# Read queue from terminal (space-separated)
queue = input().split(", ")

# Find the wolf's position
wolf_index = queue.index("wolf")
position_from_front = len(queue) - wolf_index - 1

# Check if wolf is closest to you (front of the queue)
if wolf_index == len(queue) - 1:
    print("Please go away and stop eating my sheep")
else:
    # Sheep in danger is one ahead of the wolf (from the front’s perspective)
    sheep_number = len(queue) - wolf_index - 1
    print(f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!")