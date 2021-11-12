import unittest
from anagrams import split_text

cases = [
        ("abcd efgh", "dcba hgfe"),
        ("a1bcd efg!h", "d1cba hgf!e"),
        ("", ""),
        ("hn*b6 j34g@", "bn*h6 g34j@")

    ]


class TestAnagrams(unittest.TestCase):

    def test_char(self):
        for text, reversed_text in cases:
            self.assertEqual(split_text(text), reversed_text)

    def test_type(self):
        with self.assertRaises(TypeError) as e:
            split_text(132)
            split_text({1: "123"})
        self.assertEqual('work only with strings', e.exception.args[0])


if __name__ == '__main__':
    unittest.main()
