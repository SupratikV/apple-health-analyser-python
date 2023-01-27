import xml.etree.ElementTree as ET 
import pandas as pd
import matplotlib.pyplot as plt
import datetime
tree = ET.parse('/Users/supratikvishnu/Library/Mobile Documents/com~apple~CloudDocs/coding/export.xml')
root=tree.getroot()
workout_list = [x.attrib for x in root.iter('Workout')]

workout_data = pd.DataFrame(workout_list)
workout_data['workoutActivityType'] = workout_data['workoutActivityType'].str.replace('HKWorkoutActivityType', '')
workout_data = workout_data.rename({"workoutActivityType": "Type"}, axis=1)



def plot_workouts(workouts):
    labels = []
    slices = []
    for wo_type in workouts.Type.unique():
        labels.append(wo_type)
        wo_of_type = workouts[workouts["Type"] == wo_type]
        num_workouts_of_type = wo_of_type.shape[0]
        slices.append(num_workouts_of_type)

    def make_autopct(values):
        def my_autopct(pct):
            total = sum(values)
            val = int(round(pct*total/100.0))
            return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
        return my_autopct

    plt.figure(figsize=(10, 10))
    plt.pie(slices, labels=labels, shadow=True,
            startangle=90, autopct=make_autopct(slices),
            wedgeprops={'edgecolor': 'black'})

    plt.title("Workouts recorded")
    plt.tight_layout()
    plt.show()

