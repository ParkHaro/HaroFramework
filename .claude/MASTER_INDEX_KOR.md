---
title: HaroFramework 프로젝트
version: 1.0.0
scope: framework
created: 2025-10-26
modified: 2025-10-26
category: Master Index
tags: [index, master, navigation, documentation, project-root]
paired_document: MASTER_INDEX.md
parent_documents: []
child_documents:
  - ./commands/INDEX_KOR.md
  - ./skills/INDEX_KOR.md
  - ./framework/doc/INDEX_KOR.md
  - ./framework/project/index_KOR.md
references:
  - ../CLAUDE.md
  - ./framework/project/QUICK_START_KOR.md
  - ./framework/project/READING_GUIDE_KOR.md
status: active
---


<!-- Navigation -->
**🏠 [HaroFramework Project](MASTER_INDEX_KOR.md)** | **📂 [HaroFramework 프로젝트](./)** | **⬆️ [HaroFramework 프로젝트](./)**

---
# HaroFramework 프로젝트

**재사용 가능한 Unity 6 게임 프레임워크** - 6계층 아키텍처, 이중언어 문서, AI 기반 개발 도구 제공.

**프로젝트 버전**: 3.0.0 | **Unity**: 6000.2.9f1 | **URP**: 17.2.0 | **Input System**: 1.14.2

---

## 🚀 빠른 시작

**HaroFramework가 처음이신가요?**
1. [핵심 규칙](../CLAUDE.md) 읽기 (5분)
2. [빠른 시작 가이드](./framework/project/QUICK_START_KOR.md) 확인 (10분)
3. [Phase 1 작업](./framework/project/todo/phase1-core-foundation/README_KOR.md)부터 시작

**개발 계속하기?**
- [TODO 대시보드](./framework/project/todo/PROGRESS_KOR.md) 보기
- [읽기 가이드](./framework/project/READING_GUIDE_KOR.md)로 효율적인 문서 읽기
- [세션 복원](./framework/project/SESSION_RESTORE.md) 검토

---

## 📂 프로젝트 구조

### 1. Framework 문서
**위치**: `.claude/framework/doc/`

아키텍처, 가이드라인, 워크플로우를 다루는 종합 문서.

**주요 문서**:
- [Scope 시스템](./framework/doc/architecture/scope-system_KOR.md) - 2-scope 아키텍처 (Framework vs Game)
- [코딩 규칙](./framework/doc/guidelines/coding-conventions_KOR.md) - Unity 6 모범 사례
- [개발 워크플로우](./framework/doc/workflow/development-workflow_KOR.md) - 8단계 프로세스
- [문서화 규칙](./framework/doc/guidelines/documentation-rules_KOR.md) - 이중언어 문서 시스템

👉 **[모든 Framework 문서 탐색](./framework/doc/INDEX_KOR.md)**

---

### 2. 프로젝트 관리
**위치**: `.claude/framework/project/`

프로젝트 명세, 작업 추적, 진행 모니터링.

**주요 문서**:
- [프로젝트 인덱스](./framework/project/index_KOR.md) - 마스터 프로젝트 인덱스
- [SPEC 인덱스](./framework/project/spec/README_KOR.md) - 10개 섹션 명세
- [TODO 인덱스](./framework/project/todo/README_KOR.md) - 작업 추적 시스템
- [진행 대시보드](./framework/project/todo/PROGRESS_KOR.md) - 실시간 진행상황

**빠른 참조**:
- [빠른 시작 가이드](./framework/project/QUICK_START_KOR.md) - 시나리오별 가이드
- [읽기 가이드](./framework/project/READING_GUIDE_KOR.md) - 토큰 최적화 전략

👉 **[프로젝트 관리 보기](./framework/project/index_KOR.md)**

---

### 3. Commands & Skills
**위치**: `.claude/commands/` & `.claude/skills/`

Unity 워크플로우를 위한 개발 도구 - 수동 명령과 자동 활성화 스킬.

#### Commands (수동 호출)
정확한 제어를 위한 명시적 슬래시 명령.

**인기 명령**:
- `/component <이름>` - MonoBehaviour 컴포넌트 생성
- `/scriptable <이름>` - ScriptableObject 생성
- `/test [모드]` - Unity 테스트 실행
- `/build [플랫폼]` - Unity 프로젝트 빌드

👉 **[모든 명령](./commands/INDEX_KOR.md)** (9개)

#### Skills (자동 활성화)
자연어로 활성화되는 AI 기반 기능.

**사용 가능한 스킬**:
- `unity-component` - MonoBehaviour 생성
- `unity-scriptable` - ScriptableObject 생성
- `unity-editor` - 에디터 확장
- `unity-testing` - 테스트 생성
- `unity-shader` - URP 셰이더 생성

👉 **[모든 스킬](./skills/INDEX_KOR.md)** (5개)

---

### 4. 자동화 스크립트
**위치**: `.claude/framework/scripts/` & `.claude/scripts/`

검증, 자동화, 유지보수 도구.

