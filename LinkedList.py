class Node():
  def __init__(self, val):
    self.val = val
    self.next = None
  
  def get_data(self):
    return self.val
  
  def set_data(self, val):
    self.val = val
  
  def get_next(self):
    return self.next
  
  def set_next(self, next):
    self.next = next
 

class LinkedList():
  def __init__(self, head=None):
    self.head = head
    self.count = 0
  
  def get_count(self):
    return self.count
  
  def insert(self, data):
    # TODO
    new_node = Node(data)
    new_node.set_next(self.head)
    self.head = new_node
    self.count += 1
  
  def find(self, val):
    # TODO
    item = self.head
    
    while (item != None):
      if item.get_data() == val:
        return item
      else:
        item = item.get_next()

    return None
  
  def deleteAt(self, idx):
    # TODO
    if idx > self.count - 1:
      return
    
    if idx == 0:
      self.head = self.head.get_next()
    else:
      tempIdx = 0
      node = self.head
      while tempIdx < idx - 1:
        node = node.get_next()
        tempIdx += 1
      
      node.set_next(node.get_next().get_next())
      self.count -= 1


  
  def dump_list(self):
    tempnode = self.head
    while(tempnode != None):
      print("Node:", tempnode.get_data())
      tempnode = tempnode.get_next()
  
 
linkedList = LinkedList()

linkedList.insert(38)
linkedList.insert(49)
linkedList.insert(13)
linkedList.insert(15)

linkedList.dump_list()
linkedList.find(15).get_data()
linkedList.deleteAt(2)
