### Github

$ git clone \<url>

- 원격 저장소의 프로젝트를 가져오기
- 저장소 프로젝트를 전부 가져옴



$ glt pull origin master

- 원격 저장소의 커밋 변경 사항을 가져옴



### Github

#### branch

- 버전 관리를 위한 새로운 루트를 생성



$ git branch example

- example 이라는 branch 생성



$ git branch

- branch 목록 확인



$ git checkout example

- example 브랜치로 이동



#### Merge

- 브랜치를 병합

$ git checkout master

- 마스터로 이동

$ git merge example

- 마스터에 example 브랜치를 병합



#### branch 삭제

$ git branch -d example

- 이미 병합된 브랜치는 반드시 삭제한다



#### branch 생성하며 이동

$ git checkout -b feature/about