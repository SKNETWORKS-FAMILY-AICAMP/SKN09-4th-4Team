# SKN09-4th-4Team

### - LLM을 연동한 내외부 문서 기반 질의 응답 시스템
![PSL_LOGO](https://github.com/user-attachments/assets/f99a4037-977f-4a75-8f63-d2a75a258332)


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
### 팀 명 : PoliSupport Lab 🧪👨‍🔬👩‍🔬
-  "Policy + Support + Lab"으로, 보험 약관에 대한 연구와 개발을 통해 **사용자가 자신에게 적합한 보험을 쉽게 찾을 수 있도록** 돕고, 기존에 가입한 **보험에 대한 정보도 쉽게 확인할 수 있는 시스템**을 개발하는 팀입니다.
  
<br>

### 팀 원 소개 :

<dir alige="center">

  |김도연|김우중|김정훈|이윤재|
|-------|-------|---------|-------|
| [@doyeon](https://github.com/doyeon158)  | [@kwj9942](https://github.com/kwj9942)  | [@Zayden](https://github.com/Zayden0815)  | [@dadambi](https://github.com/dadambi116)   |
</dir>

<br>

---

# 2️. 프로젝트 개요
### 2-1) 프로젝트 개요

Polict_Support Chatbot을 통해 
- 사용자가 보험 상품을 쉽게 이해하고, 자신에게 적합한 보험을 찾도록 지원
- 기존 **가입된 보험의 보장 내용을 명확히 파악**할 수 있도록 지원

### 2-2) 필요성 및 배경

### **❓ 보험 미가입 사유**
![image](https://github.com/user-attachments/assets/651b2cc0-423a-4dbc-8232-1b6e921bc73a)
- 출처 | https://kiri.or.kr/report/downloadFile.do?docId=499489
- 각 연령별로 보험 미가입 사유에 편차가 있으나, 20대 이하의 경우 '보상범위 등 상품을 잘 몰라서'로 응답
<br>

### **💡 보험사 챗봇 필요성 증가**
![스크린샷 2025-03-27 131355](https://github.com/user-attachments/assets/7f840f10-535c-4fe2-aceb-6047d4360b4e)
- 출처 | https://www.fntimes.com/html/view.php?ud=202402250021502382dd55077bc2_18
- 보험사 CEO, AI 활용 핵심 분야로 소비자 상담 및 고객 보장 분석에 초점
- 보험사 내 AI 도입율이 20% 미만으로 느끼고 있었지만 최대 80%까지는 도입을 추진하는 것으로 나타남

<br>

### 📑 요약

|이유||챗봇 상담|
|--|:--:|:--:|
|💸  **비용 부담** :보험료 부담, 경제적 이유<br>❓ **정보 부족** :잘 모름, 이해 어려움<br>🌀  **복잡함** :상품이 너무 많고 어려움<br>🤷 **관심 부족** :아직 필요성을 못 느낌<br>🕒 **시간 부족** :상담받을 시간 없음<br>📑 **약관 스트레스** :약관이 복잡하고 어려움<br>📞 **상담 불편** :전화 상담의 부담 | ➡️ |**챗봇 상담 <br> 빠르고 간편한 해결✅**|

<br>

### 2-3) 프로젝트 목표

이 프로젝트의 주요 목표는 **사용자 친화적인 보험 정보 서비스를 제공하는 것**입니다.

- **보장 범위 안내**: 사용자가 가입한 보험의 보장 내역을 한눈에 확인하고 이해할 수 있도록 분석 및 제공

- **보험 정보 접근성 개선**: 어려운 보험 약관을 쉽게 이해할 수 있도록 정리 및 시각화하여 사용자 경험 향상

- **맞춤형 보험 추천**: 보험에 처음 가입하려는 사용자가 자신의 니즈에 맞는 최적의 보험 상품을 찾을 수 있도록 지원
  
<br>

---



# 3️. 기술 스택 & 사용 모델
<br>

|항목|내용|
|:---:|---|
|개발 도구| ![VS Code](https://img.shields.io/badge/-VS%20Code-007ACC?logo=visualstudiocode&logoColor=white) ![RunPod](https://img.shields.io/badge/-RunPod-5F43DC?logo=cloud&logoColor=white) |
|개발 언어| ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)|
|Vector DB|![FAISS](https://img.shields.io/badge/-FAISS-009999?logo=meta&logoColor=white)|
|사용 모델| ![OpenAI-GPT4](https://img.shields.io/badge/GPT--4o-00A67E?style=flat&logo=openai&logoColor=white) ![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20HF_transformer%20-yellow) ![Langchain](https://img.shields.io/badge/LangChain-FF9900?style=flat&logo=Chainlink&logoColor=white)|
|인터페이스| ![streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white) |


<br>

---



# 4️. 시스템 아키텍처



<br>

---



# 5️. 요구사항 정의서


<br>

---


# 6. 화면설계서

# 7. WBS

# 8. 테스트 계획 및 결과 보고서

# 9. 수행 결과 

# 10. 한줄 회고


