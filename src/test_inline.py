import unittest
from textnode import TextNode, TextType
from inline import split_nodes_delimiter  # Replace with your actual module name

class TestSplitNodesDelimiter(unittest.TestCase):
    
    def test_no_delimiters(self):
        # Test case with no delimiters
        node = TextNode("Just plain text", TextType.NORMAL)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "Just plain text")
        self.assertEqual(result[0].text_type, TextType.NORMAL)
    
    def test_one_delimiter_pair(self):
        # Test case with one pair of delimiters
        node = TextNode("Text with `code` in it", TextType.NORMAL)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "Text with ")
        self.assertEqual(result[0].text_type, TextType.NORMAL)
        self.assertEqual(result[1].text, "code")
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[2].text, " in it")
        self.assertEqual(result[2].text_type, TextType.NORMAL)
    
    def test_multiple_delimiter_pairs(self):
        # Test case with multiple pairs of delimiters
        node = TextNode("Text with `code` and more `code blocks`", TextType.NORMAL)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0].text, "Text with ")
        self.assertEqual(result[1].text, "code")
        self.assertEqual(result[2].text, " and more ")
        self.assertEqual(result[3].text, "code blocks")
