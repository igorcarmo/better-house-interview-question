# Better House
This is the implementation to this question:
You have to choose the minimum farthest distance to facilities near houses you are prospecting to live. 
Each block appears in a sequence (as a street) and has a distance of 1 to its neighbors blocks.

## Inputs
You have 2 inputs:

1 - A list of objects representing the blocks where the houses are located. This object has as keys the names of
possible facilities and has booleans as its values, representing the presence of the facility on the block.
Ex:
[
    {
        "gym": true,
        "school": false,
        "store": false,
    },
    {
        "gym": false,
        "school": true,
        "store": false,
    }
]

2 - A list of facilities prioritized by the prospector
Ex: ["gym", "school"]

## Outputs
The output had to be the block that has the minimum farthest distance to the given facilities.
{
    "gym": false,
    "school": true,
    "store": false,
}