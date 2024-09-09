#!/bin/bash

name=$1
echo "name: " $name

url="http://localhost:8080/api/test/u"
response=$(curl -o /dev/null -s -w "%{http_code}" $url)

echo "Status code from $url: " $response