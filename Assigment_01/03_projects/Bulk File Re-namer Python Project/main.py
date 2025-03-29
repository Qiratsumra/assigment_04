import os 
def main():
    i  =0 
    path ='C:/Users/qirat.kinza/Desktop/streamlit_projects/Assigmemt_04/Assigment_01/03_projects/Bulk File Re-namer Python Project/'
    for file_name in os.listdir(path):
        my_dest = 'image' + str(i) + '.jpg'
        my_source = path +file_name
        my_dest = path + my_dest 
        os.rename(my_source, my_dest)
        i += 1

if __name__ == '__main__':
    main()