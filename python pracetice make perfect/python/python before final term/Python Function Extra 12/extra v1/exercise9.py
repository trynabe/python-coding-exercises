data = [
    {"name":"Alice","score":80},
    {"name":"Bob","score":55},
    {"name":"John","score":72}
]

compute_data = filter(lambda x: x["score"] >= 70,data)
print(list(compute_data))