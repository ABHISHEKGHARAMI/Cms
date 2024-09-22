import requests

# base url

base_url = 'http://127.0.0.1:8000/api/'

r = requests.get(f'{base_url}course/')
print(r.status_code)
print(r)

courses = r.json()

available_courses = ','.join(course['title'] for course in courses)

print(f'Available courses : {available_courses}')



