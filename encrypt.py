def _get_hex(string):
	result = []
	for item in string:
		result.append(hex(ord(item))[2:])
	string2 = ''
	for i in result:
		string2 += str(i)
	return string2
class encrypt():
	def __init__(self,PreStr):
		self.string = PreStr
		self.bit = 32
		self.hexV = ''
		self.HV = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15,'x':0,'d':0}
		print('your string is:%s'%_get_hex(self.string))
	def __str__(self):
		return self.Encrypt()
	def _hexadd(self,*arg):
		hexNum = ''
		sumNum = 0
		for i in arg:
			sumNum += self.HV[i]
		hexNum = hex(sumNum)
		return hexNum
	def _hex_bin(self,char):
		return bin(self.HV[char])
	def _c(self,char):
		if(char <  '一' or char > '龥'):
			return False
		return True
	def Encrypt(self):
		self.add()
		self.ENCRYPT()
		self.compress()
		return self.hexV
	def add(self):
		hexval = _get_hex(self.string)
		for i in range(self.bit - len(hexval)):
			if(i == 0):
				hexval += '1'
			else:
				hexval += '0'
		self.hexV = hexval
	def _add_enc(self,addval1,addval2):
		hexval = _get_hex(self.string)
		for i in range(self.bit - len(hexval)):
			if(i == 0):
				hexval += addval1
			else:
				hexval += addval2
		self.hexV = hexval
	def compress(self):
		compressed = ''
		for i in range(self.bit):
			if(i + 1 == self.bit):
				compressed += self.hexV[-1]
			elif(i + 2 == self.bit):
				compressed += self._hexadd(self.hexV[i],self.hexV[i + 1])
			else:
				compressed += self._hexadd(self.hexV[i],self.hexV[i + 1],self.hexV[i + 2])
		self.hexV = compressed
	def ENCRYPT(self):
		num = 0
		while(num <= self.bit):
			num += 1
			self._add_enc('f','1')
			self.compress()
		self.add()
		self.compress()