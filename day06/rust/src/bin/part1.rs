use day06::helper::read_input_file;

use fxhash::FxHashMap as HashMap;

// const INPUT_FILE: &str = "example.txt";
const INPUT_FILE: &str = "input.txt";


fn main()
{
    let lines: Vec<String> = read_input_file(INPUT_FILE);
    //for line in lines.iter() {
    //    println!("{}", line);
    //}

    let mut full: HashMap<&str, Vec<&str>> = HashMap::default();
    let mut orbits: HashMap<&str, i32> = HashMap::default();
    orbits.insert("COM", 0);

    for line in lines.iter() {
        let parts: Vec<&str> = line.split(")").collect();
        let (left, right) = (parts[0], parts[1]);
        if !full.contains_key(left) {
            full.insert(left, Vec::new());
        }
        full.get_mut(left).unwrap().push(right);
    }

    //println!("{:?}", full);

    while full.len() > 0
    {
        for k in full.keys().map(|s| s.clone())
        {
            if orbits.contains_key(k)
            {
                let orbit_value = orbits[k];
                let reachable = &full[k];
                for obj in reachable {
                    orbits.insert(obj, orbit_value + 1);
                }
                full.remove(k);
                break;
            }
        }
    }
    // println!("{:?}", orbits);

    let result: i32 = orbits.values().sum();
    println!("{}", result);
}
