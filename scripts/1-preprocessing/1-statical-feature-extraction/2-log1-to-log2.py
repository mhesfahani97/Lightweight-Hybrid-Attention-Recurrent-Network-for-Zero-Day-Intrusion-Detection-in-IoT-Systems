import os

def process_line(line):
    if line.startswith('#'):
        return line

    line = line.replace('"', '')

    fields = line.split('\t')

    for i in range(len(fields)):
        if ',' in fields[i]:
            fields[i] = f'"{fields[i]}"'

    return '\t'.join(fields)

def process_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    processed_lines = [process_line(line) for line in lines]

    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    with open(output_file_path, 'w') as file:
        file.writelines(processed_lines)

def find_log_files(directory_path):
    log_files = []
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.log'):
                log_files.append(os.path.join(root, file))
    return log_files

def process_directory(input_directory_path, output_directory_path):
    log_files = find_log_files(input_directory_path)
    for input_file_path in log_files:
        relative_path = os.path.relpath(input_file_path, input_directory_path)
        output_file_path = os.path.join(output_directory_path, relative_path)
        process_file(input_file_path, output_file_path)

if __name__ == '__main__':
    input_directory_path = 'your-path'
    output_directory_path = 'your-path'
    process_directory(input_directory_path, output_directory_path)
