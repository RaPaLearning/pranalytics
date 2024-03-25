
nonenglish = ['PHSTPpc', 'preflight']

with open('reviews-t.txt', 'r') as f:
    for line in f.readlines():
        if not any([unwanted in line for unwanted in nonenglish]):
            print(line)
