import requests

# base url
username = 'Test002@'
password = 'Gharami1998@'

base_url = 'http://127.0.0.1:8000/api/'

r = requests.get(f'{base_url}course/')
print(r.status_code)
print(r)

courses = r.json()

available_courses = ','.join(course['title'] for course in courses)

print(f'Available courses : {available_courses}')

for course in courses:
    course_id = course['id']
    course_title = course['title']
    r = requests.post(f'{base_url}/course/{course_id}/enroll/',
                      auth=(username,password))
    
    if r.status_code == 200:
        print(f'Successfully enrolled : {course_title}')



