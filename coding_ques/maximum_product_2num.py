n = 1245

def max_product(n: int):
    n = str(n)
    i,j=0,1
    max_prod = -999999
    if len(n) == 1:
        return int(n)
    while i<len(n) and j<len(n):
        prod = int(n[i])*int(n[j])
        # print(prod)
        if prod >= max_prod:
            max_prod = prod
        if j == len(n)-1:
            prod = int(n[i])*int(n[j])
            if prod >= max_prod:
                max_prod = prod
            i += 1
            j = i
            print(i)
        j += 1
        
    return max_prod

ans = max_product(n)
print(ans)