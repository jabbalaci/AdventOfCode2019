// Part 1

mod helper;

const INPUT_FILE: &str = "input.txt";

fn main()
{
    let lines: Vec<String> = helper::read_input_file(INPUT_FILE);
    for line in lines {
        println!("{}", line);
    }
}
