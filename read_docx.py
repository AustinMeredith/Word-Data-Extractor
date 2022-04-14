import docx2txt as d2t

def extract_images(path_to_file, images_folder, get_text=False):

    text = d2t.process(path_to_file, images_folder)
    
    if(get_text):
        return text 
        
        
path_to_file = 'C:/Users/da6ar/OneDrive/Documents/Senior Project/Data_Extractors_Charter.docx'
images_folder = 'C:/Users/da6ar/OneDrive/Documents/Senior Project/images/'

data = extract_images(path_to_file, images_folder, get_text=True)

print(data)

#feed data into other classes