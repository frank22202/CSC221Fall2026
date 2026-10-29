with open('scores.txt', 'r') as file:
    total = 0
    count = 0
    for line in file:
        cleaned_line = line.strip()
        if cleaned_line:  # Skips empty lines
            total += int(cleaned_line)
            count += 1

if count > 0:
    print(f'{total/count:.2f}')
else:
    print("No scores found in the file.")
