phone = input("Phone :")
digigt_mapping = {
    "1":"one",
    "2":"two",
    "3":"three"
}
output =""
for cha in phone:
    output +=digigt_mapping.get(cha,"!")+" "
print(output)
