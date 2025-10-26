---
title: HaroFramework 프로젝트 인덱스
version: 3.0.0
scope: framework
created: 2025-10-26
modified: 2025-10-26
category: Project Management
tags: [index, navigation, master-index]
paired_document: index.md
parent_documents: []
child_documents:
  - ./spec/README_KOR.md
  - ./todo/README_KOR.md
references: []
status: active
---


<!-- Navigation -->
**🏠 [HaroFramework Project](../../MASTER_INDEX_KOR.md)** | **📂 [HaroFramework 프로젝트 인덱스](INDEX_KOR.md)** | **⬆️ [HaroFramework 프로젝트 인덱스](INDEX_KOR.md)**

---
# HaroFramework 프로젝트 인덱스

HaroFramework 프로젝트 문서에 오신 것을 환영합니다. 이 문서는 모든 프로젝트 문서를 탐색하기 위한 마스터 인덱스입니다.

## 📋 문서 구조

### SPEC (명세서)
**완전한 프로젝트 명세 및 아키텍처 문서**

👉 **[SPEC 인덱스로 이동](./spec/README_KOR.md)**

주요 섹션 바로가기:
- [01. 프로젝트 비전](./spec/01-vision/overview_KOR.md) - 프로젝트 목표 및 방향
- [02. 아키텍처](./spec/02-architecture/6-layer-system_KOR.md) - 6계층 시스템 아키텍처
- [03. 문서 시스템](./spec/03-documentation-system/bilingual-rules_KOR.md) - 문서화 표준
- [04. 스코프 의존성 규칙](./spec/04-scope-dependency/rules_KOR.md) - Framework/Game 스코프 규칙
- [05. 핵심 시스템](./spec/05-core-systems/README_KOR.md) - 핵심 기반 및 모듈
  - [기반 상세](./spec/05-core-systems/foundation/singleton_KOR.md) - 14개 핵심 클래스
- [06. 품질 표준](./spec/06-quality/code-quality_KOR.md) - 코드 및 문서 품질
- [07. 기술 스택](./spec/07-tech-stack/unity-environment_KOR.md) - Unity 6, URP, 도구
- [08. 개발 워크플로우](./spec/08-workflow/development-process_KOR.md) - 개발 프로세스
- [09. 성공 기준](./spec/09-success-criteria/framework-goals_KOR.md) - 프로젝트 목표
- [10. 향후 계획](./spec/10-future/planned-features_KOR.md) - 로드맵

### TODO (태스크 추적)
**태스크 관리 및 진행 상황 추적**

👉 **[TODO 인덱스로 이동](./todo/README_KOR.md)**

👉 **[진행 상황 대시보드 보기](./todo/PROGRESS_KOR.md)**

#### 현재 단계
**Phase 1: 핵심 기반** - 상태: PENDING (0/14 완료)

다음 태스크: [CF-001: Singleton.cs](./todo/phase1-core-foundation/phase-a-foundation/CF-001-singleton_KOR.md)

#### 모든 단계
- [✅ 완료된 태스크](./todo/completed/) - 문서 설정, 자동화 스크립트
- [🔵 Phase 1: 핵심 기반](./todo/phase1-core-foundation/README_KOR.md) - 14개 태스크 (0-4주)
- [⏳ Phase 2: 핵심 모듈](./todo/phase2-core-modules/README_KOR.md) - 상세 예정
- [⏳ Phase 3: 예제 구현](./todo/phase3-example/README_KOR.md) - 상세 예정
- [⏳ Phase 4: 문서화 및 테스트](./todo/phase4-documentation/README_KOR.md) - 상세 예정

---

## 🔗 빠른 탐색

### 개발자용

**개발 시작하시나요?**
1. [프로젝트 비전](./spec/01-vision/overview_KOR.md) 읽기
2. [6계층 아키텍처](./spec/02-architecture/6-layer-system_KOR.md) 이해하기
3. [코딩 규칙](../doc/guidelines/coding-conventions_KOR.md) 따르기
4. [개발 워크플로우](./spec/08-workflow/development-process_KOR.md) 확인하기

**핵심 기반 작업 중이신가요?**
1. [진행 상황 대시보드](./todo/PROGRESS_KOR.md) 확인
2. [Phase 1](./todo/phase1-core-foundation/README_KOR.md)에서 작업 찾기
3. 관련된 [SPEC 문서](./spec/05-core-systems/foundation/singleton_KOR.md) 읽기
4. 태스크 체크리스트 따르기

### 문서화용

**문서 작성 중이신가요?**
- [이중언어 문서 규칙](./spec/03-documentation-system/bilingual-rules_KOR.md)
- [메타데이터 표준](./spec/03-documentation-system/metadata-standard_KOR.md)
- [버전 관리](./spec/03-documentation-system/version-management_KOR.md)
- [워크플로우 규칙](./spec/03-documentation-system/workflow-rules_KOR.md)

