#!/bin/bash
# these are the variables, name and folder for the files 
name="Esteban"
folder="./files/"

# this pulls the files from the folder and filters the lastone sorting them by the number, if empty returns cero.
last_file=$(ls ./files/| sort -V | tail -n 1 || echo 0)

# this takes the name part and leaves just the number
numbers="${last_file##Esteban}"

# gets the next number for the files
next_number=$((numbers + 1))

# loops for 1 to 25 base on the last number from the files names, if empty, starts with 1
for i in {1..25}; do
	number=$((next_number + i - 1))
	touch "$folder$name$number"
done
