import pandas as pd

hours = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
         '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15',
        '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

df = pd.read_csv("C:/Users/Tanc/Desktop/20200822.csv", sep=',', names=[
    'VehicleID', 'gpsvalid', 'lat', 'lon', 'timestamp', 'speed', 'heading', 'for_hire_light', 'engine_acc'])
split_date = df['timestamp'].str.split(' ', expand=True)
df['date'] = split_date[0]
df['timeR'] = split_date[1]

for hour in hours:
    check_timeR = df[df['timeR'].str.contains('^'+hour)]
    check_date = check_timeR.loc[(df['date'] == '2020-08-22')]
    check_date.to_csv("C:/Users/Tanc/Desktop/20200822/20200822-"+hour+".csv", index=False)

print(check_date)
