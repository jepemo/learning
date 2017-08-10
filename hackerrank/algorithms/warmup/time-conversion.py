elems = input().split(':')

out= ''
if elems[2].endswith('PM'):
    if (elems[0] == '12'):
        elems[0] = '12'
    else:
        elems[0] = str(int(elems[0])+12)

    if (elems[0] == '24'):
        elems[0] = '00'
        
else:
    if (elems[0] == '12'):
        elems[0] = '00'

out = ':'.join(elems)
out = out[0:8]
    
print(out)
