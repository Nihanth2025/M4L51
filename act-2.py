a={10,30,45,65}
b={"T","e","n","t"}
r=list(zip(a,b))
print(r)

a=[10,30,45,65]
b=["T","e","n","t"]
for k,z in zip(a,b[::1]):
    print(k,z)