#[derive(Debug)]
enum IpAddr {
    V4(u8, u8, u8, u8),
    V6(String),
}

fn check(opt: Option<i32>) -> () {
    match opt {
        Some(a) => dbg!(a),
        None => dbg!("None"),
    }

    return ();
}

fn main() {
    let home = IpAddr::V4(127, 0, 0, 1);

    let loopback = IpAddr::V6(String::from("::1"));

    dbg!(home);
    dbg!(loopback);

    check(Some(1));
}
