
def cal_profit(arr , al) :

    profit = 0 

    for i in range(1 , al) :

        # if current element grater than last subtract the privious and add to pro fit

        if arr[i] > arr[i-1] :

            profit += arr[i] - arr[ i - 1]

    return profit

a = [635 , 864, 247, 325 , 257 , 745 , 245]

print(cal_profit(a , len(a)))