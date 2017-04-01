import csv
import pickle
from collections import defaultdict

training_path = r"..\data\train.csv"
validation_path = r"..\data\validation.csv"
test_path = r"..\data\test.csv"
USERTAGS = ['13776', '10133', '10146', '10052', '13800', '13678', '10077', '10057', '10048',
            '16753', '16706', '10120', '11278', '10140', '10127', '10684', '10138', '10148', '11092',
            '15398', '10067', '11632', '10117', '10114', '10145', '11576', '14273', '10059', '16617',
            '10083', '13403', '10126', '11944', '13874', '11724', '10076', '10131', '10093', '11423',
            '10110', '10123', '16751', '13496', '10149', '10111', '10031', '10142', '10118', '10074',
            '10024', '16593', '10006', '10116', '11680', '10130', '10147', '10102', '10063',
            '10075', '11512', '10129', '10079', '10125', '10115', '13042', '11379', '16661', '13866']

def load_data(filepath):
    data = defaultdict(list)
    payprice_labels = []

    with open(filepath, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader)

        for row in reader:
            data['weekday'].append(row[1])
            data['hour'].append(row[2])
            data['region'].append(row[8])
            data['city'].append(row[9])
            data['adexchange'].append(row[10])
            data['advertiser'].append(row[24])
            os, browser = row[6].split('_')
            data['os'].append(os)
            data['browser'].append(browser)
            data['usertag'].append(process_usertags(row[25]))



            payprice_labels.append(int(row[22]))

    return data,payprice_labels

def load_data_test(filepath):
    data = defaultdict(list)
    payprice_labels = []

    with open(filepath, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader)

        for row in reader:
            data['weekday'].append(row[0])
            data['hour'].append(row[1])
            data['region'].append(row[7])
            data['city'].append(row[8])
            data['adexchange'].append(row[9])
            data['advertiser'].append(row[21])
            os, browser = row[5].split('_')
            data['os'].append(os)
            data['browser'].append(browser)
            data['usertag'].append(process_usertags(row[22]))

            payprice_labels.append(0)

    return data,payprice_labels

def process_usertags(tags):
    tag_set = set(tags.split(','))
    result = ['0'] * len(USERTAGS)
    for i in range(0,len(USERTAGS)):
        if USERTAGS[i] in tag_set:
            result[i] = '1'
    return "".join(result)

def main(filepath,data_filename, payprice_labels_filename):
    if filepath == r"..\data\test.csv":
        data,labels = load_data_test(filepath)
    else:
        data,labels = load_data(filepath)
    pickle.dump(data, open(data_filename, "wb"))
    pickle.dump(labels, open(payprice_labels_filename, "wb"))

def get_targets(filepath):
    targets = []

    with open(filepath, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader)

        for row in reader:
            targets.append((row[0],int(row[22])))

    pickle.dump(targets, open("validation_targets.p", "wb"))

main(test_path,r"..\data\test_data.p",r"..\data\test_labels_continuous.p")
main(training_path,r"..\data\training_data.p",r"..\data\training_labels_continuous.p")
main(validation_path,r"..\data\validation_data.p",r"..\data\validation_labels_continuous.p")

