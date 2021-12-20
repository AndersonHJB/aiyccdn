import json
import os
import random
from uuid import uuid4
import logging

class Compare_the_data(object):
	def __init__(self, path_list):
		"""
		path_list: 路径列表
		"""
		self.path_list = path_list
		# self.fileName = uuid4()
		logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		self.logger = logging.getLogger(__name__)
		self.filename = str(uuid4())

	# def save(self, list_data):
	# 	"""
	# 	列表嵌套列表
	# 	:param list_data:
	# 	:return:
	# 	"""
	# 	try:
	# 		if len(list_data) > 1:
	# 			for datas in list_data:
	# 				fileName = str(uuid4())
	# 				with open(f"{fileName}.txt", "w+", encoding="utf-8") as f:
	# 					for data in list_data:
	# 						f.write(data + "\n")
	# 						f.close()
	# 		else:
	# 			fileName = str(uuid4())
	# 			with open(f"{fileName}.txt", "w+", encoding="utf-8") as f:
	# 				for data in list_data:
	# 					f.write(data + "\n")
	# 					f.close()
	#
	# 	except TypeError as e:
	# 		self.logger.info(e)

	def write(self, data):
		with open(f"{self.filename}.txt", mode="a+", encoding="utf-8")as f:
			f.write(json.dumps(data, ensure_ascii=False) + "\n")

	def parse_list(self, list_data):
		if isinstance(list_data[0], list):
			for data in list_data:
				for da in data:
					self.write(da)
		else:
			for data in list_data:
				self.write(data)


	def read_path(self):
		try:
			if len(self.path_list) > 1:
				data = []
				for filePath in self.path_list:
					list_data = os.listdir(filePath)   # 读取结果存入 list_data
					# print(list_data)
					data.append(list_data)
				return data
			else:
				list_data = os.listdir(self.path_list[0])
				return list_data
		except IndexError as e:
			self.logger.info(e)

	def main(self):
		data = self.read_path()
		self.parse_list(data)
		self.logger.info("Successful！")

if __name__ == '__main__':
	path = input('Please your input Path(path1,path2....):>>>')
	list_spilt = path.strip().split(',')
	compare = Compare_the_data(list_spilt).main()
# D:\Windows_Code\sublime text\Java零基础,D:\Windows_Code\sublime text\Java零基础特训班_在线课程学习_万门-大学
# D:\Windows_Code\sublime text\Java零基础特训班_在线课程学习_万门-大学
# filePath = r'D:\application\wm\download\Java零基础特训班_在线课程学习_万门-大学'     # 要读取的文件夹的目录)
# filePath = r'D:\application\N_m3u8DL-CLI_v2.9.7_with_ffmpeg_and_SimpleG\Downloads\Java零基础特训班'     # 要读取的文件夹的目录))

# # print(list_data)
# list_file = []
# for data in list_data:
# 	list_file.append(data[:-4])
# print(list_file)
# with open("list_file.txt", "w+", encoding="utf-8")as f:
# 	for i in list_file:
# 		f.write(i + "\n")  