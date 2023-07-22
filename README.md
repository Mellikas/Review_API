# Autoservice

The first Django REST framework project created during the CodeAcademy course.

**DESCRIPTION**

The website was created to familiarize with:
- Django framework
- HTML templates
- SQLite 
- Django REST framework 

**HOW TO INSTAL AND RUN**

1. Create a new project in your IDE (e.g. PyCharm)
2. Download zipped project
3. Upload the unzipped files to the newly created project
4. In terminal run: `pip install -r requirements.txt`
6. In terminal run: `python manage py makemigrations`
7. In terminal run: `python manage py migrate`
8. In terminal run: `python manage.py createsuperuser` and creat admin user (while typing pasword it won't appear)
9. In terminal run: `python manage.py runserver localhost:18080` (or similar `localhost: 18000` etc.) 
10. Push on active server link in terminal.
11. Go to http://localhost:18080/admin/ and add data in this order:
    1. Users
    2. Bands
    2. Albums
    3. Songs
12. Go to http://localhost:18080/ and add following endpoints:
- bands/
- bands/**"insert band ID"**/albums/
- bands/**"insert band ID"**/albums/**"insert Album ID"**/songs/ 
- albumreviews/ 
- albumreviews/**"insert albumreview ID"**/
- albumreviews/**"insert albumreview ID"**/comments/
- albumreviews/**"insert albumreview ID"**/comments/**"insert comments ID"**/ 
- albumreviews/**"insert albumreview ID"**/likes/

13. In the corresponding endpoint you can create/view/edit/delete the corresponding content.

**CREDITS**
   
The project was created with CodeAcademy (https://codeacademy.lt/en/) educational materials.
