#A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
#Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

# matrix=[[1,2,3,4],[5,1,2,3],[9,5,1,2]]

# def isToeplitz(matrix):
# 	if matrix is not None:
# 		row = len(matrix)
# 		col = len(matrix[0])
		
# 		for i in range(row-1):
# 			for j in range(col-1):
# 				if matrix[i][j] != matrix[i+1][j+1]:
# 					return False
# 		return True


# print isToeplitz(matrix);

#***************************************two sum***************************************

#********SOLUTION 1**********

# arr = [1,3,5,6,8,4];
# indexes = [];

# def twosum():
#     for i in range(len(arr)):
#          for j in range(1,len(arr)):
#             for k in range(len(arr)):
#                 if arr[k] == arr[i] + arr[j] and i != j:
#                     print str(arr[i])+" + "+str(arr[j]) + " => " + str(arr[k])
#                     print str(i)+" "+str(j)+ " => " + str(k)
#                     indexes.append(i);
#                     indexes.append(j);
# twosum();
# print indexes;


#********SOLUTION 2**********
# arr = [1,3,5,6,8,4];
# indexes = [];
# target = 8;
# hash = {};

# def twosum():
#     for i in range(len(arr)):
#         if hash.has_key(arr[i]):
#             return hash[arr[i]],i
#         toNum = target - arr[i];
#         hash[toNum] = i;

# print twosum();
# print hash

#***************************************REVERSE DIGIT***************************************
#1.digit = num%10
#2.rev = rev*10 + digit
#3.num = num/10
#when num != 0
#32bit signed   -2^16 -  2^16 - 1

# num = 12345
# num1 = -12345
# revNum = 0;
# def reverseDigit(num):
# 	global revNum;

# 	isNeg = False;
# 	if(num < 0):
# 		isNeg = True;
# 		num = -num;

# 	while num != 0:
# 		digit = num%10;
# 		revNum = revNum*10 + digit;
# 		num = num / 10;

# 	if(isNeg):
# 		revNum = -revNum;

# 	if revNum > pow(2,16) - 1 or revNum < -pow(2,16):
# 		return 0;

# 	return revNum;
# print reverseDigit(429496729);

# python和java中的不同
# python取余遵循 a%b = a-(a//b)*b   其中 a//b 为math.floor()操作,数字的正负和被除数有关

# 相关资料
# 唯一不同点，就是商向0或负无穷方向取整的选择，c从c99开始规定向0取整，python则规定向负无穷取整，选择而已。

# 向零取值的含义是：9/7=1 .29----向0取值-->1；-9/7=-1.29----向0取值------>-1

# 向负无穷取值的含义是：9/7=1 .29----向0取值-->1；-9/7=-1.29----向0取值------>-2

