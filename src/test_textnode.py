import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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

    def test_text(self):
            node = TextNode("This is a text node", TextType.NORMAL)
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, None)
            self.assertEqual(html_node.value, "This is a text node")
     
    def test_bold(self):
        node = TextNode("This is bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold text")

    def test_italic(self):
        node = TextNode("This is italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic text")

    def test_code(self):
        node = TextNode("This is code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code")

    def test_link(self):
        # Assuming TextNode constructor accepts url as a parameter
        node = TextNode("Click me", TextType.LINK)
        node.url = "https://example.com"  # Set url property
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click me")
        self.assertEqual(html_node.props["href"], "https://example.com")

    def test_image(self):
        # Assuming TextNode constructor accepts url as a parameter
        node = TextNode("Alt text", TextType.IMAGE)
        node.url = "image.png"  # Set url property
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "image.png")
        self.assertEqual(html_node.props["alt"], "Alt text")


if __name__ == "__main__":
    unittest.main()
