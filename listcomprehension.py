a=[1,3,4,5,67,7,4,3]

 #   list comprehension syntax::---->  new_list=[|expression|   |for item in list|   |if condition|]  for creating list

#       [x     for printing 1-10  cond even no]
new_list=[x  for x in range(10)  if x%2==0]
print(new_list)

   

b= [3**i for i in range(10)  ]
print(b)