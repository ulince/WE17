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

neg_weight = 0.0007539649884458758
pos_weight = 0.9992460350115542

def get_all_usertags(filepath):
    all_usertags = set()
    with open(filepath, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader)
        for row in reader:
            usertag = row[25].split(',')
            for tag in usertag:
                all_usertags.add(tag)

    print(all_usertags)

def process_usertags(tags):
    tag_set = set(tags.split(','))
    result = ['0'] * len(USERTAGS)
    for i in range(0,len(USERTAGS)):
        if USERTAGS[i] in tag_set:
            result[i] = '1'
    return "".join(result)

def get_targets(filepath):
    targets = []

    with open(filepath, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader)

        for row in reader:
            targets.append((row[0],int(row[22])))

    pickle.dump(targets, open("validation_targets.p", "wb"))

def load_data_for_LR(filepath,require_labels=False):
    all_data = []
    labels = []

    with open(filepath, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader)

        for row in reader:
            data = {}
            data['weekday'] = row[1]
            data['hour'] = row[2]
            data['region'] = row[8]
            data['city'] = row[9]
            data['adexchange'] = row[10]
            data['advertiser'] = row[24]
            os, browser = row[6].split('_')
            data['os'] = os
            data['browser'] = browser
            data['usertag'] = process_usertags(row[25])

            all_data.append(data)

            if require_labels == True:
                labels.append(int(row[0]))

    return all_data,labels

def load_data_for_LR_test(filepath,require_labels=True):
    all_data = []
    labels = []

    with open(filepath, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(reader)

        for row in reader:
            data = {}
            data['weekday'] = row[0]
            data['hour'] = row[1]
            data['region'] = row[7]
            data['city'] = row[8]
            data['adexchange'] = row[9]
            data['advertiser'] = row[21]
            os, browser = row[5].split('_')
            data['os'] = os
            data['browser'] = browser
            data['usertag'] = process_usertags(row[22])

            all_data.append(data)

            if require_labels == True:
                labels.append(0)

    return all_data,labels

def main(filepath,data_filename,click_labels_filename='', payprice_labels_filename=''):
    if filepath == r"..\data\test.csv":
        data,labels = load_data_for_LR_test(filepath)
    else:
        data, click_labels = load_data_for_LR(filepath)
    pickle.dump(data, open(data_filename, "wb"))
    pickle.dump(click_labels,open(click_labels_filename,"wb"))

#ctr_data("ctr_training_data.p","ctr_training_labels.p","ctr_validation_data.p")
main(test_path,r'..\data\ctr_test_data.p',r'..\data\ctr_test_labels.p')
main(validation_path,r'..\data\ctr_validation_data.p',r'..\data\ctr_validation_labels.p')
main(ttraining_path,r'..\data\ctr_training_data.p',r'..\data\ctr_training_labels.p')