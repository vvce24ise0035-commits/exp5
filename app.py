import unittest

def add(a, b):
    return a + b

def main():
    print("Hello! Python application is running successfully.")
    print("Addition of 10 and 20 =", add(10, 20))

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 20), 30)

if __name__ == "__main__":
    main()
