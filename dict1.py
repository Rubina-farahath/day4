Dict={101:'python',201:'java',301:'c',401:'c++'}
print(Dict)
print(type(Dict))
print("________________________________________________")
print(Dict[101])
print(Dict[201])
print(Dict[301])
print(Dict[401])
Dict[501]='sql'
print("_________________________________________________")
print(Dict)
Dict[101]='flutter:'
print("_________________________________________________")
print(Dict)
del Dict[301]
print(Dict)
new=Dict.copy()
print(new)