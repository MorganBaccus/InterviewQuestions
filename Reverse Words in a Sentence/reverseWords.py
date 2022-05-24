# Option 1
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        temp = []
		
        i=0
        while(i < len(s)):	
			# accumulate chars forming words
            word = ""
            while(i<len(s) and s[i]!=" "):
                word += s[i]
                i += 1
			# if word not empty append to stack
            if(word!=""):
                temp.append(word)
            i+=1
			
		# pop from stack and add to final answer
        word = ""
        while(temp):
            word = word+temp.pop()+" "
			
		# remove extra space at the end and return
        return word.rstrip()


# Option 2
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        revStr = ""
        words = s.split()
        
        for w in words[::-1]:
            revStr += w + " "
            
        revStr = revStr[:-1]
            
        return revStr
