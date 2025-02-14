# Understand the Problem

"""
You have a number of building blocks that can be used to build a valid
structure. There are certain rules about what determines a valid structure:

- The building blocks are cubes.
- The structure is built in layers.
- The top layer is a single block.
- A block in an upper layer must be supported by four blocks in a lower layer.
- A block in a lower layer can support more than one block in an upper layer.
- You cannot leave gaps between blocks.

Write a program that, given the number of available blocks, calculates
the number of blocks left over after building the tallest possible
valid structure.

Tasks
You are provided with the problem description above. Your tasks for this step are:

- Make notes of your mental model for the problem, including:
-- inputs and outputs.
-- explicit and implicit rules.
- Write a list of clarifying questions for anything that isn't clear.
"""

# input: integer of available blocks
# output: integer of leftover blocks (after building the tallest possible valid structure)
# rules:
#   - explicit:
#       - Structures are built with blocks
#           - Blocks are cubes
#           - Cubes are six-sided, have square faces, and have equal lengths on all sides
#       - A block in an upper layer must be suppoorted by 4 blocks in a lower layer
#       - Blocks in lower layers can support multiple blocks in upper layers
#       - No gaps between blocks are allowed
#   - implicit:
#       - Number of blocks in a layer is that layer number squared
# questions:
#
#
# structure:
#   1 block
#   4 blocks
#   9 blocks
#   16 blocks
