class Tea(object):
	def __init__(self, name, region):
		self.name = name
		self.region = region
		self.temperature = 0

	def get_name(self):
		return self.name

	def get_region(self):
		return self.region

	def tea_temperature(self, tea_type):
		if self.region == 'Japan' and self.name == 'gyokuro' and tea_type == 'green':
			self.temperature = 122

		elif self.region == 'Japan' and self.name == 'sencha' and tea_type == 'green':
			self.temperature = 160

		elif tea_type == 'green' and self.region != 'Japan':
			self.temperature = 175

		elif tea_type == 'oolong' and self.region != 'Japan':
			self.temperature = 195

		elif tea_type == 'black' and tea_type == 'puerh' and self.region != 'Japan':
			self.temperature = 212

		return self.temperature



	def __str__(self):
		return str(self.name) + ' ' + str(self.region)

gyokuro = Tea('gyokuro', 'Japan')
# print(gyokuro.get_region())
print(gyokuro.tea_temperature('green'))