from basic import Country
import connect_ufms

class Connection_to_UFMS():
	def __init__(self, query):
		self.query= query

	def query_executor(self):
		cursor = connect_ufms.connection.cursor()
		execute = cursor.execute(self.query)
		return execute

class All_Country_List(Country):
	query = 'select * from T_ALL_COUNTRY_CODE'
	select_all_country_code = Connection_to_UFMS(query)
	select_data = select_all_country_code.query_executor()

	def __init__(self, name, rating):
		super().__init__(self, name, rating)

		print(self.name)

	# def compress_selected_data(self):

my_country = All_Country_List('Mongolia', 3.5)



# query = 'select * from od_alert'
# my_query = Connection_to_UFMS(query)
# select = my_query.query_executor()
#
# for i in select:
# 	print(i)

