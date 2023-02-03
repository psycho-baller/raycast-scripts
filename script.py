import base64


def print_repeated_names(filename):
    with open(filename) as file:
        names = file.readlines()

    names = [name.strip() for name in names]  # remove newline characters
    name_counts = {}
    for name in names:
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1

    repeated_names = [name for name,
                      count in name_counts.items() if count >= 2]
    if repeated_names:
        print("The following names appear 2 or more times:")
        for name in repeated_names:
            print(name)
    else:
        print("No names appear 2 or more times.")


# print_repeated_names("temp.txt")
print(open("IBM/assets/LICENSE", "rb").read())
