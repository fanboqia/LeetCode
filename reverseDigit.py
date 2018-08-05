
#thinking process
# 1.digit = num%10
# 2.rev = rev*10 + digit
# 3.num = num/10
# when num != 0
# 32bit signed   -2^16 -  2^16 - 1

num = 12345
num1 = -12345
revNum = 0;
def reverseDigit(num):
	global revNum;

	isNeg = False;
	if(num < 0):
		isNeg = True;
		num = -num;

	while num != 0:
		digit = num%10;
		revNum = revNum*10 + digit;
		num = num / 10;

	if(isNeg):
		revNum = -revNum;

	if revNum > pow(2,16) - 1 or revNum < -pow(2,16):
		return 0;

	return revNum;
print reverseDigit(429496729);

#************** PROBLEM DETECTED **************
#                  modulus
# python和java中的不同
# python取余遵循 a%b = a-(a//b)*b   其中 a//b 为math.floor()操作,数字的正负和被除数有关

#************** RELEVANT FILES *************
# 唯一不同点，就是商向0或负无穷方向取整的选择，c从c99开始规定向0取整，python则规定向负无穷取整，选择而已。

# 向零取值的含义是：9/7=1 .29----向0取值-->1；-9/7=-1.29----向0取值------>-1

# 向负无穷取值的含义是：9/7=1 .29----向0取值-->1；-9/7=-1.29----向0取值------>-2

