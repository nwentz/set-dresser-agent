#!/usr/bin/env python3
"""Set dresser engine - creates rocks and trees in Maya."""

# Maya's command module - I use Maya's built-in commands to create objects
import maya.cmds as cmds
# Python's built-in random module - I added this to generate random numbers
import random

# Settings for the set dresser
path_width = 4          # Width of the path running through the scene
path_buffer = 1         # Extra space to keep away from the path edges


# I defined this function to create a single rock with a specific position and rotation
def make_rock(position=None, rotation=None):
    """Create a rock at the given position/rotation."""
    if position is None:
        position = [0, 0, 0]
    if rotation is None:
        rotation = [0, 0, 0]

    # Create a simple rock geometry
    rock = cmds.polySphere(radius=0.8, name='rock#')
    cmds.xform(rock, translation=position, rotation=rotation)
    cmds.makeIdentity(rock, apply=True, translate=1, rotate=1, scale=1)

    return rock


def make_tree(position=None, rotation=None):
    """Create a tree at the given position/rotation."""
    if position is None:
        position = [0, 0, 0]
    if rotation is None:
        rotation = [0, 0, 0]

    # Create trunk
    trunk = cmds.polyCylinder(radius=0.2, height=4, name='tree#_trunk')
    cmds.xform(trunk, translation=position, rotation=rotation)
    cmds.makeIdentity(trunk, apply=True, translate=1, rotate=1, scale=1)

    # Create canopy
    canopy = cmds.polySphere(radius=1.5, name='tree#_canopy')
    canopy_translation = [position[0], position[1] + 2.5, position[2]]
    cmds.xform(canopy, translation=canopy_translation, rotation=rotation)
    cmds.makeIdentity(canopy, apply=True, translate=1, rotate=1, scale=1)

    return trunk[0]


def is_clear(position, path_clear=True, pond_clear=True):
    """Check if a position is valid (not on path or in pond)."""
    x, y, z = position

    # Check if in path (4-wide along Z through middle)
    # I added this if-statement to check if we should avoid the path
    if path_clear:
        center_x = 0  # Path goes through x=0
        # Keep everything at least path_buffer units back from the path edges
        if abs(x - center_x) < (path_width / 2) + path_buffer:
            return False

    # Check if in pond (radius 6 at x=10, z=10)
    if pond_clear:
        pond_x = 10
        pond_z = 10
        pond_radius = 6
        distance = ((x - pond_x) ** 2 + (z - pond_z) ** 2) ** 0.5
        if distance < pond_radius:
            return False

    return True


def scatter(rock_count=10, tree_count=4, area=40, seed=0, path_clear=True, pond_clear=True):
    """Scatter rocks and trees across the ground plane."""
    # Set the random seed for reproducibility
    random.seed(seed)

    # Create groups
    rocks_group = cmds.group(name='rocks', empty=True)
    trees_group = cmds.group(name='trees', empty=True)

    # Create ground plane
    ground = cmds.polyPlane(width=area, height=area, name='ground')
    cmds.xform(ground, translation=[0, -0.5, 0])

    # Scatter rocks
    # I added this for-loop to place each rock in sequence
    for i in range(rock_count):
        # Find valid position
        max_attempts = 100
        for attempt in range(max_attempts):
            x = random.uniform(-area/2, area/2)
            z = random.uniform(-area/2, area/2)
            y = 0

            if is_clear([x, y, z], path_clear, pond_clear):
                position = [x, y, z]
                rotation = [0, random.uniform(0, 360), 0]

                rock = make_rock(position, rotation)
                cmds.parent(rock, rocks_group)
                break

    # Scatter trees
    for i in range(tree_count):
        # Find valid position
        max_attempts = 100
        for attempt in range(max_attempts):
            x = random.uniform(-area/2, area/2)
            z = random.uniform(-area/2, area/2)
            y = 0

            if is_clear([x, y, z], path_clear, pond_clear):
                position = [x, y, z]
                rotation = [0, random.uniform(0, 360), 0]

                make_tree(position, rotation)
                cmds.parent(make_tree(position, rotation), trees_group)
                break

    cmds.warning(f'Done! Created {rock_count} rocks and {tree_count} trees.')


def clear():
    """Clear the scene, deleting only rocks and trees groups."""
    try:
        cmds.delete('rocks', 'trees', ignorePanel=True)
        cmds.warning('Cleared rocks and trees.')
    except Exception:
        cmds.warning('Nothing to clear.')
