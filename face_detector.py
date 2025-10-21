#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import mediapipe as mp

# =========================================
# 🧩 Mediapipe 초기화
# =========================================
# Face Mesh 모듈을 가져옵니다.
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_styles = mp.solutions.drawing_styles

# FaceMesh 모델 설정
# max_num_faces=1 로 설정하여 최대 1개의 얼굴을 감지합니다.
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False, 
    max_num_faces=1, 
    refine_landmarks=True,  # 랜드마크 정확도 향상 (눈, 입술 주변)
    min_detection_confidence=0.5, 
    min_tracking_confidence=0.5
)

# =========================================
# 📸 카메라 연결
# =========================================
# 기본 카메라 사용 시: cap = cv2.VideoCapture(0)
# 동영상 파일 사용 시: "face.mp4"와 같은 동영상 파일 경로를 입력하세요.
cap = cv2.VideoCapture("face.mp4") 

print("📷 카메라 스트림 시작 — ESC를 눌러 종료합니다.")

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("⚠️ 프레임을 읽지 못했습니다. 카메라 연결을 확인하거나 동영상이 끝났는지 확인하세요.")
        # 비디오 파일의 경우 루프를 종료합니다.
        # cap = cv2.VideoCapture(0) # 카메라 사용 시 무한 루프
        break

    # 좌우 반전 (선택 사항: 셀카 뷰를 위해)
    image = cv2.flip(image, 1)

    # BGR → RGB 변환 (MediaPipe는 RGB 입력을 선호)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 얼굴 검출 수행
    # 읽기 전용으로 설정하면 성능이 향상됩니다.
    image_rgb.flags.writeable = False
    result = face_mesh.process(image_rgb)
    image_rgb.flags.writeable = True

    # RGB → BGR로 다시 변환하여 OpenCV로 표시
    image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

    # 🧑‍💻 얼굴 랜드마크 표시
    if result.multi_face_landmarks:
        # 감지된 모든 얼굴 랜드마크에 대해 반복
        for face_landmarks in result.multi_face_landmarks:
            # 랜드마크를 이미지 위에 그립니다.
            mp_drawing.draw_landmarks(
                image=image,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_TESSELATION, # 얼굴 표면 메쉬 연결
                # 랜드마크 스타일: 작은 점 스타일
                landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1),
                # 연결선 스타일: 얇고 흐린 선
                connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 100, 0), thickness=1, circle_radius=1)
            )

    # 화면 표시
    cv2.imshow('🧑‍💻 MediaPipe Face Mesh Detector', image)

    # ESC 키 (ASCII 27)를 눌러 종료
    if cv2.waitKey(5) & 0xFF == 27:
        print("👋 종료합니다.")
        break

# =========================================
# 🔚 종료 처리
# =========================================
cap.release()
cv2.destroyAllWindows()
