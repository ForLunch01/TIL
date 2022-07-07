# Git/GitHub



## Git

- 분산형 버전 관리 툴



### 기본 명령어

git init

- 특정 폴더를 git 저장소로 만들어 관리



git add \<file>

- working directory 상의 변경 내용을 staging area에 추가하기 위해 사용
  - untracked 상태의 파일을 staged로 변경
  - modified 상태의 파일을 staged로 변경



git commit -m '<커밋메시지>'

- staged 상태의 파일들을 커밋을 통해 버전으로 기록



#### 현재 상태를 알고 싶다면

git log

- 현재 저장소에 기록된 커밋을 조회



git status

- Git 저장소에 있는 파일의 상태를 확인



## GitHub

#### 로컬저장소의 버전을 원격저장소로 보내기

$ git remote add origin \<url>



git push

- 원격 저장소로 로컬 저장소 변경 사항(커밋) 올림(push)
- 로컬 폴더의 파일/폴더가 아닌 저장소의 버전(커밋)이 올라감

