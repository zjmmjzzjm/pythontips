name = 'zipit'  
suffix = [1,2,3,4,5,6]  
result = zip(name, suffix)  
print(list(result))

import gc  
collected_objects = gc.collect()
print(collected_objects)
