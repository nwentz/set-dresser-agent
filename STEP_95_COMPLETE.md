# Step 95 Complete: Ask for a change by name

**Status:** ✅ PASSED

**Changes made to C:\Users\nwentz\Documents\maya\2027\scripts\set_dresser.py:**

**1. New settings at the top (lines 9-11):**
```python
# Settings for the set dresser
path_width = 4          # Width of the path running through the scene
path_buffer = 1         # Extra space to keep away from the path edges
```

**2. Changed inside `is_clear` (line 59):**
```python
# Keep everything at least path_buffer units back from the path edges
if abs(x - center_x) < (path_width / 2) + path_buffer:
    return False
```

**3. Removed:** Local `path_width = 4` variable from inside the function

**Result seen in viewport:**
- ✅ Wider clear strip on both sides of the path (now 5 units wide total)
- ✅ Objects kept at least 1 unit away from the path edges

**Difference from Week 1 vocabulary:**
- Week 1: "keep rocks off the path" (vague)
- Week 3: "keep everything at least 1 unit back from the path's edges" (precise, named parameters)

**Why this works better:**
- Precise specifications prevent misinterpretation
- Named settings (`path_buffer`) make the code more maintainable
- Separating settings from logic follows good software engineering practices
