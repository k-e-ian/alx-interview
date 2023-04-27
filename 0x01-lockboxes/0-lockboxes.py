#!/usr/bin/python3
'''
0-lockboxes.py
'''


def canUnlockAll(boxes):
    '''
    method that determines if all the boxes can be opened.
    '''
    # set to store the keys that have been found
    found_keys = set([0])
    # stack of boxes to be opened
    boxes_to_open = [0]

    # iterate through the boxes to be opened
    while boxes_to_open:
        # get the keys from the current box
        keys = boxes[boxes_to_open.pop()]

        # iterate through the keys
        for key in keys:
            # check if the key has not been found
            if key not in found_keys:
                # add the key to the set of found keys
                found_keys.add(key)
                # add the box to the stack of boxes to be opened
                boxes_to_open.append(key)

    # check if all the boxes have been opened
    return len(found_keys) == len(boxes)
