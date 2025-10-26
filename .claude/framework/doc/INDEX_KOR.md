---
title: Framework 문서 인덱스
version: 1.0.0
scope: framework
created: 2025-10-26
modified: 2025-10-26
category: Documentation
tags: [index, documentation, framework, reference]
paired_document: INDEX.md
parent_documents:
  - ../../MASTER_INDEX_KOR.md
child_documents:
  - ./architecture/scope-system_KOR.md
  - ./architecture/project-overview_KOR.md
  - ./guidelines/coding-conventions_KOR.md
  - ./guidelines/documentation-rules_KOR.md
  - ./workflow/development-workflow_KOR.md
  - ./workflow/skills-guide_KOR.md
  - ./workflow/commands-guide_KOR.md
  - ./reference/UNITY_FRAMEWORK_SPEC.md
references: []
status: active
---


<!-- Navigation -->
**🏠 [HaroFramework Project](../../MASTER_INDEX_KOR.md)** | **📂 [Framework 문서 인덱스](INDEX_KOR.md)** | **⬆️ [HaroFramework 프로젝트](../../MASTER_INDEX_KOR.md)**

---
# Framework 문서 인덱스

HaroFramework 개발을 위한 핵심 문서 - 아키텍처, 가이드라인, 워크플로우.

**전체 문서**: 8 files (카테고리당 4 영어 + 4 한국어)

---

## 📂 빠른 탐색

