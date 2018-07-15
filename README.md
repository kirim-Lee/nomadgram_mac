python 설치
# pip설치
- python3 설치시에는 pip을 따로 설치할 필요가 없음
# pipenv 설치
- mac
    - brew install pipenv
- default
    - pip install pipenv

# django 설치
- pipenv 환경에 설치한다.
- mkdir 폴더명 : 폴더만들기
- cd 폴더명 : 폴더들어가기
- pipenv --three : 버블생성
- pipenv install django : 장고설치 
- pipenv shell : 버블안으로 들어가기

# django data base 
- setting
- Urls
- Apps
    - models
    - urls(Applications')
    - views
- App프로세스 :
    ```
     --> 유저는 브라우저에 요청 
     --> urls로 이동 
     --> view 실행시킴 
     --> model을 향함(django ORM이 위치함) 
     --> ORM을 통해 DB와 대화 오브젝트 돌려줌
     --> Views 
     --> Brower(유저)
     ```

## 1. models 
- the shape of the data that you are going to save on the database.
- (데이터베이스에 구조의 모양을 어떻게 저장할지에 관한 것)
- python classes
- describe the shape of the data of application
- create a table in the Database(ORM)
```
from django.db import models
# 테이블 만들기
class Cat(models.Model):
    name = models.CharField(max_length=30)
    breed = models.CharField(max_length=20)

# 데이터 찾기
cat = Cat.objects.get(id=1) --> 예상결과값이 하나
british_cats=Cat.objects.filter(breed="British")  --> 예상결과값이 여럿
## filter lookups 
cats = Cat.objects.filter(name__startswith="Mr") --> __lookups 이렇게 사용 다음 예제는 Mr로 시작하는것을 찾음

# 데이터 저장
# 위에서 찾은 cat
cat.name="fly" --> 수정
cat.save() --> 삭제는 cat.delete()

# 데이터 추가
Cat.objects.create(name="Fluffy",breed="Persian")
```
### model operations 
- create()
- get()
- filter()
- all()
- save()
- delete()

#### lookup options
- startswith : 시작하는
- contains : 들어있는
- istartswith : 대소문자 구분없이 시작
- icontains
- lt : 작은
- gt : 큰
- [...more](https://docs.djangoproject.com/en/1.11/topics/db/models/)

### _**migration**_
- 모델을 만들거나 수정하면 마이그레이션을 해주어야 데이터베이스에 반영된다.
- python manage.py migrate

## 2. urls
- django has one urls
- tell django to do stuff(A.K.A Execute a View) 
- (url을 통해 어떤것을 보여달라고 요청할 수 있다.)
- Is the protocol you use to make the app do something.
- (프로토콜로서 이를 사용해 앱을 실행시킨다.)
- HTTP Request
- The URLS of your project are a combination of all your app URLs
- nomad.com/login 이런식으로 요청할 수 있다.

## 3. Views
- Tell Django what to do 
- (무엇을 할지)
- triggered by a URL call
- (URL콜)
- Is just a python function
- (파이썬을 통한 함수)
- def showHomepage() 이런식으로 작성

# what is Django ORM
- ORM : Objct-relational mappers
- SQL : Structured Query Language / 데이터베이스와 대화할 때 쓰는 언어
- django ORM 은 SQL언어를 python언어로 해석할 수 있도록 도와주는 통역의 역할을 한다.
- Python 으로 작성하면 -> django가 번역 -> DB가 SQL을 이해


# cookiecutter 추가하기
- 장고프로젝트의 다른 프로젝트를 복사해 와서 커스터마이징 할 수 있도록 도와주는 도구이다.
- pip install cookiecutter
- https://github.com/pydanny/cookiecutter-django
    - 사용하는 것
# cookiecutter 설치
- pip install cookiecutter : cookiecutter는 전체적 설치
- pip3 install cookiecutter 
# 프로그램설치
- cookiecutter [주소]
- **cookiecutter https://github.com/pydanny/cookiecutter-django**

## cookiecutter-django 에서 불필요한 파일 삭제
```
/docs
/utility
/CONTRIBUTTORS.txt
/README.rst
/nomadgram/templates  // 테스트동안에는 테스트하기 위해 삭제를 유예할 수 있을 것같다.
```

---
# git 생성
- /nomadgram$ git init
- git remote add origin {address}
- git add .
- git commit -m "cookiecutter + clean up"
- git push origin master

# 가상환경 설치 / 필요한도구 설치
- /nomadgram$ pipenv --three : 가상환경 생성
- pipenv install -r requirements/local.txt : 필요하다고 정의된 것들을 설치함
- pipenv shell : 가상환경으로 들어감
- django-admin : 어드민실행 테스트

## 오류가 있을 경우 
- pip install -U setuptools (-u means upgrade.. maybe)
- pip install -U pip
- pipenv install -r requirements/local.txt

---

# settings
- config/setting/ 폴더에 설정 파일이 존재
- local.py : 로컬에서 쓰이는 설정파일
- production.py : 실제 빌드시 사용되는 설정파일
- base.py : local.py, production.py에서 import 하는 파일
    - 파일 내 사용되는 데이터 베이스 정의가 있다.
    - DATABASES ={'default': env.db('DATABASE_URL', default='postgres:///nomadgram'),}
    - 이 프로젝트에서는 postgres를 사용한다.

# 데이터베이스 생성
- mac에서 생성시
    - postgres를 실행해 사용유저에 들어가면 터미널이 열린다.
    - CREATE DATABASE [데이터베이스이름];
    - 여기서는 데이터베이스이름에 nomadgram을 입력함.
- window에서 생성하는 방법은 사뭇다르다.(따로 정리가 필요)

## 데이터베이스 구동 테스트
- pipenv shell
- manage.py가 있는 폴더로 이동 (가상환경으로 들어가면 가상환경을 만든 폴더로 이동되는 것 같다)
- **python manage.py runserver**

# app 추가하기
- /nomadgram 안에는 user앱이 존재한다.
- 추가로 _images_ 앱을 추가한다.
- nomadgram은 두가지 앱을 사용. 

## app 추가 : nomadgram/users 와 같은 레벨에서 실행
```
django-admin startapp images
```
- /nomadgram/images 가 생성된다. 하위 파일도 함께 생성

## app 인지시키기
- /settings/base.py  
- INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
- DJANGO_APPS : 설치될 때 기본적으로 사용하는 것
- THIRD_PARTY_APPS : 인터넷등에서 찾아 추가해 사용하는 것
- LOCAL_APPS : 사용자가 직접 추가하는 것
- LOCAL_APPS 여기에 우리가 추가한 images를 추가한다.
    - nomadgram/images/apps.py 의 ImageConfig name='images' 를 **name='nomadgram.images'** 로 수정한다.
    - /settings/base.py 의 LOCAL_APPS= 에 **'nomadgram.images.apps.ImagesConfig',** 를 추가한다.

## pipenv 환경에서 migration
- python manage.py migrate

---

# Model 작업

## 슈펴유저만들기
- python manage.py create superuser
- localhost:8000/admin/ 에 슈퍼유저로 접속 할 수 있다.

## Create User Model

### references
- [Classes on Python](https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/)
- [Django model](https://docs.djangoproject.com/en/1.11/topics/db/models/)
- [DjangoField](https://docs.djangoproject.com/en/1.11/ref/models/fields/)

## user model 
```
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
```
- 기본적으로 제공되는 유저모델
- 사용시 마이그레이션과 base.py 등에서 **AUTH_USER_MODEL** 이 생성한 모델을 가리키도록 해야함 

#### from django.db import models

- models.CharField(max_length=100)
    - CharField에서 _max_length_ 필수 
- models.TextField(_null=True_)
    - null값이 가능하게 허용
- models.ImageField()
- medels.BooleanField(default=False)
- models.CharField(max_length=80,choices=GENDOR_CHOICES)
    - choices 셀렉트 값을 제공함
    ```
    GENDOR_CHOICES = (
        ('male','Male'),
        ('female','Female'),
        ('not-specified','Not specified')
    )
    //앞의 값이 모델에 사용되고 뒤의값은 보기 편한 단어
    ```

- models.**ForeignKey**(Owner,null=True) (ManyToOne)
- models.**ManyToManyField**('self')