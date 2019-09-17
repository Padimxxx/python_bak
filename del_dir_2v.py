# encoding:utf-8
import time
import os
import datetime
import logging
import shutil
logging.basicConfig(level=logging.INFO,
                    filename="C:/python/python_scripts/del_dir.log" #有了filename参数就不会直接输出显示到控制台，而是直接写入文件
                    )

#定义删除文件夹的函数 del_directory(),参数my_path
def del_directory(my_path):
	#获取当前的时间转换成字符串格式	
	current_time=str(time.strftime("%Y-%m-%d",time.localtime()))
	#删除时间，方便日志查看
	del_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
	#遍历目标路径下的文件夹
	for d_f_name in os.listdir(my_path):
		#获取文件绝对路径
		full_dirct_path=os.path.join(my_path,d_f_name)
		#定义日期时间格式
		format='%Y-%m-%d'
		#获取文件最后修改时间		
		modifiedTime=time.localtime(os.stat(full_dirct_path).st_mtime)
		mTime=str(time.strftime("%Y-%m-%d",modifiedTime))			
		#判断修改日期距离今天为止的间隔时间（天）
		interval_time=datetime.datetime.strptime(current_time,format) - datetime.datetime.strptime(mTime,format)
		#判断修改日期距离今天是否大于x天
		if interval_time.days > 15:
			#判断是否为文件夹
			if os.path.isdir(full_dirct_path):
				#删除非空文件夹
				shutil.rmtree(full_dirct_path)
				logging.info(del_time+" 已成功删除[目录]: "+full_dirct_path)
			else:
				#删除文件
				os.remove(full_dirct_path)
				logging.info(del_time+" 已成功删除_文件_: "+full_dirct_path)

del_directory('D:\\wwwlog\\commctrl\\activities\\')
del_directory('D:\\wwwlog\\pandaAndroid\\')



