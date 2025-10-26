---
title: HaroFramework SPEC 인덱스
version: 3.0.0
scope: framework
created: 2025-10-26
modified: 2025-10-26
category: Specification
tags: [spec, index, architecture, documentation]
paired_document: README.md
parent_documents:
  - ../index_KOR.md
child_documents:
  - ./01-vision/overview_KOR.md
  - ./02-architecture/6-layer-system_KOR.md
  - ./03-documentation-system/bilingual-rules_KOR.md
  - ./04-scope-dependency/rules_KOR.md
  - ./05-core-systems/README_KOR.md
  - ./06-quality/code-quality_KOR.md
  - ./07-tech-stack/unity-environment_KOR.md
  - ./08-workflow/development-process_KOR.md
  - ./09-success-criteria/framework-goals_KOR.md
  - ./10-future/planned-features_KOR.md
references: []
status: active
---


<!-- Navigation -->
**🏠 [HaroFramework Project](../../../MASTER_INDEX_KOR.md)** | **📂 [HaroFramework SPEC 인덱스](README_KOR.md)** | **⬆️ [HaroFramework 프로젝트 인덱스](../index_KOR.md)**

---
# HaroFramework SPEC 인덱스

10개 주요 섹션으로 구성된 완전한 프로젝트 명세 및 아키텍처 문서입니다.

**총 SPEC 파일 수**: 62개 (영어 31개 + 한국어 31개)

---

## 📑 목차

### [01. 프로젝트 비전](./01-vision/overview_KOR.md)
**무엇을 왜 만드는가**

- [개요](./01-vision/overview_KOR.md) - 프로젝트 목적 및 대상 사용 사례
- [목표](./01-vision/goals_KOR.md) - 재사용성, 확장성, 품질, 성능

**핵심 개념**: 게임 프레임워크 기반, 다중 장르 지원, 개발자 경험

---

### [02. 아키텍처](./02-architecture/6-layer-system_KOR.md)
**시스템 구조**

- [2-스코프 요약](./02-architecture/2-scope-summary_KOR.md) - Framework vs Game 스코프 분리
- [6계층 시스템](./02-architecture/6-layer-system_KOR.md) - 완전한 계층 아키텍처
  - Data, Domain, Core, Interface, Service, Gameplay
- [폴더 구조](./02-architecture/folder-structure_KOR.md) - 프로젝트 조직화
- [네이밍 규칙](./02-architecture/naming-conventions_KOR.md) - 일관된 명명 규칙

**핵심 개념**: 2-스코프 시스템, 6계층 아키텍처, 의존성 흐름, 통신 패턴

---

### [03. 문서 시스템](./03-documentation-system/bilingual-rules_KOR.md)
**프로젝트 문서화 방법**

- [이중언어 규칙](./03-documentation-system/bilingual-rules_KOR.md) - 영어/한국어 문서
- [메타데이터 표준](./03-documentation-system/metadata-standard_KOR.md) - YAML frontmatter
- [버전 관리](./03-documentation-system/version-management_KOR.md) - 시맨틱 버저닝
- [워크플로우 규칙](./03-documentation-system/workflow-rules_KOR.md) - 문서화 프로세스
- [자동화 스크립트](./03-documentation-system/automation-scripts_KOR.md) - 검증 도구

**핵심 개념**: 이중언어 문서, 모듈형 구조, 메타데이터, 자동화

---

### [04. 스코프 의존성 규칙](./04-scope-dependency/rules_KOR.md)
**중요한 아키텍처 제약**

- [규칙](./04-scope-dependency/rules_KOR.md) - Framework ❌ Game, Game ✅ Framework
- [검증](./04-scope-dependency/validation_KOR.md) - 자동화된 강제
- [예제](./04-scope-dependency/examples_KOR.md) - 좋은 패턴과 나쁜 패턴

**핵심 개념**: 스코프 격리, 재사용성 강제, 검증 스크립트

---

### [05. 핵심 시스템](./05-core-systems/README_KOR.md) ⭐
**모든 프레임워크 시스템의 상세 명세**

#### [핵심 기반](./05-core-systems/foundation/singleton_KOR.md)
프레임워크의 기반을 형성하는 14개 기초 클래스:

**기반 (3개)**:
- [Singleton](./05-core-systems/foundation/singleton_KOR.md) - 스레드 안전 싱글톤 패턴
- [IModule](./05-core-systems/foundation/imodule_KOR.md) - 모듈 인터페이스
- [IService](./05-core-systems/foundation/iservice_KOR.md) - 서비스 인터페이스

