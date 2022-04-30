import random

def createDict(filename):
    dict = {}
    f = open(filename, encoding="utf8")
    data = f.read()
    data = data.split()
    dict['FIRSTWORD'] = []
    dict['FIRSTWORD'].append(data[0])
    for i in range(0,len(data)):
        if data[i][len(data[i])-1] != '.':
            if data[i] in dict.keys():
                dict[data[i]].append(data[i+1])
            else:
                dict[data[i]] = []
                dict[data[i]].append(data[i+1])
        else:
            if (i+1) < len(data):
               dict['FIRSTWORD'].append(data[i+1])
    return dict

def generateText(d, n):
    new_sentence = ''
    start_list = d['FIRSTWORD']
    x = random.randint(0, len(start_list)-1)
    word2 = start_list[x]
    new_sentence = new_sentence+' '+word2
    counter = 0
    punct = ['.','?','!']
    while counter < n:
        if (word2[len(word2)-1] in punct):
            counter = counter + 1
            start_list = d['FIRSTWORD']
            x = random.randint(0, len(start_list)-1)
            word2 = start_list[x]
            if counter < n:
                new_sentence = new_sentence+' '+word2
        else:
            wordlist = d[word2]
            word2 = random.choice(wordlist)
            new_sentence = new_sentence+' '+word2
    return new_sentence

def main():
    a1 = input("Welcome to Markov text generator!\nEnter a txt file: ")
    a2 = input("Enter the number of sentences to generate: ")
    d = createDict(a1)
    n = generateText(d, int(a2))
    print(n)

if __name__ == "__main__":
    main()


    





