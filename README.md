### 🚀 MediaPipe 비전 인식 프로젝트 개요
이 프로젝트는 Google의 MediaPipe 라이브러리를 활용하여 실시간으로 인체를 인식하는 세 가지 기본 컴퓨터 비전 애플리케이션 모음입니다. 각 스크립트는 웹캠 또는 동영상 파일을 입력으로 받아 동작합니다.

### ⚙️ 환경 설정 및 의존성 설치
프로젝트를 실행하려면 Python 환경에 opencv-python과 mediapipe 패키지가 설치되어 있어야 합니다

1. 가상 환경 활성화Windows PowerShell에서 가상 환경을 활성화합니다.PowerShell.\.venv\Scripts\activate
2. 필요한 패키지 설치requirements.txt에 명시된 모든 의존성을 설치합니다.Bashpip install -r requirements.txt

### 📄 애플리케이션 목록 및 기능
프로젝트는 다음 세 가지 주요 스크립트로 구성되어 있습니다.파일 이름주요 기능사용 MediaPipe 모듈hand_detector.py실시간 손 랜드마크 (21개) 감지 및 추적mp.solutions.handsface_detector.py실시간 얼굴 메쉬 (468개 랜드마크) 감지 및 시각화mp.solutions.face_meshselfie_segmentation.py인물 전경/배경 분리 및 배경 블러(Blur) 처리mp.solutions.selfie_segmentation
### ▶️ 프로그램 실행 
방법가상 환경이 활성화된 상태에서 각 스크립트를 실행합니다.Bash# 예시: 손 감지 프로그램 실행
python hand_detector.py

### 💡 종료 
안내프로그램 실행 중 화면이 표시되면 ESC 키를 눌러 언제든지 종료할 수 있습니다.