import sys


blocks = [
    {
        "gym": False,
        "school": False,
        "store": True,
        "office": False,
    },
    {
        "gym": False,
        "school": True,
        "store": False,
        "office": False,
    },
    {
        "gym": False,
        "school": True,
        "store": False,
        "office": False,
    },
    {
        "gym": True,
        "school": False,
        "store": True,
        "office": False,
    },
    {
        "gym": False,
        "school": False,
        "store": False,
        "office": True,
    },
    {
        "gym": True,
        "school": False,
        "store": False,
        "office": False,
    }
]
facilities = ["store", "school", "office"]


def check_facility_distance(selected_index, facility):
    facility_distance = sys.maxsize
    for index, block in enumerate(blocks):
        if not block[facility]: continue
        
        distance = abs(selected_index - index)
        if distance == 0: return distance
        if facility_distance > distance: 
            facility_distance = distance
    
    return facility_distance


def main():
    chosen_block_distance = {
        'index': None,
        'distance': sys.maxsize
    }

    for block_idx, _ in enumerate(blocks):
        block_max_distance = -sys.maxsize
        for facility in facilities:
            distance = check_facility_distance(block_idx, facility)
            if distance > block_max_distance:
                block_max_distance = distance
        
        if chosen_block_distance['distance'] > block_max_distance:
            chosen_block_distance = { 
                'index': block_idx, 
                'distance': block_max_distance 
            }

    print(blocks[chosen_block_distance['index']])


if __name__ == "__main__":
    main()