use day05::helper::read_input_file;

const INPUT_FILE: &str = "input.txt";


#[derive(Debug, PartialEq)]
enum Mode {
    PositionMode,
    ImmediateMode
}

#[derive(Debug)]
struct Instruction {
    opcode: i32,
    first_param_mode: Mode,
    second_param_mode: Mode,
    third_param_mode: Mode
}

fn read_input() -> i32 {
    1
}

fn read_instruction(number: i32) -> Instruction
{
    fn to_mode(c: char) -> Mode {
        if c == '0' {
            Mode::PositionMode
        } else {
            Mode::ImmediateMode
        }
    }

    if number == 99 {
        // special case, it'll halt the program; parameter modes are not used, they get a dummy value
        return Instruction {
            opcode: number, first_param_mode: Mode::PositionMode,
            second_param_mode: Mode::PositionMode, third_param_mode: Mode::PositionMode
        }
    }

    let s = number.to_string();
    let result = {
        if s.len() == 1
        {
            let opcode = number;
            let first_param_mode = Mode::PositionMode;
            let second_param_mode = Mode::PositionMode;
            let third_param_mode = Mode::PositionMode;
            Instruction {    // yield
                opcode: opcode, first_param_mode: first_param_mode,
                second_param_mode: second_param_mode, third_param_mode: third_param_mode
            }
        }
        else
        {
            let opcode: i32 = (&s[s.len()-2..]).replace("0", "").parse().unwrap();
            let params: Vec<char> = format!("{:0>3}", &s[..s.len()-2]).chars().collect();
            let first_param_mode = to_mode(params[params.len()-1]);
            let second_param_mode = to_mode(params[params.len()-2]);
            let third_param_mode = to_mode(params[params.len()-3]);
            Instruction {    // yield
                opcode: opcode, first_param_mode: first_param_mode,
                second_param_mode: second_param_mode, third_param_mode: third_param_mode
            }
        }
    };

    result
}

fn run(program: &Vec<i32>) -> Vec<i32>
{
    fn get_param(data: &Vec<i32>, value: i32, mode: Mode) -> i32 {
        if mode == Mode::ImmediateMode {
            value
        } else {
            data[value as usize]
        }
    }

    let mut data = program.to_vec();    // copy

    let mut idx: usize = 0;
    let mut inst = read_instruction(data[idx]);
    while inst.opcode != 99
    {
        if inst.opcode == 1
        {
            let inp1 = get_param(&data, data[idx + 1], inst.first_param_mode);
            let inp2 = get_param(&data, data[idx + 2], inst.second_param_mode);
            let pos = data[idx + 3] as usize;
            data[pos] = inp1 + inp2;
            idx += 4;
        }
        else if inst.opcode == 2
        {
            let inp1 = get_param(&data, data[idx + 1], inst.first_param_mode);
            let inp2 = get_param(&data, data[idx + 2], inst.second_param_mode);
            let pos = data[idx + 3] as usize;
            data[pos] = inp1 * inp2;
            idx += 4;
        }
        else if inst.opcode == 3
        {
            let inp = read_input();
            let pos = data[idx + 1] as usize;
            data[pos] = inp;
            idx += 2;
        }
        else if inst.opcode == 4
        {
            let inp1 = get_param(&data, data[idx + 1], inst.first_param_mode);
            println!("Output: {}", inp1);
            idx += 2;
        }
        else {
            println!("Error: invalid opcode!");
        }
        inst = read_instruction(data[idx]);
    }

    data
}

fn main()
{
//    let line = "3,0,4,0,99";
//    let line = "1002,4,3,4,33";

    let lines: Vec<String> = read_input_file(INPUT_FILE);
    let line = &lines[0];

    let program: Vec<i32> = line.split(',').map(|s| s.parse().unwrap()).collect();

    run(&program);
}
