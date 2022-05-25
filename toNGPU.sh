

origin=$1
destiny=$2

echo "Sending $1 to $2..."

scp $1 vlugli@ngpu.ugr.es:/home/vlugli/homeGPU/$2
