def rob(self, num):
    if len(num) == 0:
        return 0
        
    if len(num) == 1:
        return num[0]
    
    num_i, num_i_1 = max(num[1], num[0]), num[0]
    for i in range(2, len(num)):
        num_i_1, num_i_2 = num_i, num_i_1
        num_i = max(num[i] + num_i_2, num_i_1);
    
    return num_i