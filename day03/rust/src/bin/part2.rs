use hashbrown::{HashMap, HashSet};
use day03::helper::read_input_file;

// const INPUT_FILE: &str = "examples/part1/example1.txt";
// const INPUT_FILE: &str = "examples/part1/example2.txt";
// const INPUT_FILE: &str = "examples/part1/example3.txt";
const INPUT_FILE: &str = "input.txt";

// ============
// struct Point
// ============

#[derive(Hash, Eq, PartialEq, Debug)]
struct Point {
    x: i32,
    y: i32
}

// ==========
// class Grid
// ==========

struct Grid {
    wire1: Vec<String>,
    wire2: Vec<String>,
    wire1_path: HashMap<Point, i32>,
    wire2_path: HashMap<Point, i32>
}

impl Grid {
    // constructor
    fn new(line1: &str, line2: &str) -> Grid {
        let wire1 = line1.split(",").map(|s| s.to_string()).collect();
        let wire2 = line2.split(",").map(|s| s.to_string()).collect();
        Grid {
            wire1: wire1,
            wire2: wire2,
            wire1_path: HashMap::new(),
            wire2_path: HashMap::new()
        }
    }

    fn debug(&self) {
        println!("{:?}", self.wire1);
        println!("{:?}", self.wire2);
    }

    fn follow_wire(&self, wire: &Vec<String>) -> HashMap<Point, i32> {
        let mut coordinates: HashMap<Point, i32> = HashMap::new();
        let mut x = 0;
        let mut y = 0;
        let mut path_length = 0;
        for instruction in wire {
            let direction = instruction.chars().next().unwrap();
            let steps: i32 = (&instruction[1..]).parse().unwrap();
            for _ in 0 .. steps {
                match direction {
                    'R' => x += 1,
                    'L' => x -= 1,
                    'U' => y += 1,
                    'D' => y -= 1,
                    _ => ()    // normally we cannot get here
                }
                path_length += 1;
                let p = Point { x: x, y: y };
                if !coordinates.contains_key(&p) {
                    coordinates.insert(p, path_length);
                }
            }
        }

        coordinates
    }

    fn follow_wires(&mut self) {
        self.wire1_path = self.follow_wire(&self.wire1);
        self.wire2_path = self.follow_wire(&self.wire2);
    }

    fn debug2(&self) {
        println!("{:?}", self.wire1_path);
        println!("{:?}", self.wire2_path);
    }

    fn find_closest_intersection(&self) -> i32 {
        let wire1_path_as_set = {
            let mut result = HashSet::new();
            for key in self.wire1_path.keys() {
                result.insert(key);
            }
            result
        };
        let wire2_path_as_set = {
            let mut result = HashSet::new();
            for key in self.wire2_path.keys() {
                result.insert(key);
            }
            result
        };
        let crosses: HashSet<_> = wire1_path_as_set.intersection(&wire2_path_as_set).collect();
        // println!("{:?}", crosses);
        let closest = crosses.iter().min_by_key(|p| {
            let val1 = self.wire1_path[p];
            let val2 = self.wire2_path[p];
            val1 + val2
        }).unwrap();
        // println!("{:?}", closest);
        //
        let result = self.wire1_path[closest] + self.wire2_path[closest];
        result
    }
}

// ==========================================================================

fn main()
{
    let lines: Vec<String> = read_input_file(INPUT_FILE);
    let line1 = &lines[0];
    let line2 = &lines[1];
    // for line in lines.iter() {
    //     println!("{}", line);
    // }
    let mut grid = Grid::new(line1, line2);
    // grid.debug();
    grid.follow_wires();
    // grid.debug2();
    let result = grid.find_closest_intersection();
    println!("{}", result);
}