**핵심 시스템 (4개)**:
- [EventBus](./05-core-systems/foundation/eventbus_KOR.md) - 이벤트 기반 통신
- [ServiceLocator](./05-core-systems/foundation/service-locator_KOR.md) - 서비스 관리
- [DataManager](./05-core-systems/foundation/data-manager_KOR.md) - 도메인 관리
- [FrameworkLogger](./05-core-systems/foundation/framework-logger_KOR.md) - 로깅 시스템

**기본 클래스 (5개)**:
- [BaseData](./05-core-systems/foundation/base-data_KOR.md) - Data 계층 기반
- [BaseDomain](./05-core-systems/foundation/base-domain_KOR.md) - Domain 계층 기반
- [BaseModule](./05-core-systems/foundation/base-module_KOR.md) - Module 계층 기반
- [BaseService](./05-core-systems/foundation/base-service_KOR.md) - Service 계층 기반
- [BaseGameplay](./05-core-systems/foundation/base-gameplay_KOR.md) - Gameplay 계층 기반

**프레임워크 관리자 (2개)**:
- [FrameworkConfig](./05-core-systems/foundation/framework-config_KOR.md) - 설정
- [FrameworkManager](./05-core-systems/foundation/framework-manager_KOR.md) - 초기화 관리자

#### [핵심 모듈](./05-core-systems/modules/) (Phase 2)
구현 예정: UIModule, AudioModule, SceneModule, NetworkModule

#### [생명주기 관리](./05-core-systems/lifecycle_KOR.md)
초기화 및 종료 시퀀스

**핵심 개념**: 핵심 기반, 6계층 기반, 생명주기, 이벤트 기반, 서비스 지향

---

### [06. 품질 표준](./06-quality/code-quality_KOR.md)
**이 프로젝트의 품질 의미**

- [코드 품질](./06-quality/code-quality_KOR.md) - 문서화, 테스트, 표준
- [문서 품질](./06-quality/documentation-quality_KOR.md) - 완전성, 정확성
- [검증](./06-quality/validation_KOR.md) - 자동화된 품질 게이트

**핵심 개념**: >80% 테스트 커버리지, XML 문서, 검증 스크립트, 코딩 규칙

---

### [07. 기술 스택](./07-tech-stack/unity-environment_KOR.md)
**사용하는 기술 및 도구**

- [Unity 환경](./07-tech-stack/unity-environment_KOR.md) - Unity 6, URP, Input System
- [개발 도구](./07-tech-stack/development-tools_KOR.md) - IDE, Git, 문서화
- [의존성](./07-tech-stack/dependencies_KOR.md) - 패키지 관리

**핵심 개념**: Unity 6, URP 17.2.0, New Input System, 최소 의존성

---

### [08. 개발 워크플로우](./08-workflow/development-process_KOR.md)
**기능 개발 방법**

- [개발 프로세스](./08-workflow/development-process_KOR.md) - 8단계 프로세스
- [문서화 워크플로우](./08-workflow/documentation-workflow_KOR.md) - 문서 작성 프로세스
- [세션 관리](./08-workflow/session-management_KOR.md) - 컨텍스트 관리 (85% 규칙)

**핵심 개념**: 계획 → 설계 → 구현 → 테스트 → 문서화 → 검토 → 통합 → 검증

---

### [09. 성공 기준](./09-success-criteria/framework-goals_KOR.md)
**성공 측정 방법**

- [프레임워크 목표](./09-success-criteria/framework-goals_KOR.md) - 핵심 시스템, 테스트, 문서
- [문서화 목표](./09-success-criteria/documentation-goals_KOR.md) - 이중언어, 검증됨
- [품질 목표](./09-success-criteria/quality-goals_KOR.md) - 경고 없음, 테스트 통과

**핵심 개념**: 측정 가능한 목표, 완료 기준, 품질 게이트

---

### [10. 향후 계획](./10-future/planned-features_KOR.md)
**다음 단계**

- [계획된 기능](./10-future/planned-features_KOR.md) - 멀티플레이어, AI, 절차적 생성
- [문서 진화](./10-future/documentation-evolution_KOR.md) - 자동 생성, 인터랙티브
- [도구 개선](./10-future/tooling-improvements_KOR.md) - CI/CD, 번역, 웹사이트

**핵심 개념**: 로드맵, 확장성, 커뮤니티

---

