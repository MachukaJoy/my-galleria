#  My Galleria Application

### A personal gallery application that you display your photos for others to see.

#### By **Joy Machuka**

+ [Description](#Description)
+ [How to run the code](#Setup)
+ [Live Site](#Live-Site)
+ [Technologies](#Technologies-and-Languages-Used)
+ [Authors Info](#Author)
+ [Licence](#Licence)

# Description
This is a Django application for personal gallery that allows a user to upload images for other to see and be able to to share by coping the image link.

## Live-Site
[View Site](https://machukagalleria.herokuapp.com/)


## BDD
* As a user, I would like to view different photos that interest me.
* As a user, I would like to click on a single photo to expand it and also view the details of the photo.
* As a user, I would like to search for different categories of photos.
* As a user, I would like to view photos based on the location they were taken.

## Setup

To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/MachukaJoy/my-galleria.git 
```
##### Navigate into the folder
 ```bash 
cd my-galleria
```
##### Create and activate virtual environment  
 ```bash 
pipenv –-three
```
##### Activate Virtual Environment
 ```bash 
- pipenv shell 
```  
##### Install Dependencies  
 ```bash 
 pipenv  install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations gallery
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test gallery
```
Open the application on your browser `127.0.0.1:8000`.


## Known Bugs
There are not any known bugs as at now. But feel free to let us know should you find any.

## Technologies-and-Languages-Used
* Python
* Visualstudio
* Django
* postgress sql

## Support and contact details
Should you have any issues or questions, ideas or concerns feel free to reach out to me. Also feel free to make contribution to the code and can contact me at machukajoy@gmail.com
## Author

- [Joy Machuka](https://github.com/MachukaJoy)
### Licence
[MIT LICENSE](https://github.com/MachukaJoy/my-galleria/blob/main/LICENSE)<br>


** <br>
Copyright (c) {2022} [Joy Machuka ](https://github.com/MachukaJoy)