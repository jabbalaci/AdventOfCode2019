//const INPUT: &str = "112233-112233";    // test 1
//const INPUT: &str = "123444-123444";    // test 2
//const INPUT: &str = "111122-111122";    // test 3
const INPUT: &str = "136760-595730";    // input


fn explode(number: i32) -> Vec<i32>
{
    let mut n = number;
    let mut digits = Vec::new();
    while n > 0 {
        digits.push(n % 10);
        n = n / 10;
    }

    digits.reverse();
    digits
}

fn is_password(digits: &Vec<i32>) -> bool
{
    let mut ascending = true;

    for i in 0 ..= digits.len()-2 {
        let a = digits[i];
        let b = digits[i+1];
        if a > b {
            ascending = false;
        }
    }
    if !ascending {
        return false;
    }

    let mut counter = [0; 10];
    for digit in digits {
        counter[*digit as usize] += 1;
    }
    let has_double = counter.iter().any(|x| *x == 2);

    has_double && ascending
}

fn process(lo: i32, hi: i32) -> i32
{
    let mut cnt = 0;
    for n in lo ..= hi {
        let digits = explode(n);
        if is_password(&digits) {
            cnt += 1;
        }
    }

    cnt
}

fn main()
{
    let parts: Vec<&str> = INPUT.split('-').collect();
    let lo: i32 = parts[0].parse().unwrap();
    let hi: i32 = parts[1].parse().unwrap();
//    println!("{:?}", parts);
    let result = process(lo, hi);
    println!("{}", result);
}
