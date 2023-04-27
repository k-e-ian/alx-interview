#!/usr/bin/python3
'''
0-lockboxes.py
'''


def canUnlockAll(boxes):
    '''
    method that determines if all the boxes can be opened.
    '''
    # Initialize variables

    # Set of keys that have been found
    found_keys = set([0])

    # Stack of boxes to be opened
    boxes_to_open = [0]

    # Continue opening boxes as long as there are boxes to be opened
    while boxes_to_open:
        # Get the keys from the current box
        box_to_open = boxes_to_open.pop()
        keys = boxes[box_to_open]

        # Iterate through the keys
        for key in keys:
            # Check if the key has not been found
            if key not in found_keys:
                # Add the key to the set of found keys
                found_keys.add(key)
                # Add the box to the stack of boxes to be opened
                boxes_to_open.append(key)
    # Check if all boxes were opened
    return len(found_keys) == len(boxes)
