---
title: 빠른 시작 가이드
version: 1.0.0
scope: framework
created: 2025-10-26
modified: 2025-10-26
category: Guide
tags: [guide, quick-start, scenarios, checklists]
paired_document: QUICK_START.md
parent_documents:
  - ./index_KOR.md
child_documents: []
references:
  - ./READING_GUIDE_KOR.md
  - ../doc/INDEX_KOR.md
  - ../../commands/INDEX_KOR.md
  - ../../skills/INDEX_KOR.md
status: active
---


<!-- Navigation -->
**🏠 [HaroFramework Project](../../MASTER_INDEX_KOR.md)** | **📂 [HaroFramework 프로젝트 인덱스](INDEX_KOR.md)** | **⬆️ [HaroFramework 프로젝트 인덱스](index_KOR.md)**

---
# 빠른 시작 가이드

**일반 개발 작업을 위한 시나리오 기반 체크리스트**

필요한 시나리오로 바로 이동 - 각 시나리오는 필수 문서, 도구, 검증 단계 포함.

---

## 📑 시나리오

1. [Unity 컴포넌트 만들기](#1-unity-컴포넌트-만들기)
2. [ScriptableObject 만들기](#2-scriptableobject-만들기)
3. [테스트 작성하기](#3-테스트-작성하기)
4. [문서 작성하기](#4-문서-작성하기)
5. [아키텍처 이해하기](#5-아키텍처-이해하기)
6. [Core Foundation 구현하기](#6-core-foundation-구현하기)
7. [새 게임 프로젝트 시작하기](#7-새-게임-프로젝트-시작하기)
8. [세션 복원하기](#8-세션-복원하기)
9. [버그 수정하기](#9-버그-수정하기)
10. [문서 검증하기](#10-문서-검증하기)

---

## 1. Unity 컴포넌트 만들기

**목표**: 프레임워크 규칙을 따르는 MonoBehaviour 스크립트 생성

**읽기** (5-10K 토큰):
1. ✅ [코딩 규칙](../doc/guidelines/coding-conventions_KOR.md) - **필수**

**도구**:
- **자동**: "플레이어 컨트롤러 만들어" → `unity-component` 스킬
- **수동**: `/component PlayerController HaroFramework.Player`

**체크리스트**:
- [ ] Namespace: `HaroFramework.*`
- [ ] 리전: Inspector Fields, Unity Lifecycle, Methods
- [ ] XML 문서화 (`///`)
- [ ] Private 필드에 SerializeField
- [ ] Awake()에서 컴포넌트 캐싱

**검증**: `/test EditMode`

---

## 2. ScriptableObject 만들기

**목표**: 게임 설정용 데이터 에셋 생성

**읽기** (3-5K 토큰):
1. ✅ [코딩 규칙](../doc/guidelines/coding-conventions_KOR.md) - **필수**

**도구**:
- **자동**: "데미지와 사거리가 있는 무기 데이터 만들어" → `unity-scriptable` 스킬
- **수동**: `/scriptable WeaponData HaroFramework.Data`

**체크리스트**:
- [ ] Namespace: `HaroFramework.Data`
- [ ] `[CreateAssetMenu]` 속성
- [ ] OnValidate()로 데이터 검증
- [ ] XML 문서화

**검증**: Project → Create → HaroFramework → [Asset]

---

## 3. 테스트 작성하기

**목표**: 컴포넌트용 단위/통합 테스트 생성

**읽기** (3-5K 토큰):
1. ✅ [품질 기준](./spec/06-quality/code-quality_KOR.md) - **필수**

**도구**:
- **자동**: "HealthSystem 테스트 작성해" → `unity-testing` 스킬

**체크리스트**:
- [ ] Tests/ 폴더의 테스트 어셈블리 (.asmdef)
- [ ] AAA 패턴 (Arrange, Act, Assert)
- [ ] 메서드명: `Method_Condition_ExpectedBehavior`
- [ ] 긍정/부정 테스트 케이스 모두

**검증**: `/test EditMode` 또는 `/test PlayMode`

---

## 4. 문서 작성하기

**목표**: 이중언어 마크다운 문서 생성/업데이트

**읽기** (5-8K 토큰):
1. ✅ [문서화 규칙](../doc/guidelines/documentation-rules_KOR.md) - **필수**

**체크리스트**:
- [ ] 필수 필드가 있는 YAML frontmatter
- [ ] 영어 `.md` 먼저 생성
- [ ] 즉시 한국어 `_KOR.md` 생성
- [ ] `paired_document` 필드로 링크
- [ ] 네비게이션 (나중에 자동 추가됨)

**검증**:
```bash
python .claude/scripts/doc_validate.py
python .claude/scripts/doc_sync.py --check
```

---

## 5. 아키텍처 이해하기

**목표**: 프레임워크 구조와 설계 학습

**읽기** (12-15K 토큰):
1. ✅ [6계층 시스템](./spec/02-architecture/6-layer-system_KOR.md) - **필수**
2. ✅ [Scope 시스템](../doc/architecture/scope-system_KOR.md) - **필수**

**핵심 개념**:
- **2-Scope**: Framework ❌ Game, Game ✅ Framework
- **6-Layer**: Data → Domain → Core → Interface → Service → Gameplay
- **의존성 흐름**: 위 → 아래만

---

## 6. Core Foundation 구현하기

**목표**: 14개 core foundation 클래스 중 하나 구현

**읽기** (10-15K 토큰):
1. ✅ 작업: `todo/phase1-core-foundation/[task]_KOR.md` - **필수**
2. ✅ SPEC: `spec/05-core-systems/foundation/[class]_KOR.md` - **필수**
3. ✅ [코딩 규칙](../doc/guidelines/coding-conventions_KOR.md) - **필수**

**체크리스트**:
- [ ] 작업 SPEC 완전히 읽기
- [ ] 의존성 이해
- [ ] SPEC 따라 클래스 구현
- [ ] XML 문서화 작성
- [ ] 테스트 작성 (unity-testing 스킬)
- [ ] 테스트 실행: `/test EditMode`
- [ ] TODO에서 작업 완료 표시

**검증**: `/test EditMode`

---

## 7. 새 게임 프로젝트 시작하기

**목표**: 프레임워크를 사용한 새 게임 생성

**읽기** (8-10K 토큰):
1. ✅ [게임 템플릿](../../games/_template/GAME_KOR.md) - **필수**
2. ✅ [Scope 시스템](../doc/architecture/scope-system_KOR.md) - **필수**

**체크리스트**:
- [ ] `.claude/games/_template/` 복사 → `.claude/games/[game-name]/`
- [ ] `GAME.md`를 게임별 설정으로 업데이트
- [ ] 게임 네임스페이스 생성: `[GameName].*`
- [ ] Game은 Framework 사용 가능 (✅)
- [ ] Framework는 Game 참조 불가 (❌)

**검증**: `python .claude/scripts/scope_validate.py`

---

## 8. 세션 복원하기

**목표**: 이전 Claude 세션에서 작업 계속

**읽기** (3-5K 토큰):
1. ✅ [Session Restore](./SESSION_RESTORE.md) - **필수**
2. ✅ [TODO 대시보드](./todo/PROGRESS_KOR.md) - **필수**

**체크리스트**:
- [ ] SESSION_RESTORE.md 읽기
- [ ] 진행 중인 작업 TODO 확인
- [ ] 관련 SPEC 섹션 읽기
- [ ] 체크포인트부터 계속

---

## 9. 버그 수정하기

**목표**: 코드 문제 디버그 및 수정

**읽기** (5-8K 토큰):
1. ✅ [코딩 규칙](../doc/guidelines/coding-conventions_KOR.md) - **필수**
2. ✅ 영향받는 클래스 SPEC - **필수**

**체크리스트**:
- [ ] 버그 재현
- [ ] 영향받는 클래스 식별
- [ ] 클래스 SPEC 읽기
- [ ] 규칙 따라 수정
- [ ] 재발 방지 테스트 작성
- [ ] 모든 테스트 실행

**검증**: `/test All`

---

## 10. 문서 검증하기

**목표**: 문서 품질 및 동기화 확인

**도구**: 검증 스크립트

**체크리스트**:
- [ ] 메타데이터 검증 실행
- [ ] 동기화 확인 실행
- [ ] Scope 검증 실행
- [ ] 오류 수정

**검증**:
```bash
python .claude/scripts/doc_validate.py
python .claude/scripts/doc_sync.py --check
python .claude/scripts/scope_validate.py
```

---

## 🎯 올바른 시나리오 선택하기

**...하고 싶다면**
- 게임플레이 코드 만들기 → #1 (Component)
- 데이터 에셋 만들기 → #2 (ScriptableObject)
- 품질 보장 → #3 (Tests)
- 기능 문서화 → #4 (Documentation)
- 프레임워크 학습 → #5 (Architecture)
- 코어 빌드 → #6 (Core Foundation)
- 게임 만들기 → #7 (New Game)
- 작업 계속 → #8 (Restore Session)
- 문제 수정 → #9 (Fix Bug)
- 품질 확인 → #10 (Validate)

---

## 💡 팁

### 시나리오 시작 전

1. **컨텍스트 사용량 확인**: [읽기 가이드](./READING_GUIDE_KOR.md) 사용
2. **TODO 확인**: [진행 대시보드](./todo/PROGRESS_KOR.md) 검토
3. **최소한으로 읽기**: 필수 문서만

### 작업 중

1. **체크리스트 따르기**: 단계 건너뛰지 않기
2. **조기 검증**: 자주 테스트/검증 실행
3. **즉시 문서화**: 끝까지 기다리지 않기

### 완료 후

1. **TODO 업데이트**: 작업 완료 표시
2. **검증 실행**: 품질 보장
3. **변경사항 커밋**: git 가이드라인 준수

---

**문서 상태**: Active
**유지관리**: HaroFramework Team
**최종 업데이트**: 2025-10-26

**기억하세요**: 이것은 시작점입니다 - 필요에 따라 조정하세요!
