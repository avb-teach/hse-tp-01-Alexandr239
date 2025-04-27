#!/bin/bash

input_dir=""
output_dir=""
max_depth=""

if [[ $# -eq 2 ]]; then
  if [[ $1 != "--max_depth" ]]; then
    input_dir=$1
    output_dir=$2
  fi
fi
if [[ $# -eq 4 ]]; then
  if [[ $1 == "--max_depth" ]]; then
    max_depth=$2
    input_dir=$3
    output_dir=$4
  fi
  if [[ $3 == "--max_depth" ]]; then
    max_depth=$4
    input_dir=$1
    output_dir=$2
  fi
fi

if [[ $input_dir == "" ]]; then
  echo "Illegal parameters" >&2
  exit 2
fi

python3 collect_files.py "$input_dir" "$output_dir" "$max_depth"
