#
#   PROJECT : Email Spam Filtering
# 
#   FILENAME : email_ml.py
# 
#   DESCRIPTION :
#       ...
# 
#   FUNCTIONS :
#       main()
# 
#   NOTES :
#       - ...
# 
#   AUTHOR(S) : Noah Da Silva               START DATE : 2022.12.02 (YYYY.MM.DD)
#
#   CHANGES :
#       - ...
# 
#   VERSION     DATE        WHO             DETAILS
#   0.0.1a      2022.12.02  Noah            Creation of project.
#

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import json
import csv

# Machine Learning Libraries
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.callbacks import LambdaCallback
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, Dense, Flatten, Activation
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder, OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report, confusion_matrix


class EmailMachineLearning:
    #
    # NOTE:
    #
    def __init__(self):
        pass

    #
    # NOTE:
    #
    def json_to_csv(self, filename=None, training=False):
        with open(filename) as json_file:
            message_data = json.load(json_file)

        count = 0
        if training is True:
            filename = 'messages_train'
            csv_file = open(f'{filename}_old.csv', 'w')
            csv_writer = csv.writer(csv_file)
            for mail in message_data:
                if count == 0:
                    header = mail.keys()
                    csv_writer.writerow(list(header) + ['spam'])
                    count += 1

                csv_writer.writerow(list(mail.values()) + [random.randint(0,1)])
        else:
            filename = 'messages_test'
            csv_file = open(f'{filename}_old.csv', 'w')
            csv_writer = csv.writer(csv_file)
            for mail in message_data:
                if count == 0:
                    header = mail.keys()
                    csv_writer.writerow(header)
                    count += 1

                csv_writer.writerow(mail.values())

        csv_file.close()

        with open(f'{filename}_old.csv', newline='') as in_file:
            with open(f'{filename}.csv', 'w', newline='') as out_file:
                writer = csv.writer(out_file)
                for row in csv.reader(in_file):
                    if row:
                        writer.writerow(row)