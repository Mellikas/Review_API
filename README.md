# Review_API

The first Django REST framework project created during the CodeAcademy course.

**DESCRIPTION**

The website was created to familiarize with:
- Django REST framework 
- Django framework
- SQLite

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
    4. Album reviews
    5. Album review likes
12. Go to http://localhost:18080/ and add following endpoints to see data:
- bands/
- bands/**"insert band ID"**/albums/
- bands/**"insert band ID"**/albums/**"insert Album ID"**/songs/ 
- albumreviews/ 
- albumreviews/**"insert albumreview ID"**/
- albumreviews/**"insert albumreview ID"**/comments/
- albumreviews/**"insert albumreview ID"**/comments/**"insert comments ID"**/ 
- albumreviews/**"insert albumreview ID"**/likes/
- signup/

13. Through your IDE terminal you can GET or POST data:
    - First you must **get your user TOKEN**:
      - In terminal run: `http POST http://localhost:18080/api-token-auth/ username=admin password=admin`
      - Copy it from terminal and save it.
    - **Get any data**:
      - In terminal run: `http localhost:18080/"insert an endpoint from above"/`
    - **Creat**:
      - New like:
        - in terminal run: `http POST http://localhost:18080/albumreviews/1/likes/ "Authorization: Token 761fee26e056d4fc065dc4edf7c2b1b9482d6f40"` 
      - New albumreview:
        - in terminal run: `http POST http://localhost:18080/albumreviews/ album_id="3" review_content="NEW review" score="8" "Authorization: Token 9e148e5b5ab42279939212ab77df3d582f2c2283"` 
      - *Comment*:
        - *Insert **your generated** token*.
        - *Insert existing **album_id** number*. 
        - *Create custom **review_content** and **score***.

14. Your request can be made via python: 
- `import requests`
  - **Post data:**   
    ```  
    url = 'http://localhost:18080/albumreviews/'
    headers = {'Authorization': 'Token 9e148e5b5ab42279939212ab77df3d582f2c2283'}
    myobj= {'album_id': '1','review_content': 'New, new, new','score': '5'}
    r = requests.post(url, headers=headers, json=myobj)
    print(r.json())
    ```
  - **Get data:**
    ``` 
    url = 'http://localhost:18080/albumreviews/'
    headers = {'Authorization': 'Token 9e148e5b5ab42279939212ab77df3d582f2c2283'}
    r = requests.get(url, headers=headers)
    print(r.json())
    ``` 

**CREDITS**
   
The project was created with CodeAcademy (https://codeacademy.lt/en/) educational materials.
