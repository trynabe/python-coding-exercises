def fav_colors(**kwargs):
    print(kwargs)
    for person , color in kwargs.items():
        print(f'{person} -> {color}')

fav_colors(dee = 'pink',tip = 'green', mock = 'purple',pa='yellow')