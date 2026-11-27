
notes = [
    "IMPORTANT: Study for the math exam on Friday\n",
    "Buy groceries after school\n",
    "TODO: Finish the Python file handling project\n",
    "Clean my desk and organize books\n",
    "IMPORTANT: Submit permission slip tomorrow\n",
    "Call grandma in the evening\n",
    "TODO: Practice coding exercises for 30 minutes\n"
]

with open("class-notes.txt", "w") as file:
    file.writelines(notes)


print("--- Part 1: First 40 characters ---")
with open("class-notes.txt", "r") as file:
    print(file.read(40))


# Part 2
print("\n--- Part 2: Numbered lines ---")
with open("class-notes.txt", "r") as file:
    lines = file.readlines()
    print(f"Total lines: {len(lines)}")
    for i in range(len(lines)):
        print(f"{i + 1}. {lines[i].strip()}")



print("\n--- Part 3: Reading one line at a time ---")
with open("class-notes.txt", "r") as file:
    for line in file:
        print(line.strip())



print("\n--- Part 4: Kept or Skipped ---")
with open("class-notes.txt", "r") as file:
    for line in file:
        clean_line = line.strip()
        if clean_line.startswith("IMPORTANT") or clean_line.startswith("TODO"):
            print(f"Kept: {clean_line}")
        else:
            print(f"Skipped: {clean_line}")


with open("class-notes.txt", "r") as source_file:
    with open("organized-notes.txt", "w") as target_file:
        for line in source_file:
            if line.startswith("IMPORTANT") or line.startswith("TODO"):
                target_file.write(line)



print("\n--- Part 6: Contents of organized-notes.txt ---")
with open("organized-notes.txt", "r") as file:
    for line in file:
        print(line.strip())