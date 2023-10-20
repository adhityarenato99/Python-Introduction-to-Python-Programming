filehandle = open(r'student-file.txt', 'r')
     
lines = filehandle.readline()

word = 'student-id = 0'

if word in lines:
    print('exit files')
    filehandle.close()
    exit()
else:
    print('continue another process')

    all_file = open(r'student-file.txt', 'r')

    with open('student-data.txt', 'w') as out_file:

        for line in all_file:

            out_file.writelines(line)

        print("Yes write down is successful")