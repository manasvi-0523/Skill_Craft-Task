#!/usr/bin/env python3
"""
Password Strength Checker
Assesses password strength based on multiple security criteria
"""

import re
import string
from typing import Dict, List, Tuple


class PasswordStrengthChecker:
    """Evaluates password strength based on various security criteria."""
    
    def __init__(self):
        self.min_length = 8
        self.recommended_length = 12
        self.strong_length = 16
        
    def check_length(self, password: str) -> Tuple[int, str]:
        """Check password length and return score and feedback."""
        length = len(password)
        
        if length < self.min_length:
            return 0, f"Too short (minimum {self.min_length} characters)"
        elif length < self.recommended_length:
            return 1, f"Acceptable length ({length} characters)"
        elif length < self.strong_length:
            return 2, f"Good length ({length} characters)"
        else:
            return 3, f"Excellent length ({length} characters)"
    
    def check_uppercase(self, password: str) -> Tuple[int, str]:
        """Check for uppercase letters."""
        if not any(c.isupper() for c in password):
            return 0, "No uppercase letters"
        
        uppercase_count = sum(1 for c in password if c.isupper())
        if uppercase_count >= 2:
            return 2, f"Contains {uppercase_count} uppercase letters"
        return 1, "Contains uppercase letter"
    
    def check_lowercase(self, password: str) -> Tuple[int, str]:
        """Check for lowercase letters."""
        if not any(c.islower() for c in password):
            return 0, "No lowercase letters"
        
        lowercase_count = sum(1 for c in password if c.islower())
        if lowercase_count >= 2:
            return 2, f"Contains {lowercase_count} lowercase letters"
        return 1, "Contains lowercase letter"
    
    def check_numbers(self, password: str) -> Tuple[int, str]:
        """Check for numeric digits."""
        if not any(c.isdigit() for c in password):
            return 0, "No numbers"
        
        number_count = sum(1 for c in password if c.isdigit())
        if number_count >= 2:
            return 2, f"Contains {number_count} numbers"
        return 1, "Contains number"
    
    def check_special_characters(self, password: str) -> Tuple[int, str]:
        """Check for special characters."""
        special_chars = string.punctuation
        special_count = sum(1 for c in password if c in special_chars)
        
        if special_count == 0:
            return 0, "No special characters"
        elif special_count >= 2:
            return 2, f"Contains {special_count} special characters"
        return 1, "Contains special character"
    
    def check_common_patterns(self, password: str) -> Tuple[int, str]:
        """Check for common weak patterns."""
        issues = []
        
        # Check for sequential characters
        if re.search(r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', password.lower()):
            issues.append("sequential letters")
        
        if re.search(r'(012|123|234|345|456|567|678|789)', password):
            issues.append("sequential numbers")
        
        # Check for repeated characters
        if re.search(r'(.)\1{2,}', password):
            issues.append("repeated characters")
        
        # Check for common words
        common_words = ['password', 'admin', 'user', 'login', '1234', 'qwerty']
        if any(word in password.lower() for word in common_words):
            issues.append("common words")
        
        if issues:
            return 0, f"Weak patterns detected: {', '.join(issues)}"
        return 2, "No common weak patterns"
    
    def check_character_variety(self, password: str) -> Tuple[int, str]:
        """Check overall character variety."""
        char_types = 0
        
        if any(c.isupper() for c in password):
            char_types += 1
        if any(c.islower() for c in password):
            char_types += 1
        if any(c.isdigit() for c in password):
            char_types += 1
        if any(c in string.punctuation for c in password):
            char_types += 1
        
        if char_types == 4:
            return 3, "Excellent variety (all character types)"
        elif char_types == 3:
            return 2, "Good variety (3 character types)"
        elif char_types == 2:
            return 1, "Limited variety (2 character types)"
        return 0, "Poor variety (1 character type)"
    
    def assess_password(self, password: str) -> Dict:
        """
        Assess password strength and return detailed results.
        
        Args:
            password: The password to assess
            
        Returns:
            Dictionary containing score, strength level, and detailed feedback
        """
        if not password:
            return {
                'score': 0,
                'max_score': 0,
                'percentage': 0,
                'strength': 'Invalid',
                'feedback': ['Password cannot be empty'],
                'passed_checks': [],
                'failed_checks': ['Empty password']
            }
        
        checks = [
            ('Length', self.check_length(password)),
            ('Uppercase', self.check_uppercase(password)),
            ('Lowercase', self.check_lowercase(password)),
            ('Numbers', self.check_numbers(password)),
            ('Special Characters', self.check_special_characters(password)),
            ('Pattern Check', self.check_common_patterns(password)),
            ('Character Variety', self.check_character_variety(password))
        ]
        
        total_score = 0
        max_score = 0
        passed_checks = []
        failed_checks = []
        feedback = []
        
        for check_name, (score, message) in checks:
            # Determine max possible score for this check
            if check_name == 'Length':
                check_max = 3
            elif check_name == 'Character Variety':
                check_max = 3
            else:
                check_max = 2
            
            total_score += score
            max_score += check_max
            
            if score > 0:
                passed_checks.append(f"✓ {check_name}: {message}")
            else:
                failed_checks.append(f"✗ {check_name}: {message}")
            
            feedback.append(f"{check_name}: {message}")
        
        percentage = (total_score / max_score) * 100
        
        # Determine strength level
        if percentage >= 90:
            strength = 'Very Strong'
            color = '🟢'
        elif percentage >= 70:
            strength = 'Strong'
            color = '🟢'
        elif percentage >= 50:
            strength = 'Moderate'
            color = '🟡'
        elif percentage >= 30:
            strength = 'Weak'
            color = '🟠'
        else:
            strength = 'Very Weak'
            color = '🔴'
        
        return {
            'score': total_score,
            'max_score': max_score,
            'percentage': round(percentage, 1),
            'strength': strength,
            'color': color,
            'feedback': feedback,
            'passed_checks': passed_checks,
            'failed_checks': failed_checks
        }
    
    def get_recommendations(self, result: Dict) -> List[str]:
        """Generate recommendations based on assessment results."""
        recommendations = []
        
        if result['percentage'] < 100:
            if any('Too short' in check for check in result['failed_checks']):
                recommendations.append(f"Increase length to at least {self.recommended_length} characters")
            
            if any('No uppercase' in check for check in result['failed_checks']):
                recommendations.append("Add uppercase letters (A-Z)")
            
            if any('No lowercase' in check for check in result['failed_checks']):
                recommendations.append("Add lowercase letters (a-z)")
            
            if any('No numbers' in check for check in result['failed_checks']):
                recommendations.append("Add numbers (0-9)")
            
            if any('No special characters' in check for check in result['failed_checks']):
                recommendations.append("Add special characters (!@#$%^&*)")
            
            if any('Weak patterns' in check for check in result['failed_checks']):
                recommendations.append("Avoid common patterns and words")
        
        return recommendations


def print_results(password: str, result: Dict, recommendations: List[str]):
    """Print formatted assessment results."""
    print("\n" + "="*60)
    print("PASSWORD STRENGTH ASSESSMENT")
    print("="*60)
    print(f"\nPassword: {'*' * len(password)}")
    print(f"\nStrength: {result['color']} {result['strength']}")
    print(f"Score: {result['score']}/{result['max_score']} ({result['percentage']}%)")
    
    # Progress bar
    bar_length = 40
    filled = int(bar_length * result['percentage'] / 100)
    bar = '█' * filled + '░' * (bar_length - filled)
    print(f"[{bar}] {result['percentage']}%")
    
    print("\n" + "-"*60)
    print("DETAILED FEEDBACK")
    print("-"*60)
    
    if result['passed_checks']:
        print("\n✓ Passed Checks:")
        for check in result['passed_checks']:
            print(f"  {check}")
    
    if result['failed_checks']:
        print("\n✗ Failed Checks:")
        for check in result['failed_checks']:
            print(f"  {check}")
    
    if recommendations:
        print("\n" + "-"*60)
        print("RECOMMENDATIONS")
        print("-"*60)
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. {rec}")
    
    print("\n" + "="*60 + "\n")


def main():
    """Main function to run the password strength checker."""
    checker = PasswordStrengthChecker()
    
    print("="*60)
    print("PASSWORD STRENGTH CHECKER")
    print("="*60)
    print("\nThis tool assesses password strength based on:")
    print("  • Length (minimum 8, recommended 12+)")
    print("  • Uppercase letters (A-Z)")
    print("  • Lowercase letters (a-z)")
    print("  • Numbers (0-9)")
    print("  • Special characters (!@#$%^&*)")
    print("  • Pattern analysis (avoiding common weak patterns)")
    print("  • Character variety")
    print("\n" + "="*60)
    
    while True:
        print("\nEnter a password to check (or 'quit' to exit):")
        password = input("> ").strip()
        
        if password.lower() == 'quit':
            print("\nThank you for using Password Strength Checker!")
            break
        
        result = checker.assess_password(password)
        recommendations = checker.get_recommendations(result)
        print_results(password, result, recommendations)


if __name__ == "__main__":
    main()
