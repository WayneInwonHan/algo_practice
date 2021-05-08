def myAtoi(self, s: str) -> int:
        int_min=-(2**31)
        int_max=(2**31)-1
        
        s=s.strip()
        
        first=None
        for character in s:
            if not first:
                if character.isdigit() or character in {'-','+'}: 
                    first=character
                else:
                    break
            else: 
                if character.isdigit():
                    first+=character
                else:
                    break
        
        if not first or first in {'-','+'}:
            first=0
        elif int(first)<int_min:
            first=int_min
        elif int(first)>int_max:
            first=int_max
            
        return int(first)