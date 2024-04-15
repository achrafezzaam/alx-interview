#!/usr/bin/python3
''' This program checks if a set of boxes can be opened '''


def canUnlockAll(boxes):
    ''' Check if the content of the opened boxes could allow us
        to open all the boxes

        Args:
            boxes (List of Lists): The boxes to check

        Return: True if all the boxes can be opened and False if not
    '''
    key_list = [0]
    for key in key_list:
        for new_key in boxes[key]:
            if (new_key not in key_list and new_key < len(boxes)):
                key_list.append(new_key)

    if (len(key_list) == len(boxes)):
        return True
    return False
