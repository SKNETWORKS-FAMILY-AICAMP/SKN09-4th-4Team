# SKN09-4th-4Team

<br>

# 📌 목차

1. 팀 소개

2. 프로젝트 개요
    - 프로젝트 개요
    - 프로젝트 필요성 및 배경
    - 프로젝트 목표
    
3. 기술 스택

4. 시스템 구성도

5. 요구사항 정의서

6. 화면 설계서

7. WBS

8. 테스트 계획 및 결과 보고서
    - 테스트 계획
    - 테스트 결과

9. 수행 결과

11. 한 줄 회고

<br>

----

# 1️. 팀 소개
<div align="center">
<img src="https://github.com/user-attachments/assets/f99a4037-977f-4a75-8f63-d2a75a258332" alt="PSL_LOGO" width="200"/>
</div>

### 팀 명 : PoliSupport Lab 🧪👨‍🔬👩‍🔬


-  "보험 약관 문서 기반 챗봇 시스템” 개발 프로젝트
-  "Policy + Support + Lab"으로, 보험 약관에 대한 연구와 개발을 통해 **사용자가 자신에게 적합한 보험을 쉽게 찾을 수 있도록** 돕고, 기존에 가입한 **보험에 대한 정보도 쉽게 확인할 수 있는 시스템**을 개발하는 팀입니다.
  
<br>

### 팀 원 소개 :

<div align="center">

  |김도연|김우중|김정훈|이윤재|
|-------|-------|---------|-------|
| [@doyeon](https://github.com/doyeon158)  | [@kwj9942](https://github.com/kwj9942)  | [@Zayden](https://github.com/Zayden0815)  | [@dadambi](https://github.com/dadambi116)   |

</div>


---

# 2️. 프로젝트 개요
### 2-1) 프로젝트 개요

**보험 약관은 방대하고 어렵기 때문에**, 일반 소비자 입장에서는 중요한 **정보를 찾기 어려움**
우리 팀은 이를 해결할 수 있도록, 사용자가 **자연어로 질문**하면 **약관 내용을 바탕으로 답변을 제공**하는 시스템이 필요!

Polict_Support Chatbot을 통해 
- 사용자가 보험 상품을 쉽게 이해하고, 자신에게 적합한 보험을 찾도록 지원
- 기존 **가입된 보험의 보장 내용을 명확히 파악**할 수 있도록 지원

### 2-2) 필요성 및 배경

### **❓ 보험 미가입 사유**
![need](https://github.com/user-attachments/assets/e7b9b74d-3f95-431d-b96b-aeddfc3d4e98)
- 출처 | https://kiri.or.kr/report/downloadFile.do?docId=499489
- 각 연령별로 보험 미가입 사유에 편차가 있으나, 전체 응답 비율 중 2번째로 높은 기록으로 나타남
<br>

### **💡 보험사 챗봇 필요성 증가**
![스크린샷 2025-03-27 131355](https://github.com/user-attachments/assets/7f840f10-535c-4fe2-aceb-6047d4360b4e)
- 출처 | https://www.fntimes.com/html/view.php?ud=202402250021502382dd55077bc2_18
- 보험사 CEO, AI 활용 핵심 분야로 소비자 상담 및 고객 보장 분석에 초점
- 보험사 내 AI 도입율이 20% 미만으로 느끼고 있었지만 최대 80%까지는 도입을 추진하는 것으로 나타남

<br>

### 📑 요약
<div align="center">

|이유||챗봇 상담|
|--|:--:|:--:|
|❓ **정보 부족** :잘 모름, 이해 어려움<br>🌀  **복잡함** :상품이 너무 많고 어려움<br>📑 **약관 스트레스** :약관이 복잡하고 어려움<br>📞 **상담 불편** :전화 상담의 부담 | ➡️ |**챗봇 상담 <br> 약관 내용 바탕으로 답변 제공✅**|

</div>

<br>

### 2-3) 프로젝트 목표

**LLM 언어 모델을 활용하여 보험 약관 문서 기반으로 자연어 질의응답이 가능한 웹 챗봇 개발**


- **보장 범위 안내**: 사용자가 가입한 보험의 보장 내역을 한눈에 확인하고 이해할 수 있도록 분석 및 제공

- **보험 정보 접근성 개선**: 어려운 보험 약관을 쉽게 이해할 수 있도록 정리 및 시각화하여 사용자 경험 향상

- **맞춤형 보험 추천**: 보험에 처음 가입하려는 사용자가 자신의 니즈에 맞는 최적의 보험 상품을 찾을 수 있도록 지원
  
<br>

---



# 3️. 기술 스택 & 사용 모델
<br>

| 항목           | 내용 |
|:--------------:|------|
| **개발 도구**   | ![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?logo=visualstudiocode&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white) ![Docker Hub](https://img.shields.io/badge/Docker%20Hub-0db7ed?logo=docker&logoColor=white) |
| **개발 언어**   | ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)  ![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white) |
| **Vector DB**  | ![FAISS](https://img.shields.io/badge/FAISS-009999?logo=meta&logoColor=white) |
| **사용 모델**  | ![OpenAI GPT-4](https://img.shields.io/badge/GPT--4-00A67E?logo=openai&logoColor=white) ![Carrot LLaMA-3](https://img.shields.io/badge/LLaMA--3-FF5C8D?logo=llama&logoColor=white) ![Kanana-nano](https://img.shields.io/badge/Kanana--nano-5BCEFA?logo=huggingface&logoColor=black) ![료
![scr-04](https://github.com/user-attachments/assets/90ab803e-93e2-48c4-9a1b-060006771e44)

- "대화기록 다운로드" 클릭 시 txt파일로 대화 내용을 저장받을 수 있음.
- 피드백을 선택하면 연동된 mysql DB에 저장.
- "돌아가기" 선택 시 다시 채팅창으로 돌아감.
- "초기화" 선택 시 대화 채팅이 초기화됨.

<br>

---


# 7. WBS
![wbs-4rd-4team](https://github.com/user-attachments/assets/caf5dc52-aeec-4151-a82e-a35579e1cf9a)

**요구사항 정의 및 시스템 설계** -> **백엔드 환경 구축** -> **추론 서버 구축** -> **Django ↔ RunPod 연동** -> **사용자 페이지(UI) 테스트** -> **aws ec2 배포**

<br>

---
   
# 8. 테스트 계획 및 결과 보고서
![test-plan](https://github.com/user-attachments/assets/6cdbf6ee-6737-4854-9481-36ec53c12296)


# 9. 수행 결과 

# 10. 한줄 회고
김도연:
김우중:
김정훈:
이윤재: 



