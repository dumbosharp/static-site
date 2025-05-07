import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "test text for test", ["test", "test", "test"], {"href": "google.com"})
        node2 = HTMLNode("p", "test text for test", ["test", "test", "test"], {"href": "google.com"})
        #print(node)
        #print(node2)
        self.assertEqual(node, node2)
    
    def test_none_eq(self):
        node = HTMLNode()
        node2 = HTMLNode()
        #print(node)
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("p", "test text for test", ["test", "test", "test"], {"href": "google.com", "target": "test"})
        node2 = HTMLNode("p", "test text for test", ["test", "test", "test"], {"href": "google.com", "target": "test"})
        test = node.props_to_html()
        test2 = node2.props_to_html()
        print(test)
        print(test2)
        self.assertEqual(test, test2)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, World!")
        self.assertEqual(node.to_html(), "<p>Hello, World!</p>")

    def test_leaf_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

if __name__ == "__main__":
    unittest.main()
