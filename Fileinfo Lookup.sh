#!/bin/zsh


while true
do

echo -n "File Extension: " 
read ext

if [[ -z "${ext// }" ]]; then # if there is no input
    echo "No extension entered! Please enter a file extension"
    
else
    if [[ $ext == .* ]]; then # check if $ext starts with a dot
        ext="${ext:1}"
    fi
    echo "https://fileinfo.com/extension/$ext"
    open "https://fileinfo.com/extension/$ext" # open Fileinfo page with specified extension
fi

done
