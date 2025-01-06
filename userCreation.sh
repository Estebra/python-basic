#!/bin/bash

# This is the way to make an array in a .sh script
names=("arosalez" "eowuso" "jdoe" "ljuan" "mmajor" "mjackson" "nwolf" "psantos" "smartinez" "ssarkar")
password="P@ssword1234!"

# Iterate through the array
for name in "${names[@]}"
do
        # Creates the user using the names in the array
        sudo useradd $name
        # Prints the password and uses the pipeline to direct the password to the passwd command
        # --stdin catches the password redirected by the pipeline, echo prints the password in the stardar intake
        echo $password | sudo passwd --stdin $name
done
