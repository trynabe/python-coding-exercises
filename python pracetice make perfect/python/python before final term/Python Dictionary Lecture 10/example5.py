playlist = {'title': 'chill',
            'author':'somename',
            'songs':[
            {'title':'song1',
            'artist': ['blue'],
            'duration':2.5},
            {'title':'song2',
            'artist': ['hj', 'dj'],
            'duration':5},
            {'title':'song3',
            'artist': ['tt', 'dd'],
            'duration':10}
            ]
            }
print(playlist['title'])
print(playlist['author'])
print(playlist['songs'])
print(playlist['songs'][0])
print(playlist['songs'][0]['artist'])
print(playlist['songs'][0]['duration'])
