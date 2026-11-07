# Set Dresser Agent - Project Brief

## What the tool does
Scatters rocks and trees across a 40x40 ground plane while avoiding obstacles:
- Rocks and trees scattered randomly across the ground
- Path avoidance: 4-wide path along Z axis through the middle (keeps objects off it)
- Pond avoidance: Round pond radius 6 centered at x=10, z=10 (keeps objects out of it)

UI Requirements:
- Window with sliders for:
  - Rock count
  - Tree count
  - Area (to control scatter area size)
- Checkbox for "Keep path and pond clear"
- Scatter button (creates the scene)
- Clear button (deletes created elements)

## Who uses it
A set dresser who will **never open the code**. The user needs a simple, intuitive UI to quickly populate an environment with rocks and trees without needing to understand Python or Maya scripting.

## What it has to get right

### Functional Requirements
1. **One function per thing it makes**: `make_rock()` and `make_tree()`
2. **One function for the rules**: `is_clear()` - checks if a position is valid (not in path or pond)
3. **Everything under group per kind**: All rocks under `rocks` group, all trees under `trees` group
4. **Clear deletes only those groups**: `cmds.delete('rocks')` and `cmds.delete('trees')` only
5. **One scatter = one undo**: Use `cmds.undoInfo(openChunk=True)` and `closeChunk(True)` in a try/finally block
6. **Window only reads controls**: The UI reads slider values and button states, then calls the engine

### Technical Requirements
- Maya 2026 (2027 is fine)
- Python 3, `import maya.cmds as cmds`
- No pymel
- No UI in engine code (`set_dresser.py`)
- Keep specific naming: `rock`, `tree`, `trunk`, `canopy`, `ground`, `path`, `pond`

### Error Handling
- Errors shown as one-sentence `cmds.warning()` messages
- No tracebacks exposed to user

## Implementation Plan
1. Create `set_dresser.py` - The engine with core functions (`make_rock`, `make_tree`, `is_clear`, `scatter`, `clear`)
2. Create `set_dresser_ui.py` - The UI window that reads controls and calls engine
3. Ensure everything goes under proper groups (`rocks`, `trees`)
4. Implement undo properly in scatter function
5. Test with Maya command port and headless mode
