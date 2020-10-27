from basic import Country
import connect_ufms
import pandas as pd


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

		number_info = {
			'Continent': '',
			'Country': '',
			'Country_code': '',
			'Alpha2': '',
			'Alpha3': ''}

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

		return number_info  # it returns dictionary


hujaa = Get_Country_Info(82)
hujaa_data = hujaa.select_all_countries()
# print(hujaa_data)

df = pd.DataFrame(hujaa_data)
print(df)
