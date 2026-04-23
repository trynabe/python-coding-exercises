enrolled = {
    "Alice","Bob","John","Doe","Nor","Sara","Max"
}
score_dict = {
    "Alice":97,"Bob":76,"John":79,"Doe":27,"Nina":90
}

no_score = {name for name in enrolled if name not in score_dict}
print(f"Enrolled but not score: {no_score}")

no_enrolled = {name for name in score_dict if name not in enrolled}
print(f"Scored but not enrolled: {no_enrolled}")