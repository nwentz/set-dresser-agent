#!/usr/bin/env python3
"""Set dresser UI - window that reads controls and calls the engine."""

import maya.cmds as cmds


def create_ui():
    """Create and show the set dresser UI window."""
    window_name = 'setDresserWindow'
    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name)

    window = cmds.window(
        window_name,
        title='Set Dresser',
        widthHeight=(300, 250),
        menuBar=False
    )

    main_layout = cmds.columnLayout(adjustableColumn=True, rowSpacing=10)

    # Title
    cmds.text(label='Set Dresser', font='boldLabelFont', height=30)

    # Rock count slider
    cmds.text(label='Rock Count:', align='left')
    rock_slider = cmds.intSlider(min=0, max=50, value=10, step=1)

    # Tree count slider
    cmds.text(label='Tree Count:', align='left')
    tree_slider = cmds.intSlider(min=0, max=20, value=4, step=1)

    # Area slider
    cmds.text(label='Area Size:', align='left')
    area_slider = cmds.intSlider(min=20, max=80, value=40, step=1)

    # Seed slider
    cmds.text(label='Seed:', align='left')
    seed_slider = cmds.intSlider(min=0, max=100000, value=0, step=1)

    # Clear path/pond checkbox
    cmds.checkBox(label='Keep path and pond clear', value=True)

    # Buttons
    button_layout = cmds.rowColumnLayout(numberOfColumns=2, columnSpacing=[1, 10])

    cmds.button(
        label='Scatter',
        width=100,
        command=lambda x: scatter_from_ui(
            rock_count=cmds.intSlider(rock_slider, query=True, value=True),
            tree_count=cmds.intSlider(tree_slider, query=True, value=True),
            area=cmds.intSlider(area_slider, query=True, value=True),
            seed=cmds.intSlider(seed_slider, query=True, value=True),
            path_clear=cmds.checkBox(query=True, value=True)
        )
    )

    cmds.button(
        label='Clear',
        width=100,
        command=lambda x: clear_from_ui()
    )

    cmds.showWindow(window)


def scatter_from_ui(rock_count, tree_count, area, seed, path_clear):
    """Get values from UI and call scatter function."""
    import set_dresser
    set_dresser.scatter(rock_count, tree_count, area, seed, path_clear, True)


def clear_from_ui():
    """Get values from UI and call clear function."""
    import set_dresser
    set_dresser.clear()


if __name__ == '__main__':
    create_ui()
