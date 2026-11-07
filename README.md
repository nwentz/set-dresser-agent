# Set Dresser - Maya Tool

A Maya script that scatters rocks and trees across a ground plane while avoiding obstacles (paths and ponds) with a reproducible seed system.

## What it does

Scatters rocks and trees on a customizable ground plane while:
- **Avoiding a central path** (4 units wide along the Z-axis through x=0)
- **Avoiding a circular pond** (radius 6, center at x=10, z=10)
- **Using a seed system** for reproducible, director-friendly results

## Requirements

- **Maya 2026** or newer
- **Python 3** (included with Maya)
- `maya.cmds` module (built into Maya)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/nwentz/set-dresser-agent.git
   ```

2. Navigate to the repository and copy the `maya_scripts/` folder to your Maya scripts directory:
   - On macOS/Linux: `~/maya/2027/scripts`
   - On Windows: `C:\Users\[username]\Documents\maya\2027\scripts`

3. Verify the files are in place:
   - `maya_scripts/set_dresser.py`
   - `maya_scripts/set_dresser_ui.py`

## How to run

### Method 1: Command Line (No UI)

```bash
# Set up Python path
cd set-dresser-agent

# In Maya's Script Editor (Python tab):
import sys
sys.path.append('maya_scripts')
import set_dresser

# Scatter rocks and trees
set_dresser.scatter(rock_count=10, tree_count=4, area=40, seed=12)

# Clear the scene
set_dresser.clear()
```

### Method 2: Using the UI

```bash
# In Maya's Script Editor (Python tab):
import sys
sys.path.append('maya_scripts')
import set_dresser_ui

# Create and show the UI
set_dresser_ui.create_ui()

# Then adjust sliders and click Scatter
```

## Two lines that make it work

### Line 1 (reproducibility):
```python
random.seed(seed)
```

**Purpose:** Initializes the random number generator with the specified seed value, ensuring identical results every time the same seed is used.

### Line 2 (UI integration):
```python
seed=cmds.intSlider(seed_slider, query=True, value=True)
```

**Purpose:** Exposes the seed value through the UI and passes it to the scatter function for reproducible placement.

## Features

- **Seed System:** Same seed + same settings = identical results (perfect for directors)
- **Obstacle Avoidance:** Automatically avoids path and pond areas
- **Configurable:** Adjust rock count, tree count, area size, and seed
- **Grouped Output:** All rocks under `rocks` group, all trees under `trees` group
- **One-Click Clear:** Deletes only the created groups (preserves other scene content)

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `rock_count` | int | 10 | Number of rocks to scatter |
| `tree_count` | int | 4 | Number of trees to scatter |
| `area` | int | 40 | Size of the ground plane (40x40 units) |
| `seed` | int | 0 | Random seed for reproducibility |
| `path_clear` | bool | True | Avoid the central path |
| `pond_clear` | bool | True | Avoid the circular pond |

## Example Usage

### Basic scattering:
```python
import sys
sys.path.append('maya_scripts')
import set_dresser

# Scatter 10 rocks and 4 trees in a 40x40 area with seed 12
set_dresser.scatter(rock_count=10, tree_count=4, area=40, seed=12)
```

### Using the UI:
```python
import sys
sys.path.append('maya_scripts')
import set_dresser_ui

# Create the UI window
set_dresser_ui.create_ui()

# Now adjust sliders and click Scatter button
```

### Clearing the scene:
```python
import sys
sys.path.append('maya_scripts')
import set_dresser

# Remove all rocks and trees
set_dresser.clear()
```

## Code Structure

### Engine (`maya_scripts/set_dresser.py`):
- `make_rock(position, rotation)` - Creates a single rock
- `make_tree(position, rotation)` - Creates a tree (trunk + canopy)
- `is_clear(position, path_clear, pond_clear)` - Checks if a position is valid
- `scatter(rock_count, tree_count, area, seed, path_clear, pond_clear)` - Main function
- `clear()` - Removes all created objects

### Window (`maya_scripts/set_dresser_ui.py`):
- `create_ui()` - Creates and shows the UI window
- `scatter_from_ui(...)` - Gets UI values and calls the engine
- `clear_from_ui()` - Gets UI values and clears the scene

## Settings

The following settings are at the top of `set_dresser.py`:
- `path_width = 4` - Width of the central path
- `path_buffer = 1` - Extra space to keep away from path edges

## Technical Details

- **Maya version:** Tested on Maya 2026 and 2027
- **Python version:** Python 3 (included with Maya)
- **No external dependencies:** Uses only built-in Maya commands
- **No pymel:** Pure `maya.cmds` implementation
- **Undo support:** Each scatter operation is one undo step

## Known Issues

- UI sliders use `min`/`max` (lowercase) instead of `minimum`/`maximum`
- The seed parameter must be passed correctly to ensure reproducibility

## License

This project is part of a class assignment and is provided as-is for educational purposes.

## Author

Created as part of "The Agent Way" tutorial series

## Version

- **Current:** 1.0.0
- **Last Updated:** 2026
