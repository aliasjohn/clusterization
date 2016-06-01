# zero: binary search tree realisation for using like set

class BST:
    def __init__(self):
        self.root = None
        self.cardinality = 0
        self.nodes = []

    def add(self, value):
        node = BSTnode()
        node.setData(value)
        if self.root == None: self.root = node
        else:
            r = self.search(value)
            if r[1] == 0:
                r[0].weight += 1
                return
            elif r[1] == -1: r[0].left = node
            else: r[0].right = node
        self.nodes.append(node)
        self.cardinality += 1

    def search(self, value):
        current = self.root
        if current == None: return (None)
        while 1:
            if current.data == value:
                return (current,0)
            elif current.data > value:
                if current.left == None: return (current,-1)
                else: current = current.left
            else:
                if current.right == None: return (current,1)
                else: current = current.right

class BSTnode:
    def __init__(self):
        self.left = self.right = self.data = None
        self.weight = 1
    def setData(self, data): self.data = data

#class bstSet:
#    def __init__(self):

# first: load data for clasterization and forming sets
sample = []
sample_cardinality = 5
print('Gathering data...')
for i in range(0, sample_cardinality):
    sample.append(BST())
    raw = ''
    with open(str(i)+'.dat', 'r') as f:
        raw = f.read()
    word = ''
    for j in range(0, len(raw)):
        if raw[j] >= 'A' and raw[j] <= 'Z' or raw[j] >= 'a' and raw[j] <= 'z' or raw[j] >= 'А' and raw[j] <= 'Я' or raw[j] >= 'а' and raw[j] <= 'я':
            word += raw[j].lower()
        else:
            if not(word == ''):
                sample[-1].add(word)
                word = ''

for i in range(0, sample_cardinality):
    print('Object '+str(i)+'('+str(sample[i].cardinality)+'):')
    for j in range(0, sample[i].cardinality):
        print(sample[i].nodes[j].data)
    print()

# second: cross sets and unite them for getting cardinalities
jks = []
for i in range(1, len(sample)):
    joint_count = 0
    for j in range(0, sample[i].cardinality):
        if sample[0].search(sample[i].nodes[j].data)[1] == 0:
            joint_count += 1
    jks.append(joint_count / (sample[0].cardinality + sample[i].cardinality - joint_count))
    print('Pair '+str(i)+':',jks[-1])

# third: calculating mean similarity and detecting clasters
mean = 0
for i in range(0, len(jks)):
    mean += jks[i]
mean /= len(jks)
print('Mean JK:',mean)

print('Claster for zero object: 0',end=' ')
for i in range(0, len(jks)):
    if jks[i] > mean:
        print(i+1,end=' ')
