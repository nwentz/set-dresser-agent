# Set dresser — rules for the agent

This folder is a Maya tool. Read this before touching anything.

## The app
- Maya 2026 (2027 is fine too). Python 3, `import maya.cmds as cmds`. No pymel.
- Scripts live in `maya_scripts/` folder.
- Import them with: `import sys; sys.path.append('maya_scripts'); import set_dresser`

## How to run your work
- Live, inside your open Maya:
  ```python
  import sys
  sys.path.append('maya_scripts')
  import set_dresser
  set_dresser.scatter(10, 4)
  ```

- Using the UI window:
  ```python
  import sys
  sys.path.append('maya_scripts')
  import set_dresser_ui
  set_dresser_ui.create_ui()
  ```

## Rules of the tool
- The engine (`maya_scripts/set_dresser.py`) has no UI in it. The window (`maya_scripts/set_dresser_ui.py`) only reads controls and calls the engine.
- One function per thing it makes: `make_rock`, `make_tree`. One function per rule: `is_clear`.
- Everything scatter makes goes under a group (`rocks`, `trees`). Clear deletes the groups and nothing else. Never `select(all=True)`, never delete by wildcard.
- One scatter = one undo step (`cmds.undoInfo(openChunk=True)` … `closeChunk=True` in a `try/finally`).
- Errors the artist sees are one sentence (`cmds.warning`), not a traceback.
- Keep the names: `rock`, `tree`, `trunk`, `canopy`, `ground`, `path`, `pond`.

## Before you say it's done
- Tell me your plan before you touch anything.
- Run it. Say what appeared and how many.
- Commit after each working step.
