from enum import Enum

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


class BlockType(Enum):
   PARAGRAPH = "paragraph"
   HEADING = "heading"
   CODE = "code"
   QUOTE = "quote"
   UNORDERED = "unordered list"
   ORDERED = "ordered list"


def block_to_block_type(block):

   if block[:3] == "```" and block[-3:] == "```":
      return BlockType.CODE

   if block[0] == "#":
      count = 0
      for char in block[:6]:
         if char == "#":
            count += 1
      if block[count] == " " and block[count + 1:].isspace() == False:
         return BlockType.HEADING
   
   split_block = block.splitlines()

   ordered_list = True
   quote = True
   unordered = True
   line_number = 1

   for line in split_block:
      if f"{line_number}. " != line[:len(f"{line_number}. ")]:
         ordered_list = False
      if line[0] != ">":
         quote = False
      if line[:2] != "- ":
         unordered = False
      line_number += 1

   if ordered_list == True:
      return BlockType.ORDERED
   if quote == True:
      return BlockType.QUOTE
   if unordered == True:
      return BlockType.UNORDERED

   return BlockType.PARAGRAPH

