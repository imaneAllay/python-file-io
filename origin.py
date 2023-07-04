print('Opening origin.txt')
with open('origin.txt', 'r') as in_file:
    print('Opening output_file.txt')
    content = in_file.readlines()

    with open('output_file.txt', 'w') as out_file:
        for line_number, line in enumerate(content, start=1):
            for keyword in line.split():
                if keyword in ['heritable', 'inherit', 'inheritance']:
                    out_file.write(f"{line_number}\t{keyword}\n")

print("Done!")
print('origin.txt is closed?', in_file.closed)
print('output_file.txt is closed?', out_file.closed)