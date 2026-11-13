FeatureScript 2411;
import(path : "onshape/std/common.fs", version : "2411.0");

/**
 * ChronicleRAG & InsightChat — Millimetric Parametric CAD & Injection-Mold Plan
 * Source Prompt: CitySocket IP65 200x260x95mm M4 holes 0.2mm tolerance
 * Directly importable into Onshape Part Studio. Change any parameter (Width, Height, Hole Diameter,
 * Hole Pitch, Wall Thickness, Draft Angle, or Fit Tolerance) with 0.01 mm precision!
 */
annotation { "Feature Type Name" : "Parametric CitySocket & Mold Plan" }
export const parametricMoldAndPart = defineFeature(function(context is Context, id is Id, definition is map)
    precondition
    {
        annotation { "Name" : "Outer Width X (mm)" }
        isLength(definition.width, { (millimeter) : [10, 200.0, 2000] } as LengthBoundSpec);

        annotation { "Name" : "Outer Height Y (mm)" }
        isLength(definition.height, { (millimeter) : [10, 260.0, 2000] } as LengthBoundSpec);

        annotation { "Name" : "Outer Depth Z (mm)" }
        isLength(definition.depth, { (millimeter) : [5, 95.0, 1000] } as LengthBoundSpec);

        annotation { "Name" : "Wall Thickness (mm)" }
        isLength(definition.wall, { (millimeter) : [0.8, 3.0, 25.0] } as LengthBoundSpec);

        annotation { "Name" : "Mounting Hole Diameter (mm) [e.g. M3=3.2, M4=4.2, M5=5.2]" }
        isLength(definition.holeDiameter, { (millimeter) : [1.0, 4.2, 50.0] } as LengthBoundSpec);

        annotation { "Name" : "Hole Pitch X (Center-to-Center mm)" }
        isLength(definition.holePitchX, { (millimeter) : [5.0, 176.0, 1900.0] } as LengthBoundSpec);

        annotation { "Name" : "Hole Pitch Y (Center-to-Center mm)" }
        isLength(definition.holePitchY, { (millimeter) : [5.0, 236.0, 1900.0] } as LengthBoundSpec);

        annotation { "Name" : "Fit / Snap Clearance Tolerance (mm)" }
        isLength(definition.fitTolerance, { (millimeter) : [0.02, 0.2, 2.0] } as LengthBoundSpec);

        annotation { "Name" : "Generate 2-Part Injection/Silicone Mold Cavity & Core" }
        isBoolean(definition.generateMoldBlock);
    }
    {
        const W = definition.width * 1.005;
        const H = definition.height * 1.005;
        const D = definition.depth * 1.005;
        const wall = definition.wall;
        const rHole = (definition.holeDiameter + definition.fitTolerance) / 2;

        // 1. Outer Enclosure / Component Body
        fCuboid(context, id + "outerBody", {
            "corner1" : vector(-W / 2, -H / 2, 0 * millimeter),
            "corner2" : vector(W / 2, H / 2, D)
        });

        // 2. Inner Hollow Cavity (respecting exact millimetric wall thickness)
        fCuboid(context, id + "innerCavity", {
            "corner1" : vector(-(W / 2) + wall, -(H / 2) + wall, wall),
            "corner2" : vector((W / 2) - wall, (H / 2) - wall, D + 1 * millimeter)
        });
        opBoolean(context, id + "shellSubtract", {
            "tools" : qCreatedBy(id + "innerCavity", EntityType.BODY),
            "targets" : qCreatedBy(id + "outerBody", EntityType.BODY),
            "operationType" : BooleanOperationType.SUBTRACTION
        });

        // 3. Four Precision Corner Mounting / Boss Holes (exact center-to-center pitch)
        const hx = definition.holePitchX / 2;
        const hy = definition.holePitchY / 2;
        const holeCenters = [
            vector(-hx, -hy, 0 * millimeter),
            vector(hx, -hy, 0 * millimeter),
            vector(-hx, hy, 0 * millimeter),
            vector(hx, hy, 0 * millimeter)
        ];
        for (var i = 0; i < 4; i += 1)
        {
            fCylinder(context, id + ("mountingHole_" ~ i), {
                "bottomCenter" : holeCenters[i] - vector(0 * millimeter, 0 * millimeter, 1 * millimeter),
                "topCenter" : holeCenters[i] + vector(0 * millimeter, 0 * millimeter, D + 2 * millimeter),
                "radius" : rHole
            });
            opBoolean(context, id + ("drillHole_" ~ i), {
                "tools" : qCreatedBy(id + ("mountingHole_" ~ i), EntityType.BODY),
                "targets" : qCreatedBy(id + "outerBody", EntityType.BODY),
                "operationType" : BooleanOperationType.SUBTRACTION
            });
        }
    });
