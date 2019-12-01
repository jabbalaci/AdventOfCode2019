// Part 1

use day??::helper::read_input_file;    // where day?? is the project's name from Cargo.toml

const INPUT_FILE: &str = "input.txt";

fn main()
{
    let lines: Vec<String> = helper::read_input_file(INPUT_FILE);
    for line in lines {
        println!("{}", line);
    }
}
