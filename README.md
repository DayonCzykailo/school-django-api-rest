# django-api
Creating a Django api for fun ...

This Django API Rest have basic authorization system, all methods HTTP {PUT, POST, GET, DELETE, PATCH}, routes customized, POO and others.

i made an API for a simple school, so its have Students, Course and Registration.
and i made some .bat file to simplify the development and put some validations, paginations, ordenations, filters and versioning.

Using:
- validate-docbr
- django
- django-framework
- requests
- django-filter

# Django flowchart
![alt text](https://cdn1.gnarususercontent.com.br/1/103811/6bd3c17a-2dc3-4db2-9fcd-a0b2447ade89.png)

# Django REST Framework flowchart
![alt text](https://cdn1.gnarususercontent.com.br/1/103811/6bd3c17a-2dc3-4db2-9fcd-a0b2447ade89.png)

# DRF data flowchart
![alt text](https://cdn1.gnarususercontent.com.br/1/103811/f69d24ff-84fe-4f8c-94a0-843d06e9ab85.png)


# Student List
```
ENDPOINT /students/
```
# GET
```json
[
    {
        "id": 1,
        "name": "Dayon",
        "email": "dayon.czykailo@email.com",
        "cpf": "12345678900",
        "birth_date": "2024-11-18",
        "phone": "99999999999999"
    }
]
```
# PUT
```json
{
    "name": "Dayon",
    "email": "dayon.czykailo@email.com",
    "cpf": "12345678900",
    "birth_date": "2024-11-18",
    "phone": "99999999999999"
}
```

# PATCH
->`/students/<id>`
```json
{
    "name": "Dayon",
    "email": "dayon.czykailo@email.com",
    "cpf": "12345678900",
    "birth_date": "2024-11-18",
    "phone": "99999999999999"
}
```
# DELETE
->`/students/<id>`

# Course List
```
ENDPOINT /courses/

level:
('B', 'Basic')
('I', 'Intermediate')
('A', 'Advanced')
```
# GET
```json

[
    {
        "id": 1,
        "code": "0000000001",
        "description": "Java",
        "level": "B"
    },
    {
        "id": 2,
        "code": "ABC-000002",
        "description": "Django/Python Course",
        "level": "I"
    }
]
```

# PUT
```json
{
    "code": "ABC-000002",
    "description": "Django/Python Course",
    "level": "I"
}
```

# PATCH
->`/courses/<id>`
```json
{
    "code": "ABC-000002",
    "description": "Django/Python Course",
    "level": "I"
}
```
# DELETE
->`/courses/<id>`

# Registration List
```
ENDPOINT /registrations/
```
# GET
```json
[
    {
        "id": 1,
        "period": "M",
        "student": 1,
        "course": 1
    }
]
```
# PUT
```json
{
    "id": 1,
    "period": "M",
    "student": 1,
    "course": 1
}
```

# PATCH
->`/registrations/<id>`
```json
{
    "period": "M",
    "student": 1,
    "course": 1
}
```
# DELETE
->`/registrations/<id>`