| 카테고리 | 파일 수 | 언제 읽어야 하는지 |
|----------|---------|------------------|
| [Architecture](#architecture) | 2 | 시스템 구조 이해시 |
| [Guidelines](#guidelines) | 2 | 코드나 문서 작성시 |
| [Workflow](#workflow) | 3 | 개발 프로세스 따를 때 |
| [Reference](#reference) | 1 | 기술 명세 필요시 |

---

## 🏗️ Architecture

**언제 읽어야 하는지**: 기능 구현 전, 프로젝트 구조 이해시

### [scope-system_KOR.md](./architecture/scope-system_KOR.md)
**목적**: 2-scope 아키텍처 (Framework vs Game)

**핵심 개념**:
- Framework ❌ Game (Framework는 Game 참조 불가)
- Game ✅ Framework (Game은 Framework 사용 가능)
- `scope_validate.py`로 강제
- Scope 격리를 통한 재사용성

**읽어야 할 때**:
- 새 기능 시작시
- 의존성 방향 불명확시
- 게임별 코드 추가시

---

### [project-overview_KOR.md](./architecture/project-overview_KOR.md)
**목적**: 프로젝트 구조와 기술 스택

**핵심 개념**:
- 6계층 아키텍처 개요
- 폴더 구조
- 명명 규칙
- 기술 스택 (Unity 6, URP, Input System)

**읽어야 할 때**:
- 프로젝트 처음 접할 때
- 코드베이스 탐색시
- 개발 환경 설정시

---

## 📝 Guidelines

**언제 읽어야 하는지**: 코드나 문서 작성 전

### [coding-conventions_KOR.md](./guidelines/coding-conventions_KOR.md)
**목적**: Unity 6 C# 코딩 표준

**주요 기준**:
- 명명 규칙 (PascalCase, _camelCase)
- 리전 구조 (`#region Inspector Fields`)
- Unity 6 API 사용 (FindFirstObjectByType)
- XML 문서화 요구사항
- MonoBehaviour 라이프사이클 패턴

**읽어야 할 때**:
- 새 스크립트 작성시
- 코드 리뷰시
- 명명이나 구조 불확실시

---

### [documentation-rules_KOR.md](./guidelines/documentation-rules_KOR.md)
**목적**: 이중언어 문서화 시스템

**주요 규칙**:
- 모든 `.md`는 `_KOR.md` 쌍 필요
- YAML 메타데이터 필수
- 버전 관리 (semantic versioning)
- 링크 검증
- 자동화 스크립트 사용

**읽어야 할 때**:
- 새 문서 생성시
- 기존 문서 업데이트시
- 문서 검증 오류시

---

## 🔄 Workflow

**언제 읽어야 하는지**: 개발 프로세스 따를 때

### [development-workflow_KOR.md](./workflow/development-workflow_KOR.md)
**목적**: 8단계 개발 프로세스

**프로세스**:
1. 계획 → 2. 설계 → 3. 구현 → 4. 테스트 → 5. 문서화 → 6. 검토 → 7. 통합 → 8. 검증

**읽어야 할 때**:
- 새 작업 시작시
- 프로세스 불확실시
- 품질 게이트 필요시

---

### [skills-guide_KOR.md](./workflow/skills-guide_KOR.md)
**목적**: 자동 활성화 AI 기능

**스킬**:
- unity-component (MonoBehaviour)
- unity-scriptable (ScriptableObject)
- unity-editor (에디터 확장)
- unity-testing (테스트)
- unity-shader (URP 셰이더)

**읽어야 할 때**:
- 자연어로 개발시
- 스킬 활성화 이해시
- 커스텀 스킬 생성시

---

### [commands-guide_KOR.md](./workflow/commands-guide_KOR.md)
**목적**: 수동 슬래시 명령

**명령**:
- `/component`, `/scriptable`, `/singleton`
- `/test`, `/build`, `/asmdef`
- `/scene-analyze`, `/package-add`, `/input-action`

**읽어야 할 때**:
- 명시적 제어 필요시
- 특정 패턴 반복시
- 커스텀 명령 생성시

---

## 📚 Reference

**언제 읽어야 하는지**: 기술 명세 필요시

### [UNITY_FRAMEWORK_SPEC.md](./reference/UNITY_FRAMEWORK_SPEC.md)
**목적**: 원본 Unity 프레임워크 명세

**내용**:
- 완전한 프레임워크 설계
- 기술 아키텍처 세부사항
- 구현 패턴

**읽어야 할 때**:
- 깊은 아키텍처 질문시
- 역사적 컨텍스트 필요시
- 기술 결정 불명확시

---

## 🎯 읽기 전략

### Claude Code용

**컨텍스트 < 30%**: 포괄적으로 읽기
- Architecture부터 시작
- Guidelines 검토
- Workflow 이해

**컨텍스트 30-60%**: 선택적으로 읽기
- 관련 섹션만
- 알고 있는 내용 건너뛰기
- 작업별 문서에 집중

**컨텍스트 60-85%**: 최소한으로 읽기
- 작업별로만 (1-2개 문서)
- 탐색에 인덱스 사용
- 기억에 의존

**컨텍스트 85%+**: 긴급 모드
- INDEX 파일만
- SPEC/TODO 업데이트
- `/clear` 실행

---

### 개발자용

**처음**:
1. [project-overview_KOR.md](./architecture/project-overview_KOR.md)
2. [scope-system_KOR.md](./architecture/scope-system_KOR.md)
3. [coding-conventions_KOR.md](./guidelines/coding-conventions_KOR.md)

**일상 작업**:
- 빠른 참조: 인덱스 확인
- 특정 질문: 관련 섹션 읽기
- 문서화: documentation-rules_KOR.md 읽기

---

## 🔗 관련 문서

### 프로젝트 관리
- [프로젝트 인덱스](../project/index_KOR.md)
- [SPEC 인덱스](../project/spec/README_KOR.md)
- [TODO 인덱스](../project/todo/README_KOR.md)

### 도구
- [Commands 인덱스](../../commands/INDEX_KOR.md)
- [Skills 인덱스](../../skills/INDEX_KOR.md)

### 가이드
- [빠른 시작](../project/QUICK_START_KOR.md)
- [읽기 가이드](../project/READING_GUIDE_KOR.md)

---

**문서 상태**: Active
**유지관리**: HaroFramework Team
**최종 업데이트**: 2025-10-26
