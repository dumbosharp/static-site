def markdown_to_blocks(markdown):
   blocks = markdown.split("\n\n")
   good_blocks = [block.strip() for block in blocks if block.strip()]
   best_blocks = []
   for block in good_blocks:
      lines = block.splitlines()
      container = []
      for line in lines:
         container.append(line.strip())
      best_blocks.append("\n".join(container))
   return best_blocks
