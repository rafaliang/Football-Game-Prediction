import csv
import time
i = 0
f_read = open('alldata.csv','rb')
f_write = open('washed_data.csv','wb')
f_csv_read = csv.reader(f_read)
f_csv_write = csv.writer(f_write)
headers = next(f_csv_read)
new_headers = headers[:7] + ['match_time_difference'] + headers[9:]
#print headers
#print new_headers
f_csv_write.writerow(new_headers)

average_numbers = [72.42294486,69.49416153,71.09863147,70.98288449,69.38916596,71.02267381,71.00557531,
                   71.11455209,71.65053024,72.04820112,72.25687848,72.42465144,69.4192138,71.06716357,
                   70.93628843,69.36589028,70.88615909,70.91856612,71.01436805,71.54030262,71.95240036,
                   72.17379734,52.42334154,49.10177293,47.9235173,52.41214282,54.04499573,54.27153116,
                   46.48435695,49.49585698,52.33736755,52.39926703,49.07228094,47.93076962,52.41146644,
                   54.02736081,54.27094734,46.46136854,49.45966163,52.34298911]
label_possibility = [0.481366, 0.279503, 0.239130, 0.481366, 0.279503, 0.239130]
for row in f_csv_read:
    #if i > 10:
    #    break
    if i % 1000 == 0:
        print i
    for t in range(20,60):
        if row[t] == '0.0':
            row[t] = average_numbers[t-20]
    for t in range(60,66):
        if row[t] == '0' or row[t] == '':
            row[t] = label_possibility[t-60]
    #print row
    #print row[:7] + ['676'] + row[9:]
    time1 = row[7]
    time2 = row[8]
    if time1 == '0.0' or time2 == '0.0':
        match_time_difference = 0
    else:
        real_time1 = time.mktime(time.strptime(time1,'%Y-%m-%d %H:%M:%S'))
        real_time2 = time.mktime(time.strptime(time2,'%Y-%m-%d %H:%M:%S'))
        match_time_difference = real_time1 - real_time2
    f_csv_write.writerow(row[:7] + [match_time_difference] + row[9:]) 
    #print row[:7] + [match_time_difference] + row[9:]
            
    i += 1

f_read.close()
f_write.close()
