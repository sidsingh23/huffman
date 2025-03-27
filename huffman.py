#!/usr/local/bin/python3
import heapq
import sys
sys.path.append('/home/staff/kurban/python')

import csc220

csc220.showForm("This is the comment on the form area.")  

textarea = csc220.getInput('textarea')
textbox = csc220.getInput('textbox')

print ("<h2>This is at the bottom and can be used for any html output </h2><br>")

#Code below is from lecture slides

freq = {}  #empty map (dictionary)

for ch in textarea:
  if ch not in freq:
    freq[ch] = 0
  freq[ch] += 1  # KeyError: '5'
  #freq[ch] = freq.get(ch, 0) + 1

print("Character Frequency")
for [char, count] in freq.items():  #go through (key: value) pairs
  print ("{}: {}".format(char, count))

print("-----")
#My code

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    #for priority queue comparison
    def __lt__(self, next):
        return self.freq < next.freq



# building huffman tree
def huffman(freq):
    # priority queue a la frequency dictionary
    heap = [Node(char, i) for char, i in freq.items()]
    heapq.heapify(heap)

    # the node combiner
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        combine = Node(None, left.freq + right.freq)
        combine.left = left
        combine.right = right

        heapq.heappush(heap, combine)

    return heap[0] 



# generating da codes
def huffcodes(node, code="", codemap={}):
    # need to make sure we have actual values we want to use in our nodes
    if node is not None:
        if node.char is not None:
            codemap[node.char] = code

        huffcodes(node.left, code + "0", codemap)     # left of tree = 0
        huffcodes(node.right, code + "1", codemap)    # right of tree = 1
    return codemap


compressed = huffman(freq)
final = huffcodes(compressed)
print("Huffman Codes:", final)



# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Siddharth Singh