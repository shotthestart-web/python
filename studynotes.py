import os


with open("file1.txt", "w") as f:
    f.write("Hello world!\nPython file handling is simple.")

with open("file2.txt", "w") as f:
    f.write("Learning how to merge files.\nKeep practicing every day!")

output_file = "merged_output.txt"


if os.path.exists(output_file):
    os.remove(output_file)
    print(f"Old '{output_file}' removed.")


with open("file1.txt", "r") as f1:
    content1 = f1.read()

with open("file2.txt", "r") as f2:
    content2 = f2.read()


with open(output_file, "w") as out_f:
    out_f.write(content1 + "\n" + content2)


total_words = 0
print("\n--- Merged File Content ---")

with open(output_file, "r") as final_f:
    for line in final_f:
        print(line.strip()) 
        words = line.split() 
        total_words += len(words)

print("---------------------------")
print(f"Total word count: {total_words}")