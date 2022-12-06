from collections import defaultdict
class Solution:

   def __init__(self, head_name):
      self.family = defaultdict(list)
      self.head = head_name
      self.dead = set()

   def birth(self, p_name, c_name):
      self.family[p_name].append(c_name)

   def death(self, name):
      self.dead.add(name)

   def inheritance(self):
      self.ans = []
      self.depth_search(self.head)
      return self.ans

   def depth_search(self, current):
      if current not in self.dead:
         self.ans.append(current)
      for child in self.family[current]:
         self.depth_search(child)

ob = Solution('Narasimha')
ob.birth('Narasimha', 'Ravi')
ob.birth('Narasimha', 'nithin')
ob.birth('nithin', 'rakesh')
ob.birth('nithin', 'Lakshmi Narayana')
ob.birth('nithin', 'Ram mohan')
ob.death('Narasimha')
print(ob.inheritance())
ob.death('Ravi')
print(ob.inheritance())
