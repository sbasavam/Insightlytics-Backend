import bcrypt

# Hashes the given plain text password using bcrypt
def hash_password(password):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode()

# Verifies a plain text password against a previously hashed one
def check_password(password, hashed):
    return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))
