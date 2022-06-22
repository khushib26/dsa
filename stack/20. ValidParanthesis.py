class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        
        stack = []
        
        for i in s:
            if (i=="{" or i=="(" or i=="["):
                stack.append(i)
            else:
                if(stack):
                    x = stack.pop()
                    if((i=="}" and x=="{" or i==")" and x=="(" or i=="]" and x=="[")):
                        continue
                    else:
                        return False
                else:
                    return False
        
        if(not stack):
            return True
        else:
            return False
