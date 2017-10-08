import os
import glob
import stat
import shutil

Path = r'C:\Users\hp\Desktop' #Desktop Path
Destination = r'C:\Users\hp\Desktop\Desktop_C'
Folder_name = 'DMA_Folder'
Sub_Folders = ['Codes','Audio','Video','Image','Documents','Others','Folders']
Folder_mapping = {'Codes': ['.C','.cc','.cxx','.cpp','.c++','.asp','.aspx','.axd','.asx','.asmx','.ashx','.cfm','.yaws','.htm','.html','.xhtml','.shtml','.jhtml','.jsp','.jspx','.wss','.do','.action','.pl','.php','.php4','.php3','.phtml','.py','.rb','.rhtml','.rss','.xml','.cgi','.dll','.fcgi'],
                  'Music':['.3gp','.aa','.aac','.aax','.act','.aiff','.amr','.ape','.au','.awb','.dct','.dss','.dvf','.flac','.gsm','.iklax','.ivs','.m4a','.m4b','.m4p','.mmf','.mp3','.mpc','.msv','.ogg','.oga','.mogg','.opus','.ra, .rm','.raw','.sln','.tta','.vox','.wav','.wma','.wv','.webm','.8svx'],
                  'Video':['.yuv','.wmv','.webm','.vob','.svi','.roq','.rmvb','.rm','.ogv','.ogg','.nsv','.mxf','.mpg','.mpeg','.m2v','.mpg','.mp2','.mpeg','.mpe','.mpv','.mp4','.m4p','.m4v','.mov','.qt','.mng','.mkv','.m4v','.gifv','.gif','.flv','.f4v','.f4p','.f4a','.f4b','.flv','.flv','.drc','.avi','.asf','.amv','.3gp','.3g2'],
                  'Image':['.tif','.tiff','.gif','.jpeg','jpg','.jif','.jfif','.jp2','.jpx','.j2k','.j2c','.fpx','.pcd','.png'],
                  'Documents':['.DOC','.DOCX','.ODT','.PDF','.XLS','.XLSX','.ODS','.PPT','.PPTX','.TXT']}
Files_l= os.listdir(Path)
#To setup the folder structure
if not os.path.exists(os.path.join(Path,Folder_name)):
    os.makedirs(os.path.join(Path,Folder_name))

for name in Sub_Folders:
    if not os.path.exists(os.path.join(Path,Folder_name,name)):
        os.makedirs(os.path.join(Path,Folder_name,name))
#End of folder structure setup
'''
print(Files_l)

for file in Files_l:
    print(file)
    print(os.path.isfile(os.path.join(Path,file)))
'''

for file in Files_l:
    count = 0 #To check for Others and Folders
    for key,values in Folder_mapping.items():
        for ext in values:
            if file.lower().endswith(ext.lower()) and count==0:
                if os.path.exists(os.path.join(Path,Folder_name,key,file)):
                    try:
                        os.remove(os.path.join(Path,Folder_name,key,file))
                    except PermissionError as exc:
                        os.chmod(os.path.join(Path,Folder_name,key), stat.S_IWUSR)
                        os.remove(os.path.join(Path,Folder_name,key,file))
                count = 1
                shutil.move(os.path.join(Path,file),os.path.join(Path,Folder_name,key))
    if os.path.isfile(os.path.join(Path,file)) and count==0:
        if os.path.exists(os.path.join(Path,Folder_name,'Others',file)):
            try:
                os.remove(os.path.join(Path,Folder_name,'Others',file))
            except PermissionError as exc:
                os.chmod(os.path.join(Path,Folder_name,'Others'), stat.S_IWUSR)
                os.remove(os.path.join(Path,Folder_name,'Others',file))
        count = 1
        shutil.move(os.path.join(Path,file),os.path.join(Path,Folder_name,'Others'))
    if os.path.isdir(os.path.join(Path,file)) and file != Folder_name and count==0:
        if os.path.exists(os.path.join(Path,Folder_name,'Folders',file)):
            try:
                shutil.rmtree(os.path.join(Path,Folder_name,'Folders',file))
            except PermissionError as exc:
                os.chmod(os.path.join(Path,Folder_name,'Folders'), stat.S_IWUSR)
                shutil.rmtree(os.path.join(Path,Folder_name,'Folders',file))
        shutil.move(os.path.join(Path,file),os.path.join(Path,Folder_name,'Folders'))

#glob.glob(Path/'//*.py')
#os.path.join()
#print(os.path.join('/Users/pilgrim/diveintopython3/examples', 'humansize.py'))








