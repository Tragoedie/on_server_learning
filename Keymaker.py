def Keymaker(k):
    door_array = []
    for x in range(k):
        door_array.append('0')
    step = 1
    for i in range(k):
        j = step - 1
        while j < k:
            if door_array[j] == '1':
                door_array[j] = '0'
            else:
                door_array[j] = '1'
            j += step
        step = step + 1
    door_array = ''.join(door_array)
    return door_array

# def Keymaker_math(k):
    # door_array_m = []
    # for x in range(k):
        # door_array_m.append('0')
    # i = 1
    # while i * i < k:
        # door_array_m[i*i-1] = '1'
        # i += 1
    # door_array_m = ''.join(door_array_m)
    # return door_array_m

# def Keymaker_math_2(k):
    # door_array_m_2 = []
    # for x in range(k):
        # door_array_m_2.append('0')
    # for i in range(1, k):
        # if (pow(i, 0.5) - int(pow(i, 0.5))) < 0.00001:
            # door_array_m_2[i-1] = '1'
    # door_array_m_2 = ''.join(door_array_m_2)
    # return door_array_m_2


# print(Keymaker(1500))
# print(Keymaker_math(1500))
# print(Keymaker_math_2(1500))
