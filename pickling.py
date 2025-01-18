import pickle
import json

data = {"name": "Vinayak", "university": "Manipal University Jaipur"}
data = "hello"
print("-----data----->", type(data))
pickled_data = pickle.dumps(data)
unpickled_data = pickle.loads(pickled_data)

serialized_data = json.dumps(data)
print("-----serialized_data----->", serialized_data)
print("-----serialized_data----->", type(serialized_data))
print("-----deserialized_data----->", unpickled_data)
print("-----deserialized_data----->", type(unpickled_data))