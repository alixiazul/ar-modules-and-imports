# Import the function from the utils.py file
from utils import sum_nums
# Import the numbers from the file in the nested data directory
import data.nested_data.example_numbers as n
# You should see the number 35

result = sum_nums(n.num_1, n.num_2)
print(result)
