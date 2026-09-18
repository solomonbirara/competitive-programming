class Solution:
    def interpret(self, command: str) -> str:
        i=0
        text=""
        while i<len(command):
            if command[i]=="G":
                text+="G"
                i+=1
            elif command[i:i+2]=="()":
                text+="o"
                i+=2
            elif command[i:i+4]=="(al)":
                text+="al"
                i+=4
            else:
                break
        return text
