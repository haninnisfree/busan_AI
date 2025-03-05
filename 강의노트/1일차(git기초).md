### 첫 날
1) git 설치
2) visual studio 설치
3) git hub 레퍼지토리 생성, visual studio 연동
    * git은 master가 아니라 main이 기본 값이다. 
    * git은 linux 운영체제를 따른다. 
        - MAC이 Linux와 운영체제 환경이 비슷하기 때문에 현업에서도 MAC을 사용한다. 
        - Linux 명령어 : ls, cd, mkdir, rm / git clone, git clone, git push
    
### 2일차
폴더 하나에다가 .git 폴더가 하나 생성될 것이다. 
이것들이 중첩되면, 충돌이 생기기 때문에 관리해야한다. 

1) 폴더 생성 후 git 설정
git config -l # 현재 셋팅 값
git config --unset user.name # 현재 유저 이름 지우기
git config --unset user.email # 현재 유저 이메일 지우기
git config --global init.defaultBranch main # branch를 main으로 설정
git init 
* .git 폴더 생성
    - git 초기 정보 값들이 알아서 들어간다. 
ls -al # 숨긴 폴더 및 파일까지 보여준다.
git status # git 상태 체크
* 지금 add . 를 안해서, git hub에 commit 된 게 하나도 없다. 
즉, git hub에 내가 작업한 내용이 올라가 있지 않은 것.

--------- 어제, 오늘 한 거 스스로 해보기 (과제) ---------
1) 로컬에 새로운 저장소를 생성하고
2) 파일을 3개를 추가한다. 하나 추가할 때마다 커밋한다. 
3) git hub에 리모트로 등록하고 파일을 push한다. 
4) 로컬에서 파일을 수정하고 리모트로 올리는 작업
5) 리모트에서 수정하고 로컬로 내려받는 작업을 진행한다. 