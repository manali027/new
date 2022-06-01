a={
    1:{'Course':'Python',
        'fees':15000},
    2:{'Course':'java',
       'fees':10000}
}
#how to access outer key/id in nested dictionary
print("Accessing key/id")
for id in a:
    print(id)
print()

#accessing inner keys
print("Accessing inner keys")
for id in a:
    for inner_key in a[id]:
        print(inner_key)
print()
#accessing values
print("Accessing values")
for id in a:
    for inner_key in a[id]:
        print(inner_key, "=" ,a[id][inner_key])


'''d={1:
       {5:'five',
        6:'six'
        },
   2:'Two'

}

def display_dict(d):
    #for k in d.keys():
        #print(k)
    #    print(d.get(k))
    for i in d.values():
        print (i)
display_dict(d)'''








