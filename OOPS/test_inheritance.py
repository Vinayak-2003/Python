# class A:
#     print("Class A")

# class B(A):
#     print("Class B")

# class C(B, A):
#     print("Class C")

# class D(C,B):
#     print("Class D")
    
# class E(D, B):
#     print("Class E")



class A:
    print("Class A")

class B:
    name = "vinayak"
    print("Class B")

class C(A):
    print("Class C")

class D(C, B):
    print("Class D")