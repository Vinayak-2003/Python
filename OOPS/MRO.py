class A:
    print("class A")
    
class B(A):
    print("class B")
    
class C(A):
    print("class C")
    
class D(C, B):
    print("class D")
    
# class E(C, A, B):
#     print("class E")

# print(E.mro())
print(D.__mro__)

# class A:  
#     pass  
# class B:  
#     pass  
# class C(A, B):  
#     pass  
# class D(B, A):  
#     pass  
# class E(C,D):  
#     pass 