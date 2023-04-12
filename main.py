from database.common.models import db, History
from database.core import crud
from site_API.core import site_api, url, headers, params

db_write = crud.create()
db_read = crud.retrieve()

fact_by_number = site_api.get_math_fact()
fact_by_date = site_api.get_date_fact()

response = fact_by_number('GET', url, headers, params, '6', 5)
response = response.json()
# print(response)
data_number = [{'numbers': response.get('number'), 'message': response.get('text')}]
db_write(db, History, data_number)

response = fact_by_date('GET', url, headers, params, '6', '21', 5)
response = response.json()
# print(response)
math_number = [{'numbers': response.get('year'), 'message': response.get('text')}]
db_write(db, History, math_number)

retrieved = db_read(db, History, History.numbers, History.message)

for element in retrieved:
    print(element.numbers, element.message)
