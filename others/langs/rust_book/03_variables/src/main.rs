fn main() {
    let mut x = 5;
    println!("The value of x is: {}", x);
    x = 6;
    println!("The value of x is: {}", x);

    let x = 5;

    let x = x + 1;

    {
        let x = x * 2;
        println!("The value of x in the inner scope is: {}", x);
    }

    println!("The value of x is: {}", x);

    // addition
    let sum = 5 + 10;

    // subtraction
    let difference = 95.5 - 4.3;

    // multiplication
    let product = 4 * 30;

    // division
    let quotient = 56.7 / 32.2;
    let floored = 2 / 3; // Results in 0

    // remainder
    let remainder = 43 % 5;

    let t = true;

    let f: bool = false; // with explicit type annotation

    let tup: (i32, f64, u8) = (500, 6.4, 1);

    let tup2 = (100, 'a', true);

    // Destructuring
    let (x, y, z) = tup;

    let x: (i32, f64, u8) = (500, 6.4, 1);
    let five_hundred = x.0;

    let six_point_four = x.1;

    let one = x.2;
}
