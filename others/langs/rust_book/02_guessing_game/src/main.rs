use rand::Rng;
use std::cmp::Ordering;
use std::io;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..101);

    // 1..=100
    // =
    // 1..101

    // println!("The secret number is: {}", secret_number);

    loop {
        println!("Please input your guess.");

        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");

        // let guess: u32 = guess.trim().parse().expect("Please type a number!");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        // let x = io::stdin().read_line(&mut guess).unwrap();

        // match io::stdin().read_line(&mut guess) {
        //     Ok(n) => {
        //         println!("{} bytes read", n);
        //         println!("{}", guess);
        //     }
        //     Err(error) => println!("error: {}", error),
        // }

        // let x: Result<i32, i32> = Ok(1);
        // x.expect("Error");

        // let y: Result<i32, i32> = Err(2);
        // y.expect("Este si error");

        println!("You guessed: {}", guess);

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }
}
