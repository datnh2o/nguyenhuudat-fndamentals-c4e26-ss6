#7
def remove_dollar_sign(s):
    if "$" in list(str(s)):
        print(str(s).replace("$",""))
        return str(s).replace("$","")
#8
string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")
#9
def get_even_list(l):
    sochan = []
    for i in l:
        if i%2==0:
            sochan.append(i)
    print("Số chắn: ",*sochan, sep=", ")
l = [1, 2, 3, 4, 5, 6, 7]

get_even_list(l)
#10
def get_even_list(l):
    sochan = []
    for i in l:
        if  i%2==0:
            sochan.append(i)
    return sochan

even_list = get_even_list([1, 2, 3, 5, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
#11
#em chưa hiểu đề bài cho lắm =)    
