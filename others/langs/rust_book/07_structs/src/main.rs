struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}

fn build_user(email: String, username: String) -> User {
    User {
        email,
        username,
        active: true,
        sign_in_count: 1,
    }
}

fn main() {
    let mut user1 = build_user(
        String::from("someone@example.com"),
        String::from("someusername123"),
    );

    println!(
        "{} - {} - {} - {}",
        user1.email, user1.username, user1.active, user1.sign_in_count
    );

    user1.email = String::from("anotheremail");

    println!(
        "{} - {} - {} - {}",
        user1.email, user1.username, user1.active, user1.sign_in_count
    );

    // Despres de esta declaracio no puc gastar user1 perque he "mogut" els valors de username a user2
    let user2 = User {
        email: String::from("another@example.com"),
        ..user1
    };

    // println!("{}", user1.username); // ERROR
}
