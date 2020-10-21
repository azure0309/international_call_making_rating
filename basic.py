class Country(object):
	def __init__(self, name, country_code, rating):
		self.name = name
		self.country_code = country_code
		self.rating = rating

	def describe_country(self):
		country_description = {
			'Name': self.name,
			'Country_code': self.country_code,
			'Rating': self.rating
		}
		return country_description


class Call(object):
	def __init__(self, a_number, b_number, status, duration):
		self.a_number = a_number
		self.b_number = b_number
		self.status = status
		self.duration = duration

	def describe_call(self):
		call_information = {
			'a_number': self.a_number,
			'b_number': self.b_number,
			'status': self.status,
			'duration': self.duration
		}
		return call_information


my_country = Country('Mongolia', '976', '0.2')
description = my_country.describe_country()

my_call = Call('97689118432', '0088656238974', 'success', 120)
information = my_call.describe_call()
# print(information)
