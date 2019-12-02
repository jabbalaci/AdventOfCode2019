use day02::helper::read_input_file;

const INPUT_FILE: &str = "input.txt";

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
    // test cases:
    // let line = "1,9,10,3,2,3,11,0,99,30,40,50";
    // let line = "1,1,1,4,99,5,6,0,99";

    let lines: Vec<String> = read_input_file(INPUT_FILE);
    let line = &lines[0];

    let mut numbers: Vec<i32> = line.split(',').map(|s| s.parse().unwrap()).collect();
    numbers[1] = 12;
    numbers[2] = 2;
    let numbers = numbers;    // make it immutable

    println!("before:");
    println!("{:?}", numbers);
    println!();
    println!("after:");
    let result: Vec<i32> = process(&numbers);
    println!("{:?}", result);
}
