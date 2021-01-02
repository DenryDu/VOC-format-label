# VOC tools 
![](https://img.shields.io/badge/language-python-green.svg)
![](https://img.shields.io/badge/VOC-TOOL-v1.0.0-519dd9.svg)

A tool for formating and labeling with VOC FORMAT        
> 按照VOC格式规格化图片并加标签的工具
## Table of Contents
- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Related Efforts](#related-efforts)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Background
As computer vision developers, every time we try to train a new model to complete a new classification or Identification task, we run into the thorny problem of missing a specific data set.Although there are tons of data on the Internet, but in practical application, the data we need is more or less differernt from existing data sets, so in this case we need to make a new data set. Given that many model dealing with VOC-format data sets, so we need a tool to format the image data into the VOC format, that's the reason this project has been made for.
> 作为计算机视觉方向的开发者，每当我们想要训练一个新的模型来完成一个新的分类或者识别项目时，我们总会遇到一个棘手的问题，那就是缺少特定数据集。网上的公开数据集虽然多，但是在实际应用当中，我们所需要的数据却又或多或少会和已有的数据集有所区别，所以在这样的情况下就需要为已经搭建好的模型制作新数据集了，鉴于很多模型都处理的是VOC格式的数据集，因此我们需要一个将图片数据格式化为VOC格式的工具，本项目也就应运而生
## Install
Just **Download** and **Unzip** the repo!

## Usage
[1] Modify Path_Variables in Shells      

> Replace **"PATH_TO_CURRENT_FOLDER"** with **absolute path** of where you download and unzip **the repo**

[2] Pack all images together into a new folder named **JPEGImages**    

[3] Copy the two shell files to where sibling with the folder **JPEGImages** 

[4] Run the compile.sh         
```
bash compile.sh
```
[5] Run the label.sh    
``` 
bash label.sh
```

## Related Efforts
## Maintainers
[@DenryDu](https://github.com/DenryDu)
## Contributors
## License

***
If you find this useful, please star it! :)
