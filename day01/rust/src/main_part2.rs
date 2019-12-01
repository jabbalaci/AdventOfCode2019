// Part 2

mod helper;

const INPUT_FILE: &str = "input.txt";

fn fuel(mass: i32) -> i32 {
    (mass / 3) - 2
}

fn extra_fuel(mass: i32) -> i32
{
    let mut value = mass;
    let mut total = 0;

    while value > 0 {
        value = fuel(value);
        if value > 0 {
            total += value;
        }
    }
    total
}

fn main()
{
    let lines: Vec<String> = helper::read_input_file(INPUT_FILE);
    let result: i32 = lines.iter().map( |s| extra_fuel(s.parse().unwrap()) ).sum();
    println!("{}", result);
}
