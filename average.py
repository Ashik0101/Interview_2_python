company = {
    'employees': {
        'John': {'age': 35, 'job_title': 'Manager'},
        'Emma': {'age': 28, 'job_title': 'Software Engineer'},
        'Kelly': {'age': 45, 'job_title': 'Senior Developer'},
        'Sam': {'age': 30, 'job_title': 'Software Engineer'},
        'Mark': {'age': 37, 'job_title': 'Senior Manager'},
        'Sara': {'age': 35, 'job_title': 'Software Engineer'},
    }
}

company2 = {
    'employees': {
        'John': {'age': 35, 'job_title': 'Manager'},
        'Emma': {'age': 28, 'job_title': 'oftware Engineer'},
        'Kelly': {'age': 45, 'job_title': 'enior Developer'},
        'Sam': {'age': 30, 'job_title': 'oftware Engineer'},
        'Mark': {'age': 37, 'job_title': 'enior Manager'},
        'Sara': {'age': 35, 'job_title': 'oftware Engineer'},
    }
}


def calculate_avg(data):
   age = 0
   count = 0
   for employee in company['employees'].values():
      if employee['job_title'].startswith("S"):
         age += employee['age']
         count += 1

   if age == 0:
      return 0
   else:
      return age / count

print(calculate_avg(company2))
print(calculate_avg(company))
