#coding:utf-8
#斐波那契算法、递归

'''
fibonacci数列增长速度几乎与2的幂增长的速度相当：
当F30就已经超过了100万，F100已经达到的21位数字;所以通过递归算取第N位fibonacci数字效率十分低下。
当我们拥有一个算法，必须考虑三个方面：
1.它正确吗？
2.他将耗费多少是将，其耗费关于n是一个什么样的函数？
3.我们能否进行改进？
'''

#不好的算法、递归
def fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

print fibonacci(3)
print fibonacci(20)
print fibonacci(30)
print fibonacci(40)

#修改算法1：
##添加一个中间层——列表随时储存中间计算结果
def fibonacci1(n):
	f = []
	for i in range(n+1):
		if i == 0 or i ==1:
			f.append(i)
		else:
			f.append(f[i-1]+f[i-2])
	return f[-1]

print fibonacci1(3)
print fibonacci1(20)
print fibonacci1(30)
print fibonacci1(40)	

