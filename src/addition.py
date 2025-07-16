# app.py

def add(a: int, b: int) -> int:
    """
    Returns the sum of two numbers.

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: Sum of a and b.
    """
    return a + b


def test_add():
    """
    Unit tests for the add function.
    """
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    assert add(0, 0) == 0
    assert add(-5, -3) == -8
    assert add(1000, 2000) == 3000


if __name__ == "__main__":
    test_add()
    print("✅ All tests passed.")
