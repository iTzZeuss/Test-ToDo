from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher(time_cost=5, memory_cost=1048576, parallelism=8) # settings are secure af

def generate_password_hash(password:str) -> str:
    """For stupid ones: hashes password"""
    return ph.hash(password)

def verify_password_hash(password:str, hash_:str) -> bool:
    """Verifys password. if Succeded - True , Failed - false"""
    try:
        ph.verify(hash_, password)
        return True  # Verification succeeded
    except VerifyMismatchError:
        return False  # Verification failed
    # idk why argon2 makes exceptions when failed to verify... thats wierd... anyway it works

import re

def load_common_passwords(file_path):
    """Load shity passwords from a text file into a set"""
    try:
        with open(file_path, 'r') as file:
            common_passwords = set(line.strip() for line in file)
        return common_passwords
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return set()

def analyze_password_strength(password, common_passwords):
    """Check how fucked your password is"""
    if password in common_passwords:
        return "Password is too common and unsafe."

    criteria = {
        'length': len(password) >= 12,  # Minimum length
        'uppercase': bool(re.search(r'[A-Z]', password)),  # Contains uppercase letter
        'lowercase': bool(re.search(r'[a-z]', password)),  # Contains lowercase letter
        'digit': bool(re.search(r'[0-9]', password)),  # Contains digit
        'symbol': bool(re.search(r'[@#$%^&+=!]', password)),  # Contains symbols
    }

    strength_score = sum(criteria.values())
    
    feedback = []
    if not criteria['length']:
        feedback.append("Password must be at least 12 characters long.")
    if not criteria['uppercase']:
        feedback.append("Password must contain at least one uppercase letter.")
    if not criteria['lowercase']:
        feedback.append("Password must contain at least one lowercase letter.")
    if not criteria['digit']:
        feedback.append("Password must contain at least one digit.")
    if not criteria['symbol']:
        feedback.append("Password must contain at least one special character (e.g., @, #, $, etc.).")

    if strength_score == len(criteria):
        return "Password is strong."
    else:
        return "Password is weak. " + " ".join(feedback)

def check_password_requirements(password:str):
    common_passwords = load_common_passwords('common_password_list.txt')
    result = analyze_password_strength(password, common_passwords)
    return result

check_password_requirements()