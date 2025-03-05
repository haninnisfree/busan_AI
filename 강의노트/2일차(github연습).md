### 2일차 git 연습 내용 정리

단계1) 로컬에 새로운 저장소를 생성하고 
- 먼저 저장소를 만들고자 하는 로컬 컴퓨터의 경로를 정확히 확인
- 저장소 폴더 생성
- 저장소 폴더 안에서 git init을 이용하여 초기화 작업을 진행

단계2) 파일을 3개 추가한다. 하나 추가할 때마다 커밋한다. 
- vs code에서 저장소를 폴더(워킹 디렉토리)를 열어준다. 
- 파일을 생성하고 git add. git commit -m "커밋 메시지"
- 위 작업을 3번 반복한다. 

단계3) github에 리모트로 등록하고 파일을 push한다. 
- github에서 새로운 레파지토리 생성
- 로컬 컴퓨터에 새로운 레팢지토리 등록
git remote add 리모트 이름 리모트url주소
git remote add origin https://.....
- 등록 확인
git remote -v
- 로컬 컴퓨터에서 
git push 리모트이름 브랜치명
git push origin main 

단계4) 로컬에서 파일을 수정하고 리모트로 올리는 작업
- vscode에서 파일 수정
git add .
git commit -m "commite message"
git push origin main

단계5) 리모트에서 수정핳고 로컬로 내려받는 작업을 진행한다. 
- github에서 특정 파일 수정 후 커밋
- 로컬 컴퓨터에서
git pull origin main
