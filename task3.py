my_list = []
for i in range(0,5):
    my_list.append(int(input()))
print('Finish of the input')
shift_num = int(input())

while shift_num > 0:
    temp_value = my_list.pop()
    my_list.insert(0,temp_value)
    shift_num-=1
else:
    while shift_num <0: 
        temp_value = my_list.pop(0)
        my_list.append(temp_value)
        shift_num+=1
print (my_list)


