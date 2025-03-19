수정해야 됨
예시1)
영화 예매 사이트

*기간 : 2025.02~

*설명 : 영화 예매 서비스를 제공하며 메인 페이지와 관리자 페이지로 구성됩니다.
영화진흥위원회(Kobis)와 KMDB API를 통해 최신 영화 데이터를 수집해 데이터베이스에 저장합니다.
관리자 페이지에서는 영화관리에 이어 회원 관리, 상영 관리, 결제 관리 기능을 제공할 예정입니다.

*사용언어 및 기술스택 :

Backend : Java (Spring MVC), MyBatis, HikariCP
Frontend : React.js, JavaScript, HTML, CSS
Database : Oracle
Tools : Spring Tool Suite 3, Visual Studio Code, GitHub, Notion
API : Kobis·KMDB API를 통한 데이터 수집 및 DB 저장
*주요 기능

영화 API(Kobis·KMDB)를 통해 영화 데이터를 수집 및 DB 저장
기존 데이터는 업데이트, 신규 데이터는 추가되도록 트랜잭션 처리 적용
관리자 페이지를 통해 회원, 상영, 결제 관리 기능 제공 예정
*팀원 :

소담, 성호, 영민, 호영, 창우
*담당 역할 (관리자 페이지 담당)

플로우차트 작성 : 관리자 페이지의 흐름 정의 및 추후 수정 예정
기본 코드 작성 : DTO, mapper.xml, mapper, service, serviceimpl, controller 작성 (호영님과 협업)
API 데이터 수집 : Kobis·KMDB API를 통해 영화 데이터를 가져와 데이터베이스에 저장
트랜잭션 처리 : 기존 데이터는 업데이트, 신규 데이터는 추가되도록 트랜잭션 어노테이션 적용
코드 리팩토링 : 유지보수와 가독성을 위해 serviceimpl과 movieutils로 기능 분리
앞으로의 계획 : 회원 관리, 상영 관리, 결제 관리 기능 구현 및 React.js를 통한 프론트엔드 개발 담당

예시2)
🐧 핑크펭귄(Pink-Penguin)
자세 추정 모델을 활용한 유아 대상의 동작 인식 교육서비스.




📚 프로젝트 설명
COVID19로 인하여 실내에 머무는 시간이 증가함에 따라 감소하는 신체 활동을 보완하기 위해 기획되었으며,
어린이들을 위한 서비스로 초점을 두어 음악과 함께 캐릭터들의 간단한 동작들을 따라하며 진행하는 방식.




📝 사용언어, 기술스택
Model : Tensorflow.js(2.0), ML5(0.6.0)
Platform : Web
Language : Javascript
Framework : Vue.js(2.6.11), Express.js(4.17.1)
Database : MariaDB(3.6.3)
Environment: Docker(4.3.1), Docker-compose(1.27.4), AWS EC2(CentOS8)



🔨 주요 개발 내용
오픈소스를 활용한 포즈 인식(Posenet)
딥러닝 모델을 통한 자세 추정(tensorflow.js, ML5)
3D애니메이션 로딩(three.js, VRM)
다국어 지원(i18n/ko,en,jp)
ORM(npm sequelize)
서버 배포(docker, AWS)



💻 최종 실행 화면
                      캐릭터선택
                      게임하기 display




🚀 설치 및 실행
1. 기본 환경에서의 실행
git clone https://github.com/won-js/project_AI.git

Build a vue project

npm install 
npm run serve
Build an express project

npm install
npm start
Run the server
http://localhost/8081

2. Docker 환경에서의 실행
docker-compose build
docker-compose start-d
Run the server
http://localhost/80




🏃 팀원 소개
😃 원준수(팀장) : 딥러닝 모델 구현, Docker 설정, 3D 애니메이션 구현
😉 유재혁(Frontend) : 프론트 구현, UI/UX디자인, 데이터 수집
😄 김수양(Frontend) : 시장분석, UI/UX설계, 문서 작업
😆김동주(Backend) : 로그인/회원가입 기능 구현, AWS 설정, 데이터 가공
😳 유정호(Backend) : 커뮤니티 기능 구현, DB모델링, 다국어 지원
