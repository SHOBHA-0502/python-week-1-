mydict = {
    "shobha": "beautiful",
    "pani": "water",
    "kutta":"dog",
    "khana":"food"
}
print("options are",mydict.keys())
a = input("enter the hindi word\n")
print("the meaning in english is:" , mydict.get(a))