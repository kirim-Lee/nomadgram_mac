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
- pip install -U setyptools (-u means upgrade.. maybe)
- pip install -U pip
- pipenv install -r requirements/local.txt

