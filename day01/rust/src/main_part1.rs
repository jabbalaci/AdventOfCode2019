// Part 1

mod helper;

const INPUT_FILE: &str = "input.txt";

fn fuel(mass: i32) -> i32 {
    (mass / 3) - 2
}

fn main()
{
    let lines: Vec<String> = helper::read_input_file(INPUT_FILE);
    let result: i32 = lines.iter().map( |s| fuel(s.parse().unwrap()) ).sum();
    println!("{}", result);
}
