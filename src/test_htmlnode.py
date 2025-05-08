import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextType, TextNode

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
            # Assuming you've already imported your classes

    def test_nested_parent_nodes(self):
        # Create a structure like:
        # <div>
        #   <p>Hello <b>World</b></p>
        #   <span>Test</span>
        # </div>
    
        # First, create the innermost node
        bold_node = LeafNode("b", "World")
    
        # Create a paragraph with text and the bold node
        hello_node = LeafNode(None, "Hello ")
        paragraph = ParentNode("p", [hello_node, bold_node])
    
        # Create a span node
        span_node = LeafNode("span", "Test")
    
        # Create the root div containing the paragraph and span
        div_node = ParentNode("div", [paragraph, span_node])
    
        # The expected HTML would be:
        expected = "<div><p>Hello <b>World</b></p><span>Test</span></div>"
    
        # Test if your to_html method produces the expected result
        actual = div_node.to_html()
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")
        print(f"Match: {expected == actual}")

    def test_complex_nested_parent_nodes_with_props(self):
        home_link = LeafNode("a", "Home", {"href": "/"})
        about_link = LeafNode("a", "About", {"href": "/about"})
    
        home_li = ParentNode("li", [home_link])
        about_li = ParentNode("li", [about_link])
    
        nav_ul = ParentNode("ul", [home_li, about_li])
    
        nav = ParentNode("nav", [nav_ul], {"class": "navigation"})
    
        h1 = LeafNode("h1", "My Website")
    
        header = ParentNode("header", [h1, nav], {"id": "main-header"})
    
        highlight_span = LeafNode("span", "my website", {"class": "highlight"})
        welcome_text_start = LeafNode(None, "Welcome to ")
        welcome_text_end = LeafNode(None, "!")
    
        welcome_p = ParentNode("p", [welcome_text_start, highlight_span, welcome_text_end])
    
        content_section = ParentNode("section", [welcome_p], {"class": "content"})
    
        container_div = ParentNode("div", [header, content_section], {"class": "container"})
    
        expected = (
            '<div class="container">'
                '<header id="main-header">'
                    '<h1>My Website</h1>'
                    '<nav class="navigation">'
                        '<ul>'
                            '<li><a href="/">Home</a></li>'
                            '<li><a href="/about">About</a></li>'
                        '</ul>'
                    '</nav>'
                '</header>'
                '<section class="content">'
                    '<p>Welcome to <span class="highlight">my website</span>!</p>'
                '</section>'
            '</div>'
        )
    
        actual = container_div.to_html()
        self.assertEqual(actual, expected) 

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
