import os

def process_file(filepath):
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()

        new_lines = []
        for i, line in enumerate(lines):
            if line.startswith('"'):
                print(f'Line {i+1} starts with a quotation mark in file: {filepath}')
                line = line.lstrip('"')
                if new_lines:
                    new_lines[-1] = new_lines[-1].rstrip('\n') + '"' + '\n'
                new_lines.append(line)
            else:
                new_lines.append(line)

        with open(filepath, 'w') as new_file:
            new_file.writelines(new_lines)

        print(f'Processed file saved as: {filepath}')

    except Exception as e:
        print(f"Error processing file {filepath}: {e}")

def process_directory(input_directory):
    for root, _, files in os.walk(input_directory):
        for file in files:
            filepath = os.path.join(root, file)
            process_file(filepath)

if __name__ == "__main__":
    input_directory_path = f'your input path'
    process_directory(input_directory_path)
