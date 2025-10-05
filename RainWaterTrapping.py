
def cal_watera(arr ,al) :

    l_tall = [0] * al
    r_tall = [0] * al

    water = 0

    l_tall[0] = arr[0]
    for i in range(1,al) :

        l_tall[i] = max(l_tall[i -1 ] , arr[i])


    r_tall[al-1] = arr[al-1]
    for i in range(al - 2 , -1 , -1) :
        r_tall[i] = max(r_tall[i + 1] , arr[i])

    
    for i in range(0, al) :
        water += min(l_tall[i] , r_tall[i]) - arr[i]

    return water

a = [ 1,2,3,2,3,1]
bars = len(a)

print(cal_watera(a , bars))