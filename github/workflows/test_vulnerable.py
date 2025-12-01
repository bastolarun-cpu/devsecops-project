# Test file with vulnerabilities for Bandit to find

import os
import subprocess
import hashlib

# Vulnerability 1: Hardcoded password
password = "admin123"

# Vulnerability 2: Command injection risk
def execute_command(cmd):
    os.system(cmd)  # Unsafe!

# Vulnerability 3: Weak hash
def hash_password(pwd):
    return hashlib.md5(pwd.encode()).hexdigest()

# Vulnerability 4: SQL injection pattern
def query_db(user_input):
    query = f"SELECT * FROM users WHERE name = '{user_input}'"
    return query
