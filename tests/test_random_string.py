"""
Test suite for random string generator
"""
import pytest
from utils.string_generator import generate_random_test_string, generate_random_full_name


class TestRandomStringGenerator:
    
    def test_generate_random_test_string_format(self):
        """Test string format"""
        print("\n" + "="*70)
        print("🎲 TEST: String Format")
        print("="*70)
        
        test_string = generate_random_test_string()
        print(f"Generated: {test_string}")
        print(f"Length: {len(test_string)}")
        
        assert len(test_string) == 9
        print("✅ PASSED: Correct length")
    
    def test_generated_string_contains_letters_and_digits(self):
        """Test contains letters and digits"""
        print("\n" + "="*70)
        print("🎲 TEST: Contains Letters and Digits")
        print("="*70)
        
        test_string = generate_random_test_string()
        print(f"Generated: {test_string}")
        
        has_letters = any(c.isalpha() for c in test_string)
        has_digits = any(c.isdigit() for c in test_string)
        
        assert has_letters and has_digits
        print("✅ PASSED: Has both letters and digits")
    
    def test_generated_string_has_3_digits(self):
        """Test exactly 3 digits"""
        print("\n" + "="*70)
        print("🎲 TEST: Exactly 3 Digits")
        print("="*70)
        
        test_string = generate_random_test_string()
        digit_count = sum(1 for c in test_string if c.isdigit())
        
        print(f"Generated: {test_string}")
        print(f"Digits: {digit_count}")
        
        assert digit_count == 3
        print("✅ PASSED: Has 3 digits")
    
    def test_generated_string_has_6_letters(self):
        """Test exactly 6 letters"""
        print("\n" + "="*70)
        print("🎲 TEST: Exactly 6 Letters")
        print("="*70)
        
        test_string = generate_random_test_string()
        letter_count = sum(1 for c in test_string if c.isalpha())
        
        print(f"Generated: {test_string}")
        print(f"Letters: {letter_count}")
        
        assert letter_count == 6
        print("✅ PASSED: Has 6 letters")
    
    def test_multiple_generations(self):
        """Test multiple generations"""
        print("\n" + "="*70)
        print("🎲 TEST: Multiple Generations")
        print("="*70)
        print("\nGenerating 10 random strings:")
        print("-" * 70)
        
        for i in range(10):
            test_string = generate_random_test_string()
            print(f"   {i+1:2d}. {test_string}")
        
        print("\n✅ PASSED: All generated successfully")
        print("="*70 + "\n")