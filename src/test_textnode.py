import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("this is a text node", TextType.BOLD)
        node2 = TextNode("this is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("this is a text node", TextType.BOLD, "http://deeznutsinyomouth.primeagen")
        node2 = TextNode("this is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_diff_type(self): 
        node = TextNode("this is a text node", TextType.NORMAL, "http://deeznutsinyomouth.primeagen")
        node1 = TextNode("this is a text node", TextType.BOLD, "http://deeznutsinyomouth.primeagen")
        self.assertNotEqual(node, node1)

if __name__ == "__main__":
    unittest.main()
