counter = 0

def inception(counter):
    if counter > 3:
        return 'done'
    counter += 1
    print(counter)
    return inception(counter)

print(inception(counter))