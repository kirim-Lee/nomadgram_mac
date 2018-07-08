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

# data base 
- setting
- Urls
- Apps

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
- 추가로 images 앱을 추가한다.
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