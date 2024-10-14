while True:
    InputString = input("input string: ")
    shiftKey = int(input("input key for shift"))
    ShiftText = []
    CipherText = ""
    for x in InputString:
        if ord(x)+shiftKey>122:
            counter = 0;
            while ord(x)<122:
                ord(x)+1
                shiftKey-1
                counter+=1
            ShiftText.append(96+shiftKey)
            shiftKey +=counter
        else:
            ShiftText.append(ord(x)+shiftKey)
    for x in ShiftText:
        CipherText += chr(x)
    print(CipherText)
# currently appllies to spaces
#use full test
# for x in InputString:
#     ShiftText.append((ord(x)) + shiftKey);

