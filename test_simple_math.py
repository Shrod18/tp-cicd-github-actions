"""Tests unitaires pour la classe SimpleMath."""

import unittest
from simple_math import SimpleMath


class TestSimpleMath(unittest.TestCase):
    """Classe de tests pour SimpleMath."""

    def test_addition_positive_numbers(self):
        """Test de l'addition avec des nombres positifs."""
        result = SimpleMath.addition(5, 3)
        self.assertEqual(result, 8)

    def test_addition_negative_numbers(self):
        """Test de l'addition avec des nombres négatifs."""
        result = SimpleMath.addition(-5, -3)
        self.assertEqual(result, -8)

    def test_addition_mixed_numbers(self):
        """Test de l'addition avec des nombres mixtes."""
        result = SimpleMath.addition(-5, 10)
        self.assertEqual(result, 5)

    def test_addition_zero(self):
        """Test de l'addition avec zéro."""
        result = SimpleMath.addition(5, 0)
        self.assertEqual(result, 5)

    def test_soustraction_positive_numbers(self):
        """Test de la soustraction avec des nombres positifs."""
        result = SimpleMath.soustraction(10, 3)
        self.assertEqual(result, 7)

    def test_soustraction_negative_numbers(self):
        """Test de la soustraction avec des nombres négatifs."""
        result = SimpleMath.soustraction(-5, -3)
        self.assertEqual(result, -2)

    def test_soustraction_mixed_numbers(self):
        """Test de la soustraction avec des nombres mixtes."""
        result = SimpleMath.soustraction(5, 10)
        self.assertEqual(result, -5)

    def test_soustraction_zero(self):
        """Test de la soustraction avec zéro."""
        result = SimpleMath.soustraction(5, 0)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
