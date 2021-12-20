import os
import psutil


# 显示当前 python 程序占用的内存大小
def show_memory_info(hint):
	pid = os.getpid()
	p = psutil.Process(pid)
	
	info = p.memory_full_info()
	memory = info.uss / 1024. / 1024
	print('{} memory used: {} MB'.format(hint, memory))
	
if __name__ == '__main__':
	show_memory_info("a")