ages={
    "dave":24,
    "mary":42,
    "john":58
}
print(ages["dave"])
print(ages["mary"])
#function
nums={
    1:"one",
    2:"two",
    3:"three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)
print(nums[1])
#get()
pairs={
    1:"apple",
    "orange":[2,3,4],
    True:False,
    12:"true",
}
print(pairs.get("orange"))
print(pairs.get(7,42))
print(pairs.get(12345,"not found"))
