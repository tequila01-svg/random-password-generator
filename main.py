import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, 
                      use_digits=True, use_special_chars=True):
    """
    Generate a random password with customizable complexity.
    
    Parameters:
    - length: Total length of the password (default 12)
    - use_uppercase: Include uppercase letters (default True)
    - use_lowercase: Include lowercase letters (default True)
    - use_digits: Include numeric digits (default True)
    - use_special_chars: Include special characters (default True)
    
    Returns:
    A randomly generated password as a string
    """
    # Define character sets
    char_sets = []
    
    if use_uppercase:
        char_sets.append(string.ascii_uppercase)
    if use_lowercase:
        char_sets.append(string.ascii_lowercase)
    if use_digits:
        char_sets.append(string.digits)
    if use_special_chars:
        char_sets.append(string.punctuation)
    
    # Validate input
    if not char_sets:
        raise ValueError("At least one character set must be selected")
    
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")
    
    # Ensure at least one character from each selected set
    password = []
    for char_set in char_sets:
        password.append(random.choice(char_set))
    
    # Fill the rest of the password
    remaining_length = length - len(password)
    all_chars = ''.join(char_sets)
    
    for _ in range(remaining_length):
        password.append(random.choice(all_chars))
    
    # Shuffle the password characters
    random.shuffle(password)
    
    # Convert to string
    return ''.join(password)

# Example usage
if __name__ == "__main__":
    # Generate a few example passwords
    print("Default password:", generate_password())
    print("Short password:", generate_password(length=8))
    print("Only lowercase:", generate_password(
        use_uppercase=False, use_digits=False, use_special_chars=False
    ))
    print("Complex password:", generate_password(
        length=16, use_special_chars=True
    ))