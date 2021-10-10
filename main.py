import math
import random
def KNN(inputDataset,items,k):


    for i in range(len(inputDataset)):
        neighbors = []
        for item in items:
            e = 0
            for key in inputDataset[i].keys():

                e += math.pow(inputDataset[i][key] - item[key], 2);
            distance = math.sqrt(e)
            #print(distance)
            if len(neighbors) < k:
                neighbors.append([distance, item['Class']])
                neighbors = sorted(neighbors)
            else:
                if neighbors[-1][0] > distance:
                    neighbors[-1] = [distance, item['Class']]
                    neighbors = sorted(neighbors)
        count = {}

        for i in range(k):
            if (neighbors[i][1] not in count):
                count[neighbors[i][1]] = 1;
            else:
                count[neighbors[i][1]] += 1;

        maximum = -1
        classification = ""

        for key in count.keys():
            if (count[key] > maximum):
                maximum = count[key]
                classification = key
        result = classification

        print(result)


def main():
    f = open('data.txt', 'r')
    dataset = f.read().splitlines()

    f.close()
    features = dataset[0].split(',')[:-1]
    items = []
    for i in range(1, len(dataset)):
        data = dataset[i].split(',')
        itemFeatures = {"Class": data[-1]}
        for j in range(len(features)):
            f = features[j]
            v = float(data[j])
            itemFeatures[f] = v
        items.append(itemFeatures)

    print("input K value:")
    k = input()

    inputDataset = [{'Height': 162, 'Weight': 53, 'Age': 28}, {'Height': 168, 'Weight': 75, 'Age': 32},
                    {'Height': 175, 'Weight': 70, 'Age': 30}, {'Height': 180, 'Weight': 85, 'Age': 29}]
    print("Predicted class is ")
    KNN(inputDataset,items,int(k))

if __name__ == '__main__':
    main()
