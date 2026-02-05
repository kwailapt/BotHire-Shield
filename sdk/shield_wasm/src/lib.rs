use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub struct ShieldWasm;

#[wasm_bindgen]
impl ShieldWasm {
    pub fn calculate_tier(stake: u64, tenure: u64, last_active: u64) -> u32 {
        let mut p = stake * tenure;
        let decay_intervals = last_active / 30;
        
        for _ in 0..decay_intervals {
            p = (p * 9) / 10;
        }

        if p == 0 { return 0; }

        // Newton's Method (Integer Sqrt)
        let mut x = p;
        let mut y = (x + 1) / 2;
        while y < x {
            x = y;
            y = (x + p / x) / 2;
        }

        let score = x;
        if score < 100 { 1 }
        else if score < 500 { 2 }
        else if score < 2000 { 3 }
        else { 4 }
    }

    pub fn generate_proof(stake: u64, tenure: u64, secret: &str) -> String {
        let payload = format!("{}{}", stake, tenure);
        let combined = format!("{}{}", payload, secret);
        let sum: u32 = combined.chars().map(|c| c as u32).sum();
        sum.to_string()
    }
}
