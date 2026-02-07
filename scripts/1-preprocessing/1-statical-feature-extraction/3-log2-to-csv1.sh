#!/bin/bash

# This script converts .log files in the specified input directory to .csv format.
# It extracts the header from log files, replaces tabs with commas, and saves the output in a structured directory.

input_dir="your input path"
output_dir="your input path"

find "$input_dir" -type f -name "*.log" | while read -r input_log; do
    output_csv="${output_dir}$(dirname "${input_log#$input_dir}")/$(basename "${input_log}" .log).csv"
    
    mkdir -p "$(dirname "$output_csv")"

    header=$(grep -m 1 "#fields" "$input_log" | sed 's/#fields[[:space:]]*//' | tr '\t' ',')

    data=$(grep -v '^#' "$input_log" | tr '\t' ',')

    {
        echo "$header"
        echo "$data"
    } > "$output_csv"

    echo "Conversion complete. CSV file saved as $output_csv"
done
