import json
from json import load

bankOldFile = open('./bank_old.json','r')

bank3File = open('./bank3.json','r')
bank7File = open('./bank7.json','r')

bankOld = json.load(bankOldFile)
bank3 = json.load(bank3File)
bank7 = json.load(bank7File)

for b3 in bank3:
    print('b3:'+ b3['Value'])
    for b7 in bank7:
        if b3['Value'] in b7['Value']:
            index = b7['Value'].index(b3['Value'])
            if index == 0:
                if b3['Key'] == b7['Key']:
                    if b7['Short'][-2:] == '本會':
                        b7['Key'] = b3['Key'] + b7['Short'][-2:]
                    else:
                        b7['Key'] = b3['Key'] + b7['Short']
                else:
                    b7['Key'] = b3['Key'] + b7['Key']
                b7['Value'] = b3['Value'] + b7['Value'][-4:]

bankOld_values = {bOld['Value'] for bOld in bankOld}

for b7 in bank7:
    isExist = b7['Value'] in bankOld_values

    if isExist == False:
        bankOld.append({'Value':b7['Value'],'Key':b7['Key']})

json_string = json.dumps(bankOld, ensure_ascii=False)

with open('bank.json', 'w', encoding='utf-8') as file:
    json.dump(bankOld, file, ensure_ascii=False)