use std::fs::File;
use std::io::{BufRead, BufReader};

pub fn read_input_file(fname: &str) -> Vec<String>
{
    let file = File::open(fname).unwrap();
    let reader = BufReader::new(file);
    let mut lines = Vec::new();

    for line in reader.lines() {
        let line = line.unwrap(); // Ignore errors.
        lines.push(line);
    }
    lines
}