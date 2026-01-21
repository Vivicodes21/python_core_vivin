import sys
import pathlib

# Make src/ importable when running tests from the repository root
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

import unittest

from python_core_vivin import add


class TestUtils(unittest.TestCase):
    def test_add_integers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_floats(self):
        self.assertAlmostEqual(add(1.5, 2.25), 3.75)

    def test_add_invalid(self):
        with self.assertRaises(TypeError):
            add("one", 2)


if __name__ == "__main__":
    unittest.main()
