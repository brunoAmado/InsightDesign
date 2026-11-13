// ChronicleRAG & InsightChat — Parametric Millimetric CAD & Mold Generator (.scad)
// Change any variable below in millimeters (mm) — holes, wall thickness, and mold cavity update automatically!

width_mm          = 120.0;
height_mm         = 45.0;
depth_mm          = 80.0;
wall_thickness_mm = 3.0;
hole_diameter_mm  = 4.2;   // e.g. 3.2mm for M3 clearance, 2.5mm for M3 self-tap
hole_pitch_x_mm   = 136.0;
hole_pitch_y_mm   = 216.0;
fit_tolerance_mm  = 0.2;
mold_draft_deg    = 2.0;
mold_shrink_pct   = 0.5;
render_mode       = "part_and_mold"; // "part_only" | "mold_cavity_and_core" | "part_and_mold"

$fn = 72; // High circular hole accuracy

module precision_part() {
    scale_f = 1.0 + (mold_shrink_pct / 100.0);
    W = width_mm * scale_f;
    H = height_mm * scale_f;
    D = depth_mm * scale_f;
    d_hole = hole_diameter_mm + fit_tolerance_mm;

    difference() {
        // Outer shell
        translate([-W/2, -H/2, 0])
            cube([W, H, D]);

        // Inner cavity
        translate([-(W/2) + wall_thickness_mm, -(H/2) + wall_thickness_mm, wall_thickness_mm])
            cube([W - 2*wall_thickness_mm, H - 2*wall_thickness_mm, D + 1.0]);

        // 4 Precision Mounting Holes
        for (sx = [-1, 1]) {
            for (sy = [-1, 1]) {
                translate([sx * (hole_pitch_x_mm / 2), sy * (hole_pitch_y_mm / 2), -1.0])
                    cylinder(h = D + 2.0, d = d_hole);
            }
        }
    }
}

module injection_mold_lower_cavity() {
    margin = 18.0;
    W_mold = width_mm + 2 * margin;
    H_mold = height_mm + 2 * margin;
    D_mold = (depth_mm / 2) + margin;
    difference() {
        translate([-W_mold/2, -H_mold/2, -margin])
            cube([W_mold, H_mold, D_mold]);
        precision_part();
        // 4 Mold Registration Alignment Dowel Pins (6.0 mm)
        for (sx = [-1, 1])
            for (sy = [-1, 1])
                translate([sx * (W_mold/2 - 8), sy * (H_mold/2 - 8), -margin - 1])
                    cylinder(h = D_mold + 2, d = 6.0 + fit_tolerance_mm);
    }
}

if (render_mode == "part_only") {
    precision_part();
} else if (render_mode == "mold_cavity_and_core") {
    injection_mold_lower_cavity();
} else {
    precision_part();
    translate([width_mm + 45, 0, 0])
        injection_mold_lower_cavity();
}
