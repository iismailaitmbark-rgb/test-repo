#!/usr/bin/env python3
"""
A simple hello world script for testing purposes.
"""

def greet(name="World"):
    """Return a greeting message."""
    return f"Hello, {name}!"

def main():
    """Main function."""
    print(greet())
    print(greet("GitHub"))
    print(greet("Claude"))

if __name__ == "__main__":
    main()
