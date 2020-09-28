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

def teaware(teas, tea_is_cold):
	"""Based on list of teas and if your tea tends to go cold, suggest teaware"""

	for tea in teas:
		if tea.get_region() == 'Japan':
			return 'kyusu'

		if tea_is_cold == True:
			return 'tea pot or gaiwan'

		if tea_is_cold == False:
			return 'CHUG A MUG! Enjoy :)'
		

gyokuro = Tea('yame gyokuro', 'gyokuro', 'Japan')
fukamushi = Tea('takumi fukamushi', 'sencha', 'Japan')
baozhong = Tea('baozhong', 'oolong', 'China')
assam = Tea('assam', 'black', 'India')
teas = [baozhong, assam]

print(teaware(teas, False))