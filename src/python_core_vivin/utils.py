"""Utility functions for python_core_vivin

Keep functions small and well-tested.
"""

def add(a, b):
    """Return the sum of two numbers.

    Accepts ints and floats. Raises TypeError for unsupported types.
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("add() expects numbers")
    return a + b
