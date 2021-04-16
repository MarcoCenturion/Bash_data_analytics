#!/bin/bash

echo 'valor coinnomi1'
read coinnomi1
echo 'valor coinnomi2'
read coinnomi2
echo 'valor Bitcoin ripio'
read bitripio
echo 'valor Ether ripio'
read ethripio
echo 'valor blue'
read blue
total=$(((($connomi1+$coinnomi2)*$blue)+$bitripio+$ethripio))

echo total $total
