s_l = []
bl = []
with open('tempstats.txt', 'r') as text:
    for line in text:
        s_l = line.split(',')
    for token in s_l:
        if token == 'next':
            bl.append('\n')
        else:
            bl.append(token)

with open('heyomap4.txt', 'w') as text:
    for token in bl:
        if token == '\n':
           text.write('\n')
        else:
            text.write(token)
            text.write(',')



