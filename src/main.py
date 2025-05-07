from textnode import TextNode, TextType

def main():
    test = TextNode("some test text", TextType.BOLD, "http://suckdeez.com")
    print(test)


if __name__ == "__main__":
    main()  
