from basic import Country
import connect_ufms


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

		number_info = {
			'Continent': '',
			'Country': '',
			'Country_code': '',
			'Alpha2': '',
			'Alpha3': ''}

		for value in select_data:
			number_info['Continent'] = value[0]
			number_info['Country'] = value[1]
			number_info['Country_code'] = value[2]
			number_info['Alpha2'] = value[3]
			number_info['Alpha3'] = value[4]

		return number_info

	def select_all_countries(self):
		query = "select * from T_ALL_COUNTRY_CODE"
		select_country_info = Connection_to_UFMS(query)
		select_data = select_country_info.query_executor()




hujaa = Get_Country_Info(82)
hujaa_data = hujaa.select_data_of_country()
print(hujaa_data)
