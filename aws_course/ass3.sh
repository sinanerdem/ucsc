#!/bin/bash

aws ec2 create-security-group --group-name AWSass3 --description "Security group created for assignment 3"

aws ec2 authorize-security-group-ingress --group-name AWSass3 --protocol tcp --port 22 --cidr 50.136.246.176/24

aws ec2 create-key-pair --key-name="ass3key"

aws ec2 run-instances --image-id ami-42908907 --count 2 --instance-type t2.micro --key-name ass3key --security-groups AWSass3 --output text  | awk -F"\t" '$1=="INSTANCES" {print $8}'

aws ec2 terminate-instances --instance-ids i-94663a57 i-95663a56

http://unix.stackexchange.com/questions/121718/how-to-parse-json-with-shell-scripting-in-linux



