import csv
import pickle
from collections import defaultdict

training_path = r"C:\Users\Uly\Desktop\Desktop\UCL\WebEcon\dataset\train.csv"
validation_path = r"C:\Users\Uly\Desktop\Desktop\UCL\WebEcon\dataset\validation.csv"
test_path = r"C:\Users\Uly\Desktop\Desktop\UCL\WebEcon\dataset\test.csv"
USERTAGS = ['13776', '10133', '10146', '10052', '13800', '13678', '10077', '10057', '10048',
            '16753', '16706', '10120', '11278', '10140', '10127', '10684', '10138', '10148', '11092',
            '15398', '10067', '11632', '10117', '10114', '10145', '11576', '14273', '10059', '16617',
            '10083', '13403', '10126', '11944', '13874', '11724', '10076', '10131', '10093', '11423',
            '10110', '10123', '16751', '13496', '10149', '10111', '10031', '10142', '10118', '10074',
            '10024', '16593', '10006', '10116', '11680', '10130', '10147', '10102', '10063',
            '10075', '11512', '10129', '10079', '10125', '10115', '13042', '11379', '16661', '13866']
classes = {0:0,10:1,20:2,30:3,40:4,50:5,60:6,70:7,80:8,90:9,100:10,110:11,120:12,130:13,140:14,150:15,160:16,170:17,
           180:18,190:19,200:20,210:21,220:22,230:23,240:24,250:25,260:26,270:27,280:28,290:29,300:30}

STD_SLOTPRICE = 37
neg_weight = 0.0007539649884458758
pos_weight = 0.9992460350115542

def round_up(number):
    return ((number + 9) // 10 * 10)

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

#get_all_usertags(training_path)
def main(filepath,data_filename, payprice_labels_filename):
    data,labels = load_data_test(filepath)
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

main(test_path,r".\test_pickles\test_data.p",r".\test_pickles\test_labels_continuous.p")
#main(test_path,r".\bidprice_pickles\validation_data.p",r".\bidprice_pickles\validation_labels_continuous.p")

