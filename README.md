# SKN09-4th-4Team

<br>

# 📌 목차

1. 팀 소개

2. 프로젝트 개요
    - 프로젝트 개요
    - 프로젝트 필요성 및 배경
    - 프로젝트 목표
    
3. WBS

4. 기술 스택

5. 시스템 구성도

6. 요구사항 정의서

7. 화면 설계서

8. 테스트 계획 및 결과 보고서
    - 테스트 계획
    - 테스트 결과

9. 수행 결과

10. 한 줄 회고

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


# 3. WBS
![wbs-4rd-4team](https://github.com/user-attachments/assets/caf5dc52-aeec-4151-a82e-a35579e1cf9a)

**요구사항 정의 및 시스템 설계** -> **백엔드 환경 구축** -> **추론 서버 구축** -> **Django ↔ RunPod 연동** -> **사용자 페이지(UI) 테스트** -> **aws ec2 배포**

<br>

---



# 4. 기술 스택 & 사용 모델
<br>

| 항목           | 내용 |
|:--------------:|------|
| **개발 도구**   | ![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?logo=visualstudiocode&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white) ![Docker Hub](https://img.shields.io/badge/Docker%20Hub-0db7ed?logo=docker&logoColor=white) |
| **개발 언어**   | ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)  ![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white) |
| **Vector DB**  | ![FAISS](https://img.shields.io/badge/FAISS-009999?logo=meta&logoColor=white) |
| **사용 모델**  | ![OpenAI GPT-4](https://img.shields.io/badge/GPT--4-00A67E?logo=openai&logoColor=white) ![Carrot LLaMA-3](https://img.shields.io/badge/LLaMA--3-FF5C8D?logo=llama&logoColor=white) ![Kanana-nano](https://img.shields.io/badge/Kanana--nano-5BCEFA?logo=huggingface&logoColor=black) ![LangChain](https://img.shields.io/badge/LangChain-FF9900?logo=Chainlink&logoColor=white) |
| **서버**       | ![AWS EC2](https://img.shields.io/badge/AWS%20EC2-232F3E?logo=amazonaws&logoColor=white) ![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white) ![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?logo=gunicorn&logoColor=white) ![Nginx](https://img.shields.io/badge/Nginx-009639?logo=nginx&logoColor=white) |
| **추론 서버**  | ![RunPod](https://img.shields.io/badge/RunPod-5F43DC?logo=cloud&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white) |
| **데이터베이스** | ![MySQL](https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=white) |
| **협업 도구**   | ![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white) ![Notion](https://img.shields.io/badge/Notion-000000?logo=notion&logoColor=white) |


<br>

---



# 5. 시스템 구성도

![system_arch](https://github.com/user-attachments/assets/20286f65-4a61-4413-ab53-507e4e73c34b)




<br>

---



# 6. 요구사항 정의서

![requirement](https://github.com/user-attachments/assets/ab4dea56-7786-402b-be86-834fad3c2b00)


✅ **1. 챗봇 질의응답 기능**

- 사용자는 보험 약관 관련 질문을 자유롭게 입력하고, 보험 약관 문서를 기반으로 답변을 제공.
 
✅ **2. 피드백 제출 기능**

- 사용자는 대화를 종료 후에 챗봇 시스템에 대해 (좋아요&보통&싫어요)으로 피드백을 남길 수 있음.
- 이 피드백 데이터를 수집하여 향후 성능향상을 위한 목적으로 모델 학습에 사용될 수 있음.

✅ **3. 대화 기록 다운로드 기능**

- 사용자는 챗봇 대화 내용을 다운로드 받을 수 있음.
- 이를 통해 상담 이력을 보관하거나 필요한 내용을 다시 확인할 수 있음.

<br>

---


# 7. 화면설계서

<br>

### 01. 첫 페이지
![scr-01](https://github.com/user-attachments/assets/d9a1d652-eaa2-4069-b13b-a789b88239dc)



<br>

### 02. 채팅 페이지
![src-02](https://github.com/user-attachments/assets/28943c03-71cc-4712-aaaa-9d46cfada46b)


<br>

![scr-03](https://github.com/user-attachments/assets/054bc2af-e202-49fc-857a-6cdff9d62904)


<br>

### 03. 피드백 및 종료
![scr-04](https://github.com/user-attachments/assets/d073337f-1263-4765-866e-ec2f7bc5f4ee)



<br>


---
   
# 8. 테스트 계획 및 결과 보고서
### 1. 테스트 계획
![test-plan](https://github.com/user-attachments/assets/6cdbf6ee-6737-4854-9481-36ec53c12296)


### 2. 테스트 결과 보고서

**테스트 결과 1**
![image111](https://github.com/user-attachments/assets/5adb6527-f201-4c22-9288-5dd61df8a67d)



**테스트 결과 2**
![IMAGE222](https://github.com/user-attachments/assets/b815dc6b-7aad-44f0-b8cd-29f8d37df26d)

![스크린샷 2025-04-22 134343](https://github.com/user-attachments/assets/92fc0244-a466-454e-a3e5-c0a45ca517ac)


**테스트 결과 3**
![image333](https://github.com/user-attachments/assets/6515cee4-3171-44b1-b32f-c3fa6e62eb2d)


<img src="https://github.com/user-attachments/assets/63f03e2e-e3e1-4245-908f-40ccb7cd7435" alt="2025-04-22_144050" width="500"/>


---

# 9. 수행 결과 
![스크린샷 2025-04-22 145856](https://github.com/user-attachments/assets/34aa0f7f-2589-4625-adad-215e76081fc6)


![스크린샷 2025-04-22 145920](https://github.com/user-attachments/assets/4c9f3498-00bb-416a-93aa-af5fc027aece)



---


# 10 발전 방향
📌 **도입 모델: 3B 사이즈 언어모델**
<br>
	도입 이유: 로컬 환경에서의 응답 속도 최적화
 <br>
	적용 분야: 보험 상담 챗봇

🚧 **확인된 개선할 사항**
<br>
추론 능력 부족
<br>
보험 상품 간 비교
<br>
세부 보장 내용에 대한 정확한 이해 부족
<br>
질문 처리 성능 저하
<br>
일반적인 질문에 대한 응답 정확도 낮음
<br>
맥락이 모호한 질의 처리 미흡
<br>

🧠 **결론 및 제안**
<br>
복잡한 질의 대응을 위해 7B 이상 모델 도입 필요
<br>
특히, 사용자 맞춤형 추천 기능 강화를 위해
<br>
→ 고성능 모델 기반의 추론 기능 필수

---

# 11. 한줄 회고

- 김도연: 기본적인 Django 파일 구조에 따라 설계를 진행했지만, 사용자별 대화 데이터를 저장하는 기능이 필요해지면서, 기존 로직에 사용자 식별용 user id 생성 함수와 관련 클래스를 새롭게 설계하게 되었습니다. 기능이 추가되면서 발생할 수 있는 구조적 복잡성과, 처음부터 구조적인 설계가 왜 중요한지 체감할 수 있었습니다.
<br>
- 김우중: Docker와 FastAPI를 연동하는 과정에서 프록시 포트와 실행 환경 설정에 어려움을 겪었지만, 시행착오를 통해 서버 실행 구조를 이해하는 경험을 얻었습니다. 
<br>
- 김정훈: AWS와 Docker를 통해 클라우드 환경에서의 자동화된 배포와 운영의 핵심 흐름을 직접 체감할 수 있었다.
<br>
- 이윤재: 처음에는 약관을 제대로 불러들여와서 사용자가 이해하기 쉽게 텍스트를 생성하는 데에 초점을 맞췄는데, 질문에 대한 답변만 잘 하는 것이 아니라 이후에 사용자가 어떤 정보를 원할지 추론해서 그에 대한 정보를 먼저 질문하거나 함께 답변해주는 추론 기능 역시 중요하다는 것을 깨달았습니다. 




