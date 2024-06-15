#!/bin/zsh

ext=$1

openURL() {
    if [[ $ext == .* ]]; then # check if $ext starts with a dot
        ext="${ext:1}"        # remove that dot (first character)
    fi
    echo "https://fileinfo.com/extension/$ext"
    open "https://fileinfo.com/extension/$ext" # open FileInfo page with specified extension
}

case $ext in
    "") 
        # no input
        echo "Interactive mode"
        while true; do
            echo -n "File Extension: "
            read ext
            openURL
        done
        ;;

    *)
        openURL
        ;;

esac
