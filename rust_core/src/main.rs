use std::env;

/// Strips zero-width and Trojan-Source bidirectional override characters (CVE-2021-42574).
pub fn strip_steganographic_unicode(input: &str) -> (String, usize) {
    let mut cleaned = String::with_capacity(input.len());
    let mut removed = 0usize;
    for ch in input.chars() {
        let code = ch as u32;
        let is_steg = (0x200B..=0x200F).contains(&code)
            || (0x202A..=0x202E).contains(&code)
            || (0x2060..=0x2069).contains(&code)
            || code == 0xFEFF
            || (0xE0000..=0xE007F).contains(&code);
        if is_steg {
            removed += 1;
        } else {
            cleaned.push(ch);
        }
    }
    (cleaned, removed)
}

/// Computes bounding-box volume in mm^3 for a parametric 3D CAD enclosure.
pub fn compute_cad_bbox_volume_mm3(width_mm: f64, depth_mm: f64, height_mm: f64) -> f64 {
    (width_mm.max(0.0)) * (depth_mm.max(0.0)) * (height_mm.max(0.0))
}

/// Deterministic 64-bit FNV-1a fingerprint for 3D mesh & CAD recipe hashing.
pub fn fnv1a_64(input: &str) -> u64 {
    let mut hash: u64 = 0xcbf29ce484222325;
    for b in input.as_bytes() {
        hash ^= *b as u64;
        hash = hash.wrapping_mul(0x100000001b3);
    }
    hash
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let sample = args.get(1).map(|s| s.as_str()).unwrap_or("InsightDesign");
    let (cleaned, removed) = strip_steganographic_unicode(sample);
    let fp = fnv1a_64(&cleaned);
    let vol = compute_cad_bbox_volume_mm3(120.0, 80.0, 45.0);
    println!(
        "{{\"member\":\"InsightDesign\",\"cleaned\":\"{}\",\"steganographic_removed\":{},\"cad_bbox_volume_mm3\":{:.1},\"fnv1a_64\":\"0x{:016x}\"}}",
        cleaned, removed, vol, fp
    );
}
