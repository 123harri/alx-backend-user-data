#!/usr/bin/env python3
"""Module for password hashing and validation.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt.

    Args:
        password (str): The plain text password to hash.

    Returns:
        bytes: The hashed password.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks if a hashed password matches the given plain text password.

    Args:
        hashed_password (bytes): The hashed password.
        password (str): The plain text password to check.

    Returns:
        bool: True if the password matches, False otherwise.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
