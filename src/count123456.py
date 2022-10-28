nums = []
for i in ['+','-','*','/']:
    for j in ['+','-','*','/']:
        for k in ['+','-','*','/']:
            for l in ['+','-','*','/']:
                for m in ['+','-','*','/']:
                    num = eval("1" f"{i}" "2" f"{j}" "3" f"{k}" "4" f"{l}" "5" f"{m}" "6")
                    if(num%1 == 0 and num > 0):
                        nums.append(num)
                        print("1" f"{i}" "2" f"{j}" "3" f"{k}" "4" f"{l}" "5" f"{m}" "6",num)

nums.sort()
print(nums)   
