while True:
# Data input
    row = input("Please input letters one by one without spaces \n").upper().strip()

# Calculation workflow
    row_len = len(row)
    g_counter = row.count("G")
    c_counter = row.count("C")
    percentage = round((((g_counter + c_counter) / row_len) * 100), 2)

# Displaying results
    print(percentage)

# Dialogue for breaking or continue
    request = input("Please input 'Y' for continue and new row input OR 'N' for exit from program \n").upper()
    if request == "N":
        break