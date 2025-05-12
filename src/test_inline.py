import unittest
from textnode import TextNode, TextType
from inline_markdown import *  # Replace with your actual module name

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
        self.assertEqual(result[0].text, "Text with ")
        self.assertEqual(result[1].text, "code")
        self.assertEqual(result[2].text, " and more ")
        self.assertEqual(result[3].text, "code blocks")

    def test_extract_markdown_images(self):

        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        matches1 = extract_markdown_images(
            "this is a big test  ![!@#$%^)^*)(}{](!@#$%^&*_+=-0987654321)"
        )
        
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        self.assertListEqual([("!@#$%^)^*)(}{", "!@#$%^&*_+=-0987654321")], matches1)


    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
