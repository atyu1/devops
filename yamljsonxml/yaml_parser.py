import yaml
from pprint import pprint

with open('example.yaml', 'r') as YAMLFILE:
    data = yaml.safe_load(YAMLFILE)

podname = data['PODNAME']
print (podname)

for role in data['ROLES']:
    print('\n#R: %s', role)
    for server in data['ROLES'][role]:
        print ('#S: %s', server)


print ('--- Full data ---')
pprint(data)

print('... Fixing username: test -> admin')
data['REGISTRY_USERNAME'] = 'admin'

print('... Saving to file: example2.yaml')
with open('example2.yaml', 'w') as FIXYAMLFILE:
    yaml.dump(data, FIXYAMLFILE, default_flow_style=False)