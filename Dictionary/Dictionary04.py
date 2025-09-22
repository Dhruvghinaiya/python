data = {
    'name':'dhruv',
    'surname':'ghinaiya',
    'lunguage' :{
        'java':0.7,
        'laravel':0.9,
        'python':0.4
    }
}

print(data)

print(type(data))

print(len(data))
print(list(data))
print('Key:',data.keys())
print('Values',data.values())
print(data.copy())
print(data.items())

# print(data['name1'])    # return error if key is not exits 
print(data.get('name2')) # return none if key is not exits

data.update({'gender':'male','name':'tushar'})
print(data)