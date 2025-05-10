from textnode import TextType, TextNode


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
            
        processed_text.append(TextNode(text, TextType.NORMAL))

        new_node.extend(processed_text)

    return new_node
