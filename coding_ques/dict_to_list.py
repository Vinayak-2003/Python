dict1 = {"key1": "value1", "key2": "Value2"}
dict2 = {"key3": "Value3"}

# dict1.update(dict2)
# ans_list = []
# for k,v in dict1.items():
#     temp = f"{k}:{v}"
#     ans_list.append(temp)
    
# dict1.update(dict2)
# ans_list = [f"{k}:{v}" for k,v in dict1.items()]

ans_list = [f"{k}:{v}" for k,v in {**dict1, **dict2}.items()]
print(ans_list)