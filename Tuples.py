words=("athiff","munsif","zulaiha")
print(words[0])

dict={
    ("david",42):"red",
    ("bob",24):"green"
}
print(dict[("bob",24)])

#Tuple unpacking
numbers=(1,2,3)
a,b,c=numbers
print(a)
print(b)
print(c)
t,u,*v,w=[1,2,3,4,5,6,7,8,9]
print(t)
print(u)
print(v)
print(w)