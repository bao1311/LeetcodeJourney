# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, tra: str) -> Optional[TreeNode]:
        n = len(tra)
        '''
        1-2--3--4-5--6--7
                1
            2       5
        3     4    6    7
        '''

        # i = 0
        # stack = []
        # while i < n:
        #     lvl = 0
        #     while i < n and tra[i] == '-':
        #         i += 1
        #         lvl += 1
        #     val = ""
        #     while i < n and tra[i] != '-':
        #         val += tra[i]
        #         i += 1
        #     while len(stack) > lvl:
        #         stack.pop()
        #     cur = TreeNode(int(val))
        #     if stack and not stack[-1].left:
        #         stack[-1].left = cur
        #     elif stack:
        #         stack[-1].right = cur
        #     stack.append(cur)
        # return stack[0]
        # Approach 2: Recursive
        n = len(tra)
        i = 0
        def help(h):
            nonlocal i
            lvl = 0
            nxt = 0
            while i+nxt < n and tra[i+nxt] == '-':
                lvl += 1
                nxt += 1
            val = ''
            
            if nxt != h:
                return None
            i += nxt
            while i < n and tra[i] != '-':
                val += tra[i]
                i += 1
            root = TreeNode(int(val))
            root.left = help(lvl+1)
            root.right = help(lvl+1)
            return root


        
        return help(0)

