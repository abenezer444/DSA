class Solution:
    def interpret(self, command: str) -> str:
        ans=""
        for i in range(len(command)):
            if command[i]=="G":
                ans+="G"
            elif command[i]=="(":
                if command[i+1]=="a":
                    ans+="al"
                else:
                    ans+="o"
        return ans
            
        
                
            