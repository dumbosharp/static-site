from textnode import TextType, TextNode
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_node = []
    for node in old_nodes:

        if node.text_type != TextType.NORMAL:
            new_node.append(node)
            continue

        text = node.text
        processed_text = []

        while delimiter in text:

            start_idx = text.find(delimiter)
            end_idx = text.find(delimiter, start_idx + len(delimiter))

            if end_idx == -1:
               raise Exception("Invalid markdown: missing closing delimiter")

            before = text[:start_idx]
            content  = text[start_idx + len(delimiter): end_idx]
            after = text[end_idx + len(delimiter):]

            if before:
                processed_text.append(TextNode(before, TextType.NORMAL))
            processed_text.append(TextNode(content, text_type))

            text = after

        if text:    
            processed_text.append(TextNode(text, TextType.NORMAL))

        new_node.extend(processed_text)

    return new_node


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_image(old_nodes):
    
    new_node = []
    
    for node in old_nodes:

        if node.text_type != TextType.NORMAL:
            new_node.append(node)
            continue
        
        text = node.text
        images = list(extract_markdown_images(node.text))
        process_text = []

        while images:

            start_idx = text.find(f"![{images[0][0]}]({images[0][1]})")
            end_idx = start_idx + len(f"![{images[0][0]}]({images[0][1]})")

            before = text[:start_idx]
            after = text[end_idx:]

            if before:
                process_text.append(TextNode(before, TextType.NORMAL))
            process_text.append(TextNode(images[0][0], TextType.IMAGE, images[0][1]))

            text = after
            del images[0]

        if text:
            process_text.append(TextNode(text, TextType.NORMAL))

        new_node.extend(process_text)

    return new_node



def split_nodes_link(old_nodes):
    
    new_node = []
    
    for node in old_nodes:

        if node.text_type != TextType.NORMAL:
            new_node.append(node)
            continue
        
        text = node.text
        links = list(extract_markdown_links(node.text))
        process_text = []

        while links:

            start_idx = text.find(f"[{links[0][0]}]({links[0][1]})")
            end_idx = start_idx + len(f"[{links[0][0]}]({links[0][1]})")

            before = text[:start_idx]
            after = text[end_idx:]

            if before:
                process_text.append(TextNode(before, TextType.NORMAL))
            process_text.append(TextNode(links[0][0], TextType.LINK, links[0][1]))

            text = after
            del links[0]

        if text:
            process_text.append(TextNode(text, TextType.NORMAL))

        new_node.extend(process_text)

    return new_node


def text_to_textnodes(text):
    
    return split_nodes_delimiter(split_nodes_delimiter(split_nodes_link(split_nodes_image(split_nodes_delimiter([TextNode(text, TextType.NORMAL)], "`", TextType.CODE))), "_", TextType.ITALIC), "**", TextType.BOLD)