**사용 가능한 스크립트**:
- `scope_validate.py` - scope 의존성 규칙 강제
- `doc_validate.py` - 문서 메타데이터 검증
- `doc_sync.py` - 이중언어 문서 동기화 확인
- `version_bump.py` - 자동화된 버전 관리
- `add_navigation.py` - 스마트 네비게이션 생성기

**사용법**:
```bash
# scope 의존성 검증
python .claude/scripts/scope_validate.py

# 문서 확인
python .claude/scripts/doc_validate.py

# 모든 문서에 네비게이션 추가
python .claude/framework/scripts/add_navigation.py --apply-all
```

👉 **[스크립트 문서](./framework/scripts/README_KOR.md)**

---

### 5. 게임 프로젝트
**위치**: `.claude/games/`

프레임워크를 사용한 게임별 구현.

**구조**:
```
.claude/games/
├── _template/          # 게임 프로젝트 템플릿
│   ├── GAME.md         # 게임별 Claude 설정
│   ├── project/        # SPEC & TODO
│   └── doc/            # 게임 문서
│
└── [game-name]/        # 실제 게임 프로젝트
    └── (템플릿과 동일한 구조)
```

👉 **[게임 템플릿](./games/_template/GAME_KOR.md)**

---

## 🎯 일반 작업

### Claude Code용

#### 새 세션 시작
1. [프로젝트 인덱스](./framework/project/index_KOR.md) 읽기
2. [TODO 대시보드](./framework/project/todo/PROGRESS_KOR.md) 읽기
3. 토큰 최적화를 위한 [읽기 가이드](./framework/project/READING_GUIDE_KOR.md) 확인
4. [세션 복원](./framework/project/SESSION_RESTORE.md)의 마지막 체크포인트부터 계속

#### Core Foundation 구현
1. 작업 명세 읽기: [Phase 1 작업](./framework/project/todo/phase1-core-foundation/README_KOR.md)
2. SPEC 읽기: [Core Systems](./framework/project/spec/05-core-systems/README_KOR.md)
3. 규칙 따르기: [코딩 규칙](./framework/doc/guidelines/coding-conventions_KOR.md)
4. 테스트 실행: `/test EditMode`

#### 문서 작성
1. [문서화 규칙](./framework/doc/guidelines/documentation-rules_KOR.md) 읽기
2. 이중언어 템플릿 사용
3. 메타데이터 추가
4. 검증: `python .claude/scripts/doc_validate.py`

---

### 개발자용

#### 프레임워크 학습
1. **아키텍처**: [6계층 시스템](./framework/project/spec/02-architecture/6-layer-system_KOR.md)
2. **Scope 규칙**: [Scope 시스템](./framework/doc/architecture/scope-system_KOR.md)
3. **규칙**: [코딩 규칙](./framework/doc/guidelines/coding-conventions_KOR.md)
4. **워크플로우**: [개발 워크플로우](./framework/doc/workflow/development-workflow_KOR.md)

#### 컴포넌트 생성
- **자동**: "플레이어 체력 시스템 만들어" → unity-component 스킬
- **수동**: `/component HealthSystem HaroFramework.Player`
- **테스팅**: "HealthSystem 테스트 작성해" → unity-testing 스킬

#### 새 게임 시작
1. [게임 템플릿](./games/_template/) 복사
2. GAME.md 설정 업데이트
3. [Scope 규칙](./framework/doc/architecture/scope-system_KOR.md) 준수
4. Game은 Framework 사용 가능, Framework는 Game 참조 불가

---

## 📖 문서화 시스템

### 이중언어 지원
모든 문서는 다음 언어로 제공:
- **영어**: `*.md` 파일
- **한국어**: `*_KOR.md` 파일

**Claude Code용**: 영어 파일만 읽기 (토큰 최적화)
**개발자용**: 선호하는 언어 선택

### 네비게이션 시스템
모든 문서에 스마트 네비게이션 포함:
```markdown
🏠 [Home](경로) | 📂 [Category](경로) | ⬆️ [Parent](경로)
```

네비게이션에 실제 문서 제목 표시로 쉬운 탐색.

---

## 🏗️ 아키텍처 개요

### 2-Scope 시스템
```
Framework Scope (.claude/framework/)
  ✅ 재사용 가능한 게임 프레임워크
  ✅ 게임 독립적
  ❌ Game scope 참조 불가

Game Scope (.claude/games/[game-name]/)
  ✅ 특정 게임 구현
  ✅ Framework 사용 가능
  ✅ Framework 참조 가능
```

### 6계층 아키텍처
```
┌─────────────────────────────────────┐
│      Gameplay Layer (Game)          │ ← MonoBehaviour 컴포넌트
├─────────────────────────────────────┤
│      Service Layer                  │ ← 비즈니스 로직 서비스
├─────────────────────────────────────┤
│      Interface Layer                │ ← 계약 및 인터페이스
├─────────────────────────────────────┤
│      Core Layer                     │ ← 핵심 시스템 (EventBus, ServiceLocator)
├─────────────────────────────────────┤
│      Domain Layer                   │ ← 비즈니스 로직 & 검증
├─────────────────────────────────────┤
│      Data Layer                     │ ← ScriptableObject 데이터
└─────────────────────────────────────┘
```

