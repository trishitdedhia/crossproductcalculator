

#Start collecting Vector A values
#Get ai
print("Enter Vector A's 'i' value");
ai = input();
# 'print("\033c")' will clear screen in Terminal
print("\033c");

#Get aj
print("Enter Vector A's 'j' value");
aj = input();
# 'print("\033c")' will clear screen in Terminal
print("\033c");

#Get ak
print("Enter Vector A's 'k' value");
ak = input();
# 'print("\033c")' will clear screen in Terminal
print("\033c");

#Start collecting Vector B values
#Get bi
print("Enter Vector B's 'i' value");
bi = input();
# 'print("\033c")' will clear screen in Terminal
print("\033c");

#Get bj
print("Enter Vector B's 'j' value");
bj = input();
# 'print("\033c")' will clear screen in Terminal
print("\033c");

#Get bk
print("Enter Vector  B's 'k' value");
bk = input();
# 'print("\033c")' will clear screen in Terminal
print("\033c");

#Processing
#Calculate i
i = (aj * bk) - (ak * bj);

#Calculate j
j = -((ai * bk) - (ak * bi));

#Calculate i
k = (ai * bj) - (aj * bi);

#Convert the values to strings
x = str(i) + 'i';


#j to y
if j < 0 :
    y = str(j) + 'j';
else:
    y = '+' + str(j) + 'j';


#k to z
if k < 0 :
    z = str(k) + 'k';
else:
    z = '+' + str(k) + 'k';



#Show result
print('The cross product is ' + x + y + z);