## 🔍 탐색 방법

### 처음 읽는 분들을 위한
**권장 읽기 순서:**
1. [01. 프로젝트 비전](./01-vision/overview_KOR.md) - "왜"를 이해하기
2. [02. 아키텍처 - 6계층 시스템](./02-architecture/6-layer-system_KOR.md) - 구조 이해하기
3. [05. 핵심 시스템 - 기반](./05-core-systems/foundation/singleton_KOR.md) - 구현 세부 사항 보기
4. [06. 품질 표준](./06-quality/code-quality_KOR.md) - 품질 요구사항 학습

### 개발자용
**빠른 참조:**
- 아키텍처 → [6계층 시스템](./02-architecture/6-layer-system_KOR.md)
- 구현 → [핵심 기반](./05-core-systems/foundation/singleton_KOR.md)
- 표준 → [품질](./06-quality/code-quality_KOR.md)
- 워크플로우 → [개발 프로세스](./08-workflow/development-process_KOR.md)

### 문서 작성자용
**필수 읽기:**
- [이중언어 규칙](./03-documentation-system/bilingual-rules_KOR.md)
- [메타데이터 표준](./03-documentation-system/metadata-standard_KOR.md)
- [워크플로우 규칙](./03-documentation-system/workflow-rules_KOR.md)

---

## 📊 SPEC 통계

### 섹션별 파일 수

| 섹션 | 파일 수 | 주제 |
|---------|-------|--------|
| 01. 비전 | 2 | 개요, 목표 |
| 02. 아키텍처 | 4 | 스코프, 계층, 구조, 네이밍 |
| 03. 문서화 | 5 | 규칙, 메타데이터, 버저닝, 워크플로우, 스크립트 |
| 04. 스코프 의존성 | 3 | 규칙, 검증, 예제 |
| 05. 핵심 시스템 | 16 | 14개 클래스 + 생명주기 + 인덱스 |
| 06. 품질 | 3 | 코드, 문서, 검증 |
| 07. 기술 스택 | 3 | Unity, 도구, 의존성 |
| 08. 워크플로우 | 3 | 개발, 문서, 세션 |
| 09. 성공 | 3 | 프레임워크, 문서, 품질 |
| 10. 향후 | 3 | 기능, 문서, 도구 |

**총계**: 45개 문서 (영어), 45개 번역 (한국어), 2개 인덱스 = **92개 SPEC 파일**

### 핵심 지표
- **가장 깊은 섹션**: 핵심 시스템 (14개 클래스 명세)
- **가장 중요한**: 아키텍처 (6계층 시스템, 스코프 규칙)
- **가장 많이 참조됨**: 핵심 기반 (모든 Phase 1 태스크가 링크)

---

## 🔗 관련 문서

### 내부 링크
- [프로젝트 인덱스로 돌아가기](../index_KOR.md)
- [TODO 인덱스](../todo/README_KOR.md)
- [진행 상황 대시보드](../todo/PROGRESS_KOR.md)

### 외부 리소스
- [코딩 규칙](../../doc/guidelines/coding-conventions_KOR.md)
- [개발 워크플로우](../../doc/workflow/development-workflow_KOR.md)
- [스코프 시스템 가이드](../../doc/architecture/scope-system_KOR.md)

### 도구
- [스코프 검증 스크립트](../../../scripts/scope_validate.py)
- [문서 검증 스크립트](../../../scripts/doc_validate.py)

---

## 📝 문서 유지보수

### 버전 관리
각 SPEC 문서는 시맨틱 버저닝을 따르는 독립적인 버전 관리를 합니다:
- **MAJOR**: 명세의 주요 변경사항
- **MINOR**: 새 섹션 또는 중요한 추가사항
- **PATCH**: 명확화, 오타, 예제

### 업데이트 워크플로우
1. 영어 문서 업데이트
2. 메타데이터의 `modified` 날짜 업데이트
3. 적절하게 버전 증가
4. 한국어 번역 업데이트
5. `doc_validate.py` 실행
6. 변경사항 커밋

### 품질 체크리스트
- [ ] 메타데이터 완전하고 정확함
- [ ] 한국어 번역 동기화됨
- [ ] 상호 참조 유효함
- [ ] 예제 테스트되고 작동함
- [ ] 검증 스크립트 통과함

---

**문서 상태**: Active
**관리자**: HaroFramework Team
**마지막 업데이트**: 2025-10-26
**다음 검토**: Phase 1 완료 후
