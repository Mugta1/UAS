two=[]
three=[]
four=[]
append=[]
input=[]
def output(a):
    #try1.py will return values
    #number of red houses on fire
    rf=4
    #number of blue houses on fire
    bf=2
    #number of red houses not on fire
    rg=1
    #number of blue houses not on fire
    bg=3
    name=a ##a passed as name of file in parameter of the function
    Hb=rf+bf
    Hg=rg+bg
    list2=[Hb, Hg]
    Pb=rf*1+bf*2
    Pg=rg*1+bg*2
    list3=[Pb, Pg]
    Pr=Pb/Pg
    results=[name, list2, list3, Pr]
    return results
def collectoutput(list):
    for i in list:
        x=output(i)
        two.append(x[1])
        three.append(x[2])
        four.append(x[3])
        input.append([x[0], x[3]])
def get_float(pair):
    return pair[1]

def arrange_by_float_descending(input):
    sorted_pairs = sorted(input, key=get_float, reverse=True)
    return sorted_pairs
collectoutput(list)
print('2. ', two)
print('3. ', three)
print('4. ', four)
sorted_output = arrange_by_float_descending(input)

for name, value in sorted_output:
    print(f"{name}")

    