**의존성 흐름**: 위 → 아래만 (상향 의존성 없음)

👉 **[전체 아키텍처 상세](./framework/project/spec/02-architecture/6-layer-system_KOR.md)**

---

## 📊 현재 상태

### 진행상황
- **Phase 0**: ✅ 문서 설정 완료
- **Phase 1**: 🔴 Core Foundation (0/14 작업) - 대기중
- **Phase 2**: ⏳ Core Modules (TBD)
- **Phase 3**: ⏳ 예제 구현 (TBD)
- **Phase 4**: ⏳ 문서 & 테스팅 (TBD)

👉 **[진행 대시보드 보기](./framework/project/todo/PROGRESS_KOR.md)**

### 문서화
- **전체 파일**: 148개 (74 EN + 74 KR)
- **SPEC**: 62 files (31 EN + 31 KR)
- **TODO**: 66 files (33 EN + 33 KR)
- **Commands**: 9 files
- **Skills**: 5 files
- **Indexes**: 6 files (3 EN + 3 KR)

### 기술 스택
- **Unity**: 6000.2.9f1 (Unity 6)
- **URP**: 17.2.0 (Universal Render Pipeline)
- **Input System**: 1.14.2 (New Input System)
- **Testing**: Unity Test Framework

---

## 💡 모범 사례

### Claude Code용
1. **효율적으로 읽기**: 컨텍스트 사용량에 따라 [읽기 가이드](./framework/project/READING_GUIDE_KOR.md) 사용
2. **TODO 확인**: 작업 시작 전 항상 [TODO 대시보드](./framework/project/todo/PROGRESS_KOR.md) 검토
3. **규칙 준수**: [코딩 규칙](./framework/doc/guidelines/coding-conventions_KOR.md) 준수
4. **검증**: 커밋 전 검증 스크립트 실행
5. **문서화**: 코딩하면서 문서 업데이트

### 개발자용
1. **아키텍처 이해**: [6계층 시스템](./framework/project/spec/02-architecture/6-layer-system_KOR.md) 읽기
2. **Scope 존중**: [Scope 규칙](./framework/doc/architecture/scope-system_KOR.md) 엄격히 준수
3. **도구 사용**: 생산성을 위해 commands와 skills 활용
4. **모든 것 테스트**: >80% 테스트 커버리지 목표
5. **문서화**: 이중언어 문서 작성

---

## 🔍 정보 찾기

### 주제별
- **아키텍처**: [6계층 시스템](./framework/project/spec/02-architecture/6-layer-system_KOR.md)
- **코딩**: [코딩 규칙](./framework/doc/guidelines/coding-conventions_KOR.md)
- **문서화**: [문서화 규칙](./framework/doc/guidelines/documentation-rules_KOR.md)
- **테스팅**: [품질 기준](./framework/project/spec/06-quality/code-quality_KOR.md)
- **워크플로우**: [개발 워크플로우](./framework/doc/workflow/development-workflow_KOR.md)

### 역할별
- **신입 개발자**: [빠른 시작](./framework/project/QUICK_START_KOR.md)부터
- **AI 어시스턴트**: [읽기 가이드](./framework/project/READING_GUIDE_KOR.md) 읽기
- **아키텍트**: [SPEC 인덱스](./framework/project/spec/README_KOR.md) 검토
- **QA**: [테스팅 가이드](./framework/project/spec/06-quality/code-quality_KOR.md) 확인

### 작업별
- **컴포넌트 생성**: `/component` 또는 자연어 사용
- **테스트 실행**: `/test` 명령
- **프로젝트 빌드**: `/build` 명령
- **패키지 추가**: `/package-add` 명령

---

## 🎓 학습 경로

### 초급 (0-2시간)
1. [핵심 규칙](../CLAUDE.md) - 5분
2. [빠른 시작](./framework/project/QUICK_START_KOR.md) - 10분
3. [Scope 시스템](./framework/doc/architecture/scope-system_KOR.md) - 15분
4. [코딩 규칙](./framework/doc/guidelines/coding-conventions_KOR.md) - 30분
5. `/component`로 컴포넌트 만들기 시도 - 15분

### 중급 (2-8시간)
1. [6계층 아키텍처](./framework/project/spec/02-architecture/6-layer-system_KOR.md) - 1시간
2. [Core Systems SPEC](./framework/project/spec/05-core-systems/README_KOR.md) - 2시간
3. [Phase 1 작업](./framework/project/todo/phase1-core-foundation/README_KOR.md) 구현 - 4시간
4. unity-testing 스킬로 테스트 작성 - 1시간

### 고급 (8+시간)
1. Core Foundation 완료 (Phase 1) - 8시간
2. Core Modules 구현 (Phase 2) - 10시간
3. 예제 게임 생성 (Phase 3) - 12시간
4. 전체 문서화 & 테스팅 (Phase 4) - 6시간

---

**문서 상태**: Active
**유지관리**: HaroFramework Team
**최종 업데이트**: 2025-10-26
**전체 파일 수**: 148 문서 파일

**HaroFramework에 오신 것을 환영합니다! 🎮**