**문서 검증 중이신가요?**
- `python .claude/scripts/doc_validate.py` 실행
- `python .claude/scripts/scope_validate.py` 실행
- [검증 가이드](./spec/06-quality/validation_KOR.md) 확인

### 프로젝트 관리용

**진행 상황 추적 중이신가요?**
- [진행 상황 대시보드](./todo/PROGRESS_KOR.md) - 전체 진행 지표
- [Phase 1 상태](./todo/phase1-core-foundation/README_KOR.md) - 현재 단계 상세
- [완료된 태스크](./todo/completed/) - 이력 기록

**다음 단계 계획 중이신가요?**
- [성공 기준](./spec/09-success-criteria/framework-goals_KOR.md) 검토
- [향후 계획](./spec/10-future/planned-features_KOR.md) 확인
- [세션 관리](./spec/08-workflow/session-management_KOR.md) 참조

---

## 📚 외부 문서

### 프레임워크 문서
- [아키텍처 문서](../doc/architecture/scope-system_KOR.md)
- [개발 가이드라인](../doc/guidelines/coding-conventions_KOR.md)
- [워크플로우 가이드](../doc/workflow/development-workflow_KOR.md)
- [스킬 가이드](../doc/workflow/skills-guide_KOR.md)
- [커맨드 가이드](../doc/workflow/commands-guide_KOR.md)

### 자동화 스크립트
- [스코프 검증](../../scripts/scope_validate.py)
- [문서 검증](../../scripts/doc_validate.py)
- [문서 동기화](../../scripts/doc_sync.py)
- [버전 증가](../../scripts/version_bump.py)
- [스크립트 README](../../scripts/README_KOR.md)

---

## 🎯 문서 구조 장점

### 모듈형 조직
- **작은 파일**: 각 문서 100-300줄 (읽기/편집 용이)
- **명확한 계층**: 직관적인 폴더 구조
- **쉬운 탐색**: 인덱스 파일 및 상호 참조
- **Git 친화적**: 명확한 diff, 최소 충돌

### 진행 상황 추적
- **단계 기반**: 개발 단계별 태스크 조직화
- **상태 추적**: PENDING → IN_PROGRESS → COMPLETED
- **의존성**: 명확한 태스크 의존성
- **이력**: 완료된 태스크 보관

### 확장성
- **쉬운 추가**: 다른 섹션 수정 없이 새 섹션 추가
- **독립적 업데이트**: 한 번에 하나의 문서만 업데이트
- **버전 관리**: 각 문서가 독립적인 버전 관리
- **협업**: 여러 사람이 동시에 작업 가능

---

## 📖 인덱스 사용 방법

### 정보 찾기

**프로젝트를 이해하고 싶다면:**
→ [SPEC 인덱스](./spec/README_KOR.md)에서 시작 → 비전 및 아키텍처 읽기

**기능을 구현하고 싶다면:**
→ [TODO 인덱스](./todo/README_KOR.md) 확인 → 작업 찾기 → 관련 SPEC 읽기

**기여하고 싶다면:**
→ [개발 워크플로우](./spec/08-workflow/development-process_KOR.md) 읽기 → 규칙 따르기

### 탐색 팁

1. **인덱스 파일 사용**: 인덱스에서 시작하여 세부 사항으로 이동
2. **상호 참조 따르기**: 문서가 관련 콘텐츠에 링크됨
3. **메타데이터 확인**: 각 문서가 부모/자식 관계를 나열
4. **검색 사용**: 이름으로 파일 찾기 또는 키워드 grep

---

## 🔄 버전 이력

| 버전 | 날짜 | 변경사항 |
|---------|------|---------|
| 3.0.0 | 2025-10-26 | 모듈화된 구조 (136개 파일) |
| 2.0.0 | 2025-10-25 | 단일 파일 SPEC/TODO (2개 파일) |
| 1.0.0 | 2025-10-25 | 초기 문서 설정 |

---

## 📞 지원

**질문이 있으신 경우:**
- 관련 SPEC 섹션 확인
- 개발 워크플로우 검토
- 코딩 규칙 참조

**문제가 있는 경우:**
- 문서 검증 오류 → 검증 스크립트 실행
- 누락된 정보 → 인덱스 탐색 확인
- 불명확한 요구사항 → SPEC 세부 사항 검토

---

**문서 상태**: Active
**관리자**: HaroFramework Team
**마지막 주요 업데이트**: 2025-10-26 (v3.0.0 - 모듈형 구조)

**총 파일 수**: 136개 (영어 70개 + 한국어 66개)
- SPEC: 62개 파일 (영어 31개 + 한국어 31개)
- TODO: 66개 파일 (영어 33개 + 한국어 33개)
- 보관: 4개 파일
- 인덱스: 4개 파일
