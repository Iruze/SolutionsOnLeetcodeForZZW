# 一共三种方法：

# Read from the file file.txt and output the tenth line to stdout.
# solution1:
tail -n +10 file.txt | head -1

# solution2:
awk 'NR==10{print $0}' file.txt

# solution3:
sed -n '10p' file.txt
