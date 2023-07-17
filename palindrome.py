def check_palindrom(num):
   num_str = str(num)
   reversed_num_str = num_str[::-1]
   if num_str == reversed_num_str:
      return True
   else:
      return False


print(check_palindrom(242))
print(check_palindrom(241))
print(check_palindrom(2423))