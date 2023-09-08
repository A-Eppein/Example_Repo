#New File
CountryName = []
CountryCode = []
def read_csv():
    with open("data.csv", "r") as data_csv:
        lines = data_csv.readlines()
    return lines
def parse_csv(data_csv):
    for line in data_csv:
        new_list = line.strip().split(",")
        if len(new_list)>= 2:
            CountryName.append(new_list[0])
            CountryCode.append(new_list[1])
def print_data():
    for Cname, Ccode in zip(CountryName, CountryCode):
        print("---------")
        print("Country Name: ", Cname)
        print("Country Code: ", Ccode)

data_csv = read_csv()
parse_csv(data_csv)
print_data()
