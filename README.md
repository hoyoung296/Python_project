학생 관리 프로그램 (Student Management Program)
<br>
📅 기간 : 2025.02
<br>
📌 설명

학생의 인적 사항을 등록, 검색, 수정, 삭제할 수 있는 학생 관리 프로그램입니다.

데이터베이스를 사용하지 않고, Python의 딕셔너리를 활용하여 학생 정보를 관리합니다.

사용자는 학번을 기준으로 학생을 조회하고, 필요한 정보를 수정하거나 삭제할 수 있습니다.
<br>
🛠 사용 기술 및 스택

Backend : Python

Database : 없음 (딕셔너리 활용)

Tools : Visual Studio Code, GitHub
<br>
✨ 주요 기능

✅ 학생 정보 등록 (학번, 이름, 생년월일, 학년)

✅ 학번을 이용한 학생 검색 기능

✅ 학생 정보 수정 (이름, 생년월일, 학년 변경)

✅ 특정 학생 삭제 및 전체 학생 목록 삭제 기능

✅ 등록된 모든 학생 목록 출력 기능
<br>
🛠 구현 상세

프로그램 구조 설계 : 학생 정보를 객체로 관리하는 student 클래스 정의

기능 구현 : 학생 정보 등록, 검색, 수정, 삭제 기능 함수별 구현

데이터 저장 방식 : 딕셔너리를 활용하여 학생 정보 저장 및 관리

유효성 검사 : 올바른 학년 입력, 존재하는 학번 확인 등의 검증 로직 적용
<br>
🚀 앞으로의 계획

데이터베이스(MySQL 또는 SQLite)를 연동하여 영구 저장 기능 추가

GUI 환경 구축을 통한 사용자 편의성 개선 (Tkinter 또는 PyQt 활용)

웹 기반 학생 관리 시스템으로 확장 (Flask 또는 Django 활용)
