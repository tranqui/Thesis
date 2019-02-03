#!/usr/bin/env bash
cd tex;
for p in *.tex; do
    filename=${p%.*}
    if [[ $filename == "word-count" ]]
    then
       continue
    fi

    (texcount $p -merge -sum | head -n 10 | tail -n +3) > $filename.wordcount 2> /dev/null
    summary=($(head -n 1 $filename.wordcount))
    echo ${summary[2]} $'\t' $filename
done
