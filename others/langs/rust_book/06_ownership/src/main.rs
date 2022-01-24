fn sum(a: i32, b: i32) -> i32 {
    a + b
}

fn show_str(cad: &str) {
    println!("{}", cad);
}

fn show_string(cad: String) {
    println!("{}", cad)
}

fn main() {
    // No aplica el ownership perque son primitius
    let [a, b] = [2, 3];
    let res = sum(a, b);
    println!("{} + {} = {}", a, b, res);

    // Tampoc aplica perque es un &str
    let s1 = "cad1";
    show_str(s1);
    println!("Fin: {}", s1);

    let mut s2 = String::from("Hello");
    s2.push_str(" World");
    show_string(s2);
    // println!("Fin: {}", s2);
}
