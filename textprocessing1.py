
import csv
import os
import re
import sys

def main():
    import_text = os.getcwd() + '\\' + 'import_text.txt'
    with open(import_text) as text:
        lines = [line for line in text]

    interface_re = re.compile('(.*[0-9]: )')
    inet_re = re.compile('(inet )(([0-9]{1,3}\.){3}[0-9]{1,3})')
    status_re = re.compile('(status: )(\w+)')

    interface_count = 0
    interfaces_found=0
    interfaces = [[]] 
    for line in lines:
        interface = interface_re.match(line)
        inet = inet_re.search(line)
        status = status_re.search(line)

        if interface:
            if interfaces_found > 0:
                if len(interfaces[interface_count]) == 1:
                    interfaces[interface_count].append('')
                    interfaces[interface_count].append('')
                elif len(interfaces[interface_count]) == 2:
                    interfaces[interface_count].append('')
                interface_count += 1
                interfaces.append([])

            interfaces[interface_count].append(interface[0].strip()[:-1])
            interfaces_found += 1

        elif inet:
            interfaces[interface_count].append(inet[2])

        elif status:
            if len(interfaces[interface_count])==2:
                interfaces[interface_count].append(status[2])
            else:
                interfaces[interface_count].append('')
                interfaces[interface_count].append(status[2])


    print(interfaces)

    with open('output.csv', 'w', newline='') as csvfile:
        output_writer = csv.writer(csvfile, delimiter=',')
        output_writer.writerow(['interface','inet','status'])
        for interface in interfaces:
            output_writer.writerow(interface)


if __name__ == "__main__":
    main()





