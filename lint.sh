#!/bin/bash
function read_dir(){
for file in `ls $1` #注意此处这是两个反引号，表示运行系统命令
do
  if [ -d $1"/"$file ] #注意此处之间一定要加上空格，否则会报错
  then
    if [ "$file" != ".git" ] && [ "$file" != "__pycache__" ] && [ "$file" != "venv" ]
    then
      read_dir $1"/"$file
    fi
  else
    if [[ "$file" =  *".py" ]]
    then
        # echo $1"/"$file
        # TODO: add autopep8 here.
        autopep8 --in-place --aggressive --aggressive $1"/"$file

        # TODO: add autoflake here.
        autoflake --in-place --remove-unused-variables $1"/"$file

        # TODO: add isort here.
        isort $1"/"$file
    fi
  fi
done
}
read_dir "."

# TODO: add flake8 here.
 flake8 .
