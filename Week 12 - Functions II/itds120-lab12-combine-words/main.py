'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab12-combine-words
*/
'''

def combine_words(word,**kwargs):
    if 'position' in kwargs:
        position = kwargs['position']
        extra = kwargs['extra']

        if position == 'prefix':
            return extra + word
        elif position == 'suffix':
            return word + extra
    return word

input_text = input()
position_text = input()
extra_text = input()

print(combine_words(input_text, position = position_text, extra=extra_text)) #homework
