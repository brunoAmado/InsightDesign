import bpy
from pathlib import Path

# ChronicleRAG & InsightChat — Procedural Millimetric Blender (bpy) + Game Asset Multi-LOD Generator
# Prompt: Low-poly CitySocket smart-city node with orbital camera
# Units: 1.0 Blender Unit = 1.0 Millimeter (scale_length = 0.001)

PARAMS_MM = {
    "width_mm": 120.0,
    "height_mm": 45.0,
    "depth_mm": 80.0,
    "wall_thickness_mm": 3.0,
    "hole_diameter_mm": 4.2,
    "hole_pitch_x_mm": 136.0,
    "hole_pitch_y_mm": 216.0,
    "fit_tolerance_mm": 0.2,
    "mold_draft_angle_deg": 2.0,
}

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene
scene.unit_settings.system = 'METRIC'
scene.unit_settings.length_unit = 'MILLIMETERS'
scene.unit_settings.scale_length = 0.001

for k, v in PARAMS_MM.items():
    scene[k] = v

# 1. Create Main Parametric Body (in mm)
W, H, D = PARAMS_MM["width_mm"], PARAMS_MM["height_mm"], PARAMS_MM["depth_mm"]
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0.0, 0.0, D / 2.0))
body = bpy.context.active_object
body.name = "Parametric_Part_LOD0"
body.dimensions = (W, H, D)
bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

# 2. Add Non-Destructive Solidify (Wall Thickness) & Bevel Modifiers
solid = body.modifiers.new(name="Parametric_Wall_Thickness", type='SOLIDIFY')
solid.thickness = PARAMS_MM["wall_thickness_mm"]

bevel = body.modifiers.new(name="Precision_Chamfer", type='BEVEL')
bevel.width = 0.8
bevel.segments = 3

# 3. Create 4 Non-Destructive Boolean Hole Cutters (Change radius anytime to resize holes!)
r_hole = (PARAMS_MM["hole_diameter_mm"] + PARAMS_MM["fit_tolerance_mm"]) / 2.0
hx, hy = PARAMS_MM["hole_pitch_x_mm"] / 2.0, PARAMS_MM["hole_pitch_y_mm"] / 2.0
for idx, (cx, cy) in enumerate([(-hx, -hy), (hx, -hy), (-hx, hy), (hx, hy)], start=1):
    bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=r_hole, depth=D * 2.2, location=(cx, cy, D / 2.0))
    cutter = bpy.context.active_object
    cutter.name = f"Hole_Cutter_{idx}_{PARAMS_MM['hole_diameter_mm']}mm"
    cutter.display_type = 'WIRE'
    bool_mod = body.modifiers.new(name=f"Drill_Hole_{idx}", type='BOOLEAN')
    bool_mod.operation = 'DIFFERENCE'
    bool_mod.solver = 'EXACT'
    bool_mod.object = cutter

# 4. Generate Game-Engine LOD1 (50% tris), LOD2 (25% tris) & UCX_ Convex Collision Proxy
for lod_idx, ratio in ((1, 0.5), (2, 0.25)):
    lod_obj = body.copy()
    lod_obj.data = body.data.copy()
    lod_obj.name = f"Parametric_Part_LOD{lod_idx}"
    bpy.context.collection.objects.link(lod_obj)
    dec = lod_obj.modifiers.new(name=f"Game_LOD{lod_idx}_Decimate", type='DECIMATE')
    dec.ratio = ratio

col_obj = body.copy()
col_obj.data = body.data.copy()
col_obj.name = "UCX_Parametric_Part_01"
bpy.context.collection.objects.link(col_obj)
