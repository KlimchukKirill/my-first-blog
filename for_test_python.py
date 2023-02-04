def hi(name):
    if name == 'Kirill':
        print('Меня зовут Кирилл')
    else:
        print('Его зовут по другому')

def privet(name):
    print('hi' + name)

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    privet(name)
    print('Next girls')

