#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn area(rectangle: &Rectangle) -> u32 {
    rectangle.width * rectangle.height
}

impl Rectangle {
    fn area(self: &Self) -> u32 {
        // o (&self)
        self.width * self.height
    }

    fn square(dim: u32) -> Rectangle {
        Rectangle {
            width: dim,
            height: dim,
        }
    }
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}

fn main() {
    let scale = 2;
    let rect1 = Rectangle {
        width: dbg!(30 * scale),
        height: 50,
    };

    let rect2 = Rectangle {
        width: 2,
        height: 3,
    };

    dbg!(area(&rect1));

    dbg!(rect1.area());

    dbg!(rect1.can_hold(&rect2));

    println!("{:?}", rect1);
    dbg!(&rect1);

    dbg!(Rectangle::square(3));
}
