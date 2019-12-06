use day06::helper::read_input_file;

use fxhash::FxHashMap as HashMap;
use std::collections::HashSet;

// const INPUT_FILE: &str = "example2.txt";
const INPUT_FILE: &str = "input.txt";


fn find_path(d: &HashMap<&str, &str>, src: &str, dest: &str) -> Vec<String>
{
    let mut path = Vec::new();
    let mut key = src;
    loop {
        let value = d[key];
        path.push(value.to_string());
        if value == dest {
            break;
        }
        key = value;
    }

    path.reverse();
    path
}

fn main()
{
    let lines: Vec<String> = read_input_file(INPUT_FILE);

    let mut child_parent: HashMap<&str, &str> = HashMap::default();
    for line in lines.iter() {
        let parts: Vec<&str> = line.split(")").collect();
        let (left, right) = (parts[0], parts[1]);
        child_parent.insert(right, left);
    }
    let child_parent = child_parent;    // immutable

    let p1: Vec<String> = find_path(&child_parent, "YOU", "COM");
    // println!("{:?}", p1);
    let p2: Vec<String> = find_path(&child_parent, "SAN", "COM");
    // println!("{:?}", p2);

    let p1_set: HashSet<String> = p1.iter().cloned().collect();
    // println!("{:?}", p1_set);
    let p2_set: HashSet<String> = p2.iter().cloned().collect();
    // println!("{:?}", p2_set);
    let diff1: HashSet<_> = p1_set.difference(&p2_set).collect();
    let diff2: HashSet<_> = p2_set.difference(&p1_set).collect();
    let result = diff1.len() + diff2.len();
    println!("{}", result);
}
