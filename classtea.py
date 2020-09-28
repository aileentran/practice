class Tea(object):
	def __init__(self, name, tea_type, region):
		self.name = name
		self.region = region
		self.tea_type = tea_type
		self.temperature = 0

	def get_name(self):
		return self.name

	def get_region(self):
		return self.region

	def tea_temperature(self):
		if self.region == 'Japan' and self.tea_type == 'gyokuro':
			self.temperature = 122

		elif self.region == 'Japan' and self.tea_type == 'sencha':
			self.temperature = 160

		elif self.tea_type == 'green' and self.region != 'Japan':
			self.temperature = 175

		elif self.tea_type == 'oolong' and self.region != 'Japan':
			self.temperature = 195

		elif self.tea_type == 'black' and tea_type == 'puerh' and self.region != 'Japan':
			self.temperature = 212

		return self.temperature

	def __str__(self):
		return str(self.name) + ' ' + str(self.region)

# def teaware(teas):


gyokuro = Tea('yame gyokuro', 'gyokuro', 'Japan')
fukamushi = Tea('takumi fukamushi', 'sencha', 'Japan')
baozhong = Tea('baozhong', 'oolong', 'China')
# print(gyokuro.get_region())
print(gyokuro.tea_temperature())
print(fukamushi.tea_temperature())
print(baozhong.tea_temperature())