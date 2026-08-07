"""Tests for the Caesar cipher program."""

import unittest

from main import caesar_cipher


class CaesarCipherTests(unittest.TestCase):
    """Verify encryption, decryption, and input handling."""

    def test_encrypts_with_wraparound(self) -> None:
        self.assertEqual(caesar_cipher("XYZ", 3, "encrypt"), "ABC")

    def test_decrypts_with_wraparound(self) -> None:
        self.assertEqual(caesar_cipher("ABC", 3, "decrypt"), "XYZ")

    def test_preserves_case_and_non_letters(self) -> None:
        self.assertEqual(
            caesar_cipher("Hello, World! 123", 3, "encrypt"),
            "Khoor, Zruog! 123",
        )

    def test_round_trip_restores_original_message(self) -> None:
        original = "Meet me at 8:30 by Gate Z."
        encrypted = caesar_cipher(original, 11, "encrypt")
        self.assertEqual(caesar_cipher(encrypted, 11, "decrypt"), original)

    def test_zero_key_leaves_message_unchanged(self) -> None:
        self.assertEqual(caesar_cipher("No change!", 0, "encrypt"), "No change!")

    def test_rejects_key_outside_valid_range(self) -> None:
        with self.assertRaisesRegex(ValueError, "between 0 and 25"):
            caesar_cipher("Hello", 26, "encrypt")

    def test_rejects_unknown_mode(self) -> None:
        with self.assertRaisesRegex(ValueError, "encrypt.*decrypt"):
            caesar_cipher("Hello", 3, "rotate")


if __name__ == "__main__":
    unittest.main()
