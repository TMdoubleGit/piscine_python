from ft_package import count_in_list

import sys
sys.path.append("/mnt/nfs/homes/tmichel-/42Cursus/algo_ai_data/piscine_python/00/starting/ex09/")


print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0