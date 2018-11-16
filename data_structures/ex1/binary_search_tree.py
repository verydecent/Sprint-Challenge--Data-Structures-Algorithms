class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    #  Call cb on current node
    cb(self.value)
    # if there is a left recursive call
    if self.left:
        self.left.depth_first_for_each(cb)
    # If there is a right recursive call
    if self.right:
        self.right.depth_first_for_each(cb)    

  def breadth_first_for_each(self, cb):
    # Use a ds like a queue
    queue = []
    # add root node
    queue.append(self)
    # iterate over queue and call function
    while len(queue) > 0:
        current = queue[0]
        cb(current.value)
        # pop out of queue
        queue.pop(0)
        # if there is a left node add to queue
        if current.left:
            queue.append(current.left)
        # if there is a right node append to queue
        if current.right:
            queue.append(current.right)

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
