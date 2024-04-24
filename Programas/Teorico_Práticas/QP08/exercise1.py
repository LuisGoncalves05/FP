def move_tower(height, from_pole, to_pole, with_pole, count):
    """A recursive function to move a tower of given height >= 1"""
    if height > 1:
        # we are in the recursive case
        # move height-1 disks from source to auxiliary, so they are out of the way
        count = move_tower(height-1, from_pole, with_pole, to_pole, count)
        # move the top disk from source to target
        count = move_disk(from_pole, to_pole, count)
        # move the n-1 disks that we left on auxiliary onto target
        count = move_tower(height-1, with_pole, to_pole, from_pole, count)
    else:
        # otherwise, were are in the base case:
        # move a single disc
        count = move_disk(from_pole, to_pole, count)
    return count

def move_disk(from_pole, to_pole, count):
    """An auxiliar function to print a single move instruction."""
    print(f"{count}. Move disk from", from_pole, "to", to_pole)
    return count + 1

