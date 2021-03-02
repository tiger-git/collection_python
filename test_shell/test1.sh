#!/bin/bash
#TODO 系统命令执行
#ls /home/tiger/
#TODO 定义变量
#方式1
#name='tiger'
#echo ${name}
#echo ${name}你好
#方式2
#for file in `ls /home/tiger`
##for file in $(ls /home/tiger/)
#do
#  echo $file
#done

#变量拓展
#var=apple
#apple='苹果'
#echo $apple
#echo $var
#echo ${!var}# 取参数的值

#字符串处理
#litter="helloWolld"
#echo $litter
#echo ${litter^}
#echo $litter
#new_litter=${litter^^}
#echo 新的"${new_litter}"
#echo ${litter^^}
#echo ${litter,}
#echo ${litter,,}
#echo ${litter~}
#echo ${litter~~}


#TODO 启动文件传参
echo "param1:$1"
echo "param2:$2"
echo "param3:$3"

echo $1
echo $2
echo $3
name="$4"
echo $name

