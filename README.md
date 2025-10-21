🖐️ MediaPipe 기반 비전 프로젝트 (Hand, Face Mesh, Selfie Segmentation)이 프로젝트는 Google의 MediaPipe 라이브러리를 활용하여 실시간으로 손, 얼굴 랜드마크를 감지하고, 셀카(Selfie) 배경을 분리하여 블러 처리하는 세 가지 기본 컴퓨터 비전 애플리케이션으로 구성되어 있습니다.📦 프로젝트 환경 설정프로젝트를 실행하기 위해 필요한 패키지들을 설치합니다. 가상 환경(venv) 사용을 권장합니다.1. 가상 환경 생성 및 활성화# 가상 환경 생성
python -m venv .venv

# 가상 환경 활성화 (Windows PowerShell 기준)
.\.venv\Scripts\activate
2. 의존성 설치requirements.txt 파일에 정의된 opencv-python과 mediapipe를 설치합니다.# pip 업그레이드 (선택 사항)
python -m pip install --upgrade pip

# requirements.txt 파일의 모든 패키지 설치
pip install -r requirements.txt
참고: requirements.txt 파일에는 최소한 다음 내용이 포함되어야 합니다.opencv-python
mediapipe
📁 프로젝트 파일 목록 및 설명파일 이름기능 요약사용된 MediaPipe 모듈hand_detector.py실시간으로 손 랜드마크(총 21개)를 감지하고 추적합니다.mp.solutions.handsface_detector.py실시간으로 얼굴 메쉬(Face Mesh, 468개 랜드마크)를 감지하여 촘촘한 망을 그립니다.mp.solutions.face_meshselfie_segmentation.py실시간으로 전경(인물)과 배경을 분리하고, 배경에 블러(Blur) 효과를 적용합니다.mp.solutions.selfie_segmentationhand.mp4, face.mp4테스트를 위한 비디오 파일 (필요 시)-🚀 애플리케이션 실행 방법각 스크립트를 실행하여 기능을 테스트할 수 있습니다. 각 파일 내부의 cap = cv2.VideoCapture(...) 라인을 수정하여 웹캠(0) 또는 동영상 파일을 선택할 수 있습니다.1. 손 랜드마크 감지 (hand_detector.py)손의 관절 21개에 대한 랜드마크를 추적합니다.python hand_detector.py
2. 얼굴 메쉬 감지 (face_detector.py)얼굴의 468개 랜드마크를 감지하여 얼굴 위에 정교한 메쉬(Mesh)를 그립니다.python face_detector.py
3. 셀카 배경 분리 및 블러 (selfie_segmentation.py)인물만 분리하고 배경을 부드럽게 블러 처리하여 프라이버시 보호 또는 시각 효과를 줍니다.python selfie_segmentation.py
종료 방법: 모든 애플리케이션은 화면이 활성화된 상태에서 ESC 키를 누르면 종료됩니다.