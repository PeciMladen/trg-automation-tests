"""
Random string generator for testing
"""
import random
import string


def generate_random_test_string():
    """
    Generate random test string
    
    Format:
    1. Generate 6 random letters (mixed case)
    2. Generate 3 random digits
    3. Concatenate: letters + digits
    4. Reverse the string
    
    Example: "sGeoRD256" -> "652DRoeGs"
    
    Returns:
        str: Reversed random string (9 characters)
    """
    # Step 1: 6 random letters
    letters = ''.join(random.choices(string.ascii_letters, k=6))
    
    # Step 2: 3 random digits
    digits = ''.join(random.choices(string.digits, k=3))
    
    # Step 3: Concatenate
    combined = letters + digits
    
    # Step 4: Reverse
    reversed_string = combined[::-1]
    
    return reversed_string


def generate_random_full_name():
    """
    Generate random full name for forms
    
    Returns:
        str: Random test name
    """
    return generate_random_test_string()


if __name__ == "__main__":
    print("Testing Random String Generator:")
    print("=" * 50)
    
    for i in range(5):
        test_string = generate_random_test_string()
        print(f"{i+1}. {test_string}")