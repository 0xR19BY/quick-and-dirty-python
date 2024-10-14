import re
import glob, os
from datetime import datetime
import sys

# Regular expression to match valid IPv4 addresses
ipv4_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

def extract_ips_from_file(file_path):
    '''function to xyz'''
    with open(file_path, 'r') as file:
        text = file.read()
        ip_addresses = re.findall(ipv4_pattern, text)
    return ip_addresses

def append_ips_to_file(ip_addresses, output_file):
    '''will append outputs to a given file'''
    with open(output_file, 'a') as file:
        for ip in ip_addresses:
            file.write(ip + '\n')

def go_through_all_txt(extension):
    '''will return all the names of files ending in .txt'''
    file_list = []
    os.chdir("./")
    for file in glob.glob(f'*.{extension}'): #Feel free to edit this to your liking
        file_list.append(file)

    print(file_list)
    return file_list


def main(file_list):
    '''main function'''
    if len(sys.argv) < 3:
        print("Usage: -e {extension type}")
        return
    
    if sys.argv[1] == '-e':
        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"IP_List{current_datetime}.csv"
        for file in file_list:
            output_file = file_name
            ip_addresses = extract_ips_from_file(file)
            append_ips_to_file(ip_addresses, output_file)
        print("Scrape completed")
    else:
        print("Usage: -e {extension type}")

if len(sys.argv) < 3:
    print("Usage: -e {extension type}")
else:
    files = go_through_all_txt(sys.argv[2])
    main(files)