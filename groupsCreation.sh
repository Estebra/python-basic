#!/bin/bash

groups=("Sales" "HR" "Finance" "Shipping" "Managers" "CEO")

for group in "${groups[@]}"
do
        sudo groupadd $group
done
