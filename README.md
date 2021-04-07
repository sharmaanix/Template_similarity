# Template Matching

## Introduction 

The Template Matching Algorithm consist of two parts:
 - Firstly, It takes the input image, and figure out the contour within paragraph and group of words, letters and symbols. It will generate many such segments, which is cropped and saved as list of segment.
 - Secondly, we load the template folder, and match the segments of input image with template images.
- At last, It counts the number of matches with the template, the template with highest number of matches is returned as an output.

 

## Installation


Clone from Git
```bash
git clone git@github.com:sharmaanix/Template_similarity.git
cd Template_similarity
sudo docker-compose up --build
```

Accessing the app in local browser, For example
 
```bash
GET http://0.0.0.0:8000/match?image_path=Document_Dataset/inputs/document-000-100647.out.000.png&template_folder_path=Document_Dataset/templates

RESPONSE as

{
  "input_filename": "Document_Dataset/inputs/document-000-100647.out.000.png", 
  "template_file_name": "Document_Dataset/templates/document-006-101162.in.000.png"
}
```

# Efficiency

# Result
![img](result.jpg) 

