def reverseString(self, s: List[str]) -> None:
        j=-1
        for i in range(0,len(s)//2):
            t=s[i]
            s[i]=s[j]
            s[j]=t
            j-=1