fn is_prime(n: u32) -> bool {
    if (n == 1) {
        return true;
    }

    for i in 2..n-1 {
        if n % i == 0 {
            return false;
        }
    }

    true
}

pub fn nth(n: u32) -> u32 {
    if (n == 0) {
        return 2;
    }

    let mut counter = 3;
    let mut n_prime = 1;

    loop {
        if is_prime(counter) {
            if n_prime == n {
                break;
            }

            n_prime+=1;
        }
        
        counter+=1;
    }

    counter
}
