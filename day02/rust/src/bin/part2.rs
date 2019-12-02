use day02::helper::read_input_file;

const INPUT_FILE: &str = "input.txt";
const GOAL: i32 = 19690720;

fn process(numbers: &Vec<i32>) -> Vec<i32>
{
    let mut data = numbers.to_vec();    // copy

    let mut idx: usize = 0;
    let mut opcode = data[idx];
    while opcode != 99 {
        if opcode == 1 {
            let inp1 = data[data[idx + 1] as usize];
            let inp2 = data[data[idx + 2] as usize];
            let pos = data[idx + 3];
            data[pos as usize] = inp1 + inp2;
        }
        else if opcode == 2 {
            let inp1 = data[data[idx + 1] as usize];
            let inp2 = data[data[idx + 2] as usize];
            let pos = data[idx + 3];
            data[pos as usize] = inp1 * inp2;
        }
        idx += 4;
        opcode = data[idx];
    }

    data
}

fn main()
{
    let lines: Vec<String> = read_input_file(INPUT_FILE);
    let line = &lines[0];

    let mut numbers: Vec<i32> = line.split(',').map(|s| s.parse().unwrap()).collect();

    'outer:
    for i in 0 ..= 99 {
        for j in 0 ..= 99 {
            numbers[1] = i;
            numbers[2] = j;
            println!("# i = {}, j = {}", i, j);
            let result: Vec<i32> = process(&numbers);
            if result[0] == GOAL {
                println!("i = {}", i);
                println!("j = {}", j);
                println!("answer: {}", 100 * i + j);
                break 'outer;
            }
        }
    }
    println!("__END__");
}
