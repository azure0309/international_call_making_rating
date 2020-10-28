from basic import Country, Call
import connect_ufms
import pandas as pd
import csv


class Connection_to_UFMS():
	def __init__(self, query):
		self.query = query

	def query_executor(self):
		cursor = connect_ufms.connection.cursor()
		execute = cursor.execute(self.query)
		return execute


class Get_Country_Info(Country):
	def __init__(self, country_code):
		Country.__init__(self, country_code, country_code, country_code)

	def __str__(self):
		query = f"select COUNTRY from T_ALL_COUNTRY_CODE where COUNTRYCODE = '{self.country_code}'"
		select_country_info = Connection_to_UFMS(query)
		select_name = select_country_info.query_executor()

		country_name = ''
		for name in select_name:
			country_name = name[0]
		return country_name  # it returns string

	def select_data_of_country(self):
		query = f"select * from T_ALL_COUNTRY_CODE where COUNTRYCODE = '{self.country_code}'"
		select_country_info = Connection_to_UFMS(query)
		select_data = select_country_info.query_executor()

		number_info = \
			{
				'Continent': '',
				'Country': '',
				'Country_code': '',
				'Alpha2': '',
				'Alpha3': ''
			}

		for value in select_data:
			number_info['Continent'] = value[0]
			number_info['Country'] = value[1]
			number_info['Country_code'] = value[2]
			number_info['Alpha2'] = value[3]
			number_info['Alpha3'] = value[4]

		return number_info  # it returns dictionary

	@classmethod
	def select_all_countries(cls):
		continent = []
		country = []
		country_code = []
		alpha2 = []
		alpha3 = []

		query = "select * from T_ALL_COUNTRY_CODE"
		select_country_info = Connection_to_UFMS(query)
		select_data = select_country_info.query_executor()

		number_info = \
			{
				'Continent': '',
				'Country': '',
				'Country_code': '',
				'Alpha2': '',
				'Alpha3': ''
			}

		for value in select_data:
			continent.append(value[0])
			country.append(value[1])
			country_code.append(value[2])
			alpha2.append(value[3])
			alpha3.append(value[4])

		number_info['Continent'] = continent
		number_info['Country'] = country
		number_info['Country_code'] = country_code
		number_info['Alpha2'] = alpha2
		number_info['Alpha3'] = alpha3

		framed_countries_info = pd.DataFrame(number_info)
		return framed_countries_info  # it returns Dataframe


def get_number_from_traffic():
	query = f"select * from T_CALL_INTL_WHOLESALE where INVITETIME > sysdate - 1 / 24"
	select_country_info = Connection_to_UFMS(query)
	select_number = select_country_info.query_executor()

	return select_number


# class B_Number_Split():
# 	def __init__(self, b_number):
# 		self.b_number = b_number


# def describe_country(self):
# 	country_description = {
# 		'name': self.name,
# 		'country_code': self.country_code,
# 		'b_number': self.b_number
# 	}
# 	return country_description

def B_Number_Split(number):
	if str(number[:3]) == '008':
		print('IDD')
	elif str(number[:4]) == '1668':
		print('OD')
	else:
		print('Roaming')

numbers = ['008654987', '1668987654321', '123456789']
for i in numbers:
	B_Number_Split(i)
