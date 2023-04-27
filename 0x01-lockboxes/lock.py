#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Given a list of boxes containing keys to other boxes, this function
    returns True if all boxes can be opened, starting from box 0. Otherwise
    it returns False.

    Args:
    - boxes (list of lists of integers): A list of boxes, where each box is
        represented as a list of integers representing the keys to other boxes.

    Returns:
    - bool: True if all boxes can be opened starting from box 0, False otherwise.
    """
    # Initialize variables
    n = len(boxes) # Number of boxes
    keys = [0] + boxes[0] # List of keys available, starting with box 0
    unlocked = set(keys) # Set of unlocked boxes
    
    # Continue unlocking boxes as long as there are keys to try
    while keys:
        key = keys.pop() # Get the last key in the list
        for box in boxes[key]:
            # Check if the box exists and is not already unlocked
            if box < n and box not in unlocked:
                unlocked.add(box) # Add the box to the set of unlocked boxes
                keys.append(box) # Add the keys from the new box to the list of keys
    
    # Check if all boxes were unlocked
    return len(unlocked) == n
