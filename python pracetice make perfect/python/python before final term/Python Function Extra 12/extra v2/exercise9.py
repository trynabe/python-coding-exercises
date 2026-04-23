company = {
    "IT": {"names": ["Ann", "Bob"]},
    "HR": {"names": ["Cara", "Don"]},
    "Sales": {"names": ["Eve"]}
}
def combine_names(company):
    dept_lists = map(lambda d: d["names"],company.values())
    all_names = [name for sublist in dept_lists for name in sublist]
    return all_names
print(combine_names(company))