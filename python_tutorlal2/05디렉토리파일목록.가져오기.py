import os,glob

""" 이걸 언제쓰나? 파일 이름을 가져와서 그 파일 이름으로 파일을 열고 
안에 내용을 이용하거나 수정할 떄 요긴하다. """
folder_path='C:/Users/seeti/git/python_tu/python_tutorial'
file_namelist=os.listdir(folder_path)
print(file_namelist)

# files='*.py'  # 확장자가 py인것만 가져오기 
# file_namelist=glob.glob(files)
# print(file_namelist)