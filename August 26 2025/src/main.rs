fn is_valid_hex_code(hex_code: &str) -> bool {
    // Check if the string starts with '#'
    if !hex_code.starts_with('#') {
        return false;
    }
    
    // Check if the length is exactly 7 characters (# + 6 hex digits)
    if hex_code.len() != 7 {
        return false;
    }
    
    // Check if all characters after '#' are valid hex digits (0-9, A-F, a-f)
    let hex_part = &hex_code[1..]; // Skip the '#' character
    for ch in hex_part.chars() {
        if !ch.is_ascii_hexdigit() {
            return false;
        }
    }
    
    true
}

fn main() {
    // Test examples from the problem statement
    println!("is_valid_hex_code(\"#CD5C5C\") = {}", is_valid_hex_code("#CD5C5C"));
    println!("is_valid_hex_code(\"#EAECEE\") = {}", is_valid_hex_code("#EAECEE"));
    println!("is_valid_hex_code(\"#eaecee\") = {}", is_valid_hex_code("#eaecee"));
    println!("is_valid_hex_code(\"#CD5C58C\") = {}", is_valid_hex_code("#CD5C58C"));
    println!("is_valid_hex_code(\"#CD5C5Z\") = {}", is_valid_hex_code("#CD5C5Z"));
    println!("is_valid_hex_code(\"#CD5C&C\") = {}", is_valid_hex_code("#CD5C&C"));
    println!("is_valid_hex_code(\"CD5C5C\") = {}", is_valid_hex_code("CD5C5C"));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_valid_hex_codes() {
        assert_eq!(is_valid_hex_code("#CD5C5C"), true);
        assert_eq!(is_valid_hex_code("#EAECEE"), true);
        assert_eq!(is_valid_hex_code("#eaecee"), true);
        assert_eq!(is_valid_hex_code("#123456"), true);
        assert_eq!(is_valid_hex_code("#ABCDEF"), true);
        assert_eq!(is_valid_hex_code("#abcdef"), true);
        assert_eq!(is_valid_hex_code("#000000"), true);
        assert_eq!(is_valid_hex_code("#FFFFFF"), true);
    }

    #[test]
    fn test_invalid_hex_codes() {
        // Too long
        assert_eq!(is_valid_hex_code("#CD5C58C"), false);
        
        // Invalid characters
        assert_eq!(is_valid_hex_code("#CD5C5Z"), false);
        assert_eq!(is_valid_hex_code("#CD5C&C"), false);
        
        // Missing #
        assert_eq!(is_valid_hex_code("CD5C5C"), false);
        
        // Too short
        assert_eq!(is_valid_hex_code("#CD5C5"), false);
        assert_eq!(is_valid_hex_code("#"), false);
        assert_eq!(is_valid_hex_code(""), false);
        
        // Wrong start character
        assert_eq!(is_valid_hex_code("@CD5C5C"), false);
    }
}
