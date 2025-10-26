---
title: Claude Code 읽기 가이드
version: 1.0.0
scope: framework
created: 2025-10-26
modified: 2025-10-26
category: Guide
tags: [guide, token-optimization, reading-strategy, context-management]
paired_document: READING_GUIDE.md
parent_documents:
  - ./index_KOR.md
child_documents: []
references:
  - ./QUICK_START_KOR.md
  - ./SESSION_RESTORE.md
  - ../doc/INDEX_KOR.md
status: active
---


<!-- Navigation -->
**🏠 [HaroFramework Project](../../MASTER_INDEX_KOR.md)** | **📂 [HaroFramework 프로젝트 인덱스](INDEX_KOR.md)** | **⬆️ [HaroFramework 프로젝트 인덱스](index_KOR.md)**

---
# Claude Code 읽기 가이드

**효율적인 문서 읽기를 위한 토큰 최적화 전략**

이 가이드는 Claude Code가 컨텍스트 사용량에 따라 필요한 문서만 읽도록 도와 30-50% 토큰을 절약합니다.

**컨텍스트 제한**: 200K 토큰 | **모니터링**: 현재 토큰 사용량 비율

---

## 📊 컨텍스트 기반 읽기 전략

### 🟢 Green Zone (0-30% / 0-60K 토큰)
**상태**: 충분한 컨텍스트 사용 가능

**전략**: **포괄적 읽기**

**읽을 것**:
- [Master Index](../../MASTER_INDEX_KOR.md)부터 시작
- [프로젝트 인덱스](./index_KOR.md) 읽기
- [TODO 대시보드](./todo/PROGRESS_KOR.md) 검토
- 작업별 SPEC 섹션
- [빠른 시작](./QUICK_START_KOR.md) 시나리오 확인

**이유**: 완전한 이해 구축, 최적화 불필요

---

### 🟡 Yellow Zone (30-60% / 60-120K 토큰)
**상태**: 보통 수준 컨텍스트 사용

**전략**: **선택적 읽기**

**읽을 것**:
- [TODO 대시보드](./todo/PROGRESS_KOR.md) - 현재 작업만
- 작업별 SPEC (1-2개 파일)
- 관련 가이드라인 (필요시)

**건너뛸 것**:
- 이미 읽은 일반 개요
- 자세한 예제
- 전체 SPEC 섹션 (인덱스 사용)

**이유**: 작업 컨텍스트 유지하면서 토큰 절약

---

### 🟠 Orange Zone (60-85% / 120-170K 토큰)
**상태**: 높은 컨텍스트 사용 - **주의**

**전략**: **최소 읽기**

**읽을 것** (최대 2-3개 파일):
- TODO의 특정 작업 파일
- 직접 관련된 하나의 SPEC 섹션
- 인덱스에서 빠른 참조

**건너뛸 것**:
- 작업과 직접 관련 없는 모든 것
- 아키텍처 개요
- 가이드라인 (기억에 의존)
- 예제와 튜토리얼

**이유**: 중요한 토큰 보존

---

### 🔴 Red Zone (85%+ / 170K+ 토큰)
**상태**: **긴급** - 컨텍스트 거의 가득참

**전략**: **인덱스만 + 즉시 조치**

**읽을 것** (최대 1개 파일):
- [TODO 대시보드](./todo/PROGRESS_KOR.md)만

**즉시 조치**:
1. 현재 진행상황으로 [TODO](./TODO_KOR.md) 업데이트
2. 변경사항으로 [SPEC](./SPEC_KOR.md) 업데이트
3. [Session Restore](./SESSION_RESTORE.md)에 현재 상태 문서화
4. `/clear` 명령 실행
5. 체크포인트부터 새 세션 시작

**이유**: 컨텍스트 오버플로우 방지, 연속성 확보

---

## 🎯 작업 기반 읽기 맵

"각 작업 유형별로 무엇을 읽어야 하는지" 빠른 참조

### 1. Core Foundation 클래스 구현
**컨텍스트 예산**: 10-15K 토큰

**필수 읽기** (우선순위 순):
1. 작업 파일: `todo/phase1-core-foundation/[task]_KOR.md` (2K)
2. SPEC: `spec/05-core-systems/foundation/[class]_KOR.md` (3K)
3. 코딩 규칙: `doc/guidelines/coding-conventions_KOR.md` (5K)

**선택적** (컨텍스트 허용시):
- 6계층 아키텍처: `spec/02-architecture/6-layer-system_KOR.md`

**건너뛰기**:
- 일반 프로젝트 개요
- 다른 SPEC 섹션
- 워크플로우 문서

---

### 2. 새 게임 프로젝트 생성
**컨텍스트 예산**: 8-10K 토큰

**필수 읽기**:
1. 게임 템플릿: `games/_template/GAME_KOR.md` (2K)
2. Scope 시스템: `doc/architecture/scope-system_KOR.md` (3K)
3. 프로젝트 구조: `spec/02-architecture/folder-structure_KOR.md` (3K)

**건너뛰기**:
- 자세한 프레임워크 구현
- Core systems SPEC
- 테스팅 가이드라인

---

### 3. 문서 작성
**컨텍스트 예산**: 5-8K 토큰

**필수 읽기**:
1. 문서화 규칙: `doc/guidelines/documentation-rules_KOR.md` (8K)
2. 기존 문서의 메타데이터 템플릿 (1K)

**건너뛰기**:
- 코드 구현 세부사항
- 아키텍처 개요
- 워크플로우 문서

---

### 4. 테스트 실행
**컨텍스트 예산**: 5K 토큰

**필수 읽기**:
1. 품질 기준: `spec/06-quality/code-quality_KOR.md` (3K)
2. 테스트 명령: `commands/test.md` (1K)

---

### 5. 아키텍처 이해
**컨텍스트 예산**: 12-15K 토큰

**필수 읽기**:
1. 6계층 시스템: `spec/02-architecture/6-layer-system_KOR.md` (5K)
2. Scope 시스템: `doc/architecture/scope-system_KOR.md` (3K)
3. 프로젝트 개요: `doc/architecture/project-overview_KOR.md` (4K)

---

### 6. 코드 리뷰 / 버그 수정
**컨텍스트 예산**: 5-8K 토큰

**필수 읽기**:
1. 코딩 규칙: `doc/guidelines/coding-conventions_KOR.md` (5K)
2. 영향받는 클래스의 특정 SPEC (3K)

---

### 7. 세션 복원
**컨텍스트 예산**: 3-5K 토큰

**필수 읽기**:
1. Session Restore: `SESSION_RESTORE.md` (1K)
2. TODO 대시보드: `todo/PROGRESS_KOR.md` (2K)
3. SPEC/TODO의 마지막 체크포인트 (2K)

---

### 8. 변경사항 커밋
**컨텍스트 예산**: 2-3K 토큰

**필수 읽기**:
1. CLAUDE.md의 Git 가이드라인 (2K)

---

### 9. 검증 / 품질 검사
**컨텍스트 예산**: 5-7K 토큰

**필수 읽기**:
1. 품질 기준: `spec/06-quality/` (4K)
2. 검증 가이드: `spec/06-quality/validation_KOR.md` (3K)

---

### 10. 새 Command/Skill 추가
**컨텍스트 예산**: 8-10K 토큰

**필수 읽기**:
1. Commands/Skills Index (2K)
2. 예제 command/skill 파일 (2K)
3. Commands/skills 워크플로우 가이드 (4K)

---

## 💡 토큰 절약 팁

### 읽기 기법

**1. 인덱스 먼저 사용**
```
❌ 전체 SPEC 읽기 → 필요한 것 찾기
✅ INDEX 읽기 → 특정 섹션으로 이동
절약: 50-70% 토큰
```

**2. 영어만 읽기**
```
❌ .md와 _KOR.md 둘 다 읽기
✅ .md만 읽기 (한국어는 사람용)
절약: 50% 토큰
```

**3. 내용 전에 메타데이터 읽기**
```
✅ 메타데이터 `references` 필드 확인
→ 추가로 필요한 것 파악
→ 읽기 전략 계획
절약: 불필요한 재읽기 방지
```

**4. 시나리오용 Quick Start 사용**
```
❌ 여러 문서 검색
✅ QUICK_START_KOR.md에서 시나리오 확인
→ 필요한 정확한 문서 얻기
절약: 30-40% 토큰
```

**5. 네비게이션 활용**
```
✅ 모든 문서에 관련 문서 네비게이션
→ 검색 대신 직접 링크 따라가기
절약: 시간과 토큰
```

---

## 📈 컨텍스트 사용량 모니터링

### 정기적으로 컨텍스트 확인

**30분마다 또는 주요 작업 후**:
```
현재: X 토큰 / 200K 토큰 = Y%

Y < 30%: Green zone - 자유롭게 읽기
30% ≤ Y < 60%: Yellow zone - 선택적으로 읽기
60% ≤ Y < 85%: Orange zone - 최소한으로 읽기
Y ≥ 85%: Red zone - 긴급 모드
```

### 컨텍스트 사용량 예측

**일반적인 토큰 비용**:
- 인덱스 파일: 1-2K 토큰
- 짧은 가이드 (Quick Start): 3-5K 토큰
- SPEC 섹션: 3-8K 토큰
- 전체 SPEC 문서: 15-30K 토큰
- 코드 파일: 2-5K 토큰
- Command/Skill 파일: 1-2K 토큰

---

## 🔄 세션 관리

### 85% 규칙

**컨텍스트가 85% (170K 토큰)에 도달하면**:

**필수 조치**:
1. **TODO.md 업데이트**
2. **SPEC.md 업데이트** (변경시)
3. **SESSION_RESTORE.md 생성**
4. **`/clear` 실행**

### 새 세션 시작

**첫 조치** (5-10K 토큰):
1. SESSION_RESTORE.md 읽기 (1K)
2. TODO 대시보드 읽기 (2K)
3. 진행 중인 작업 SPEC 읽기 (4K)
4. 체크포인트부터 계속

---

## 🎓 모범 사례

### 해야 할 것 ✅

1. **읽기 전에 컨텍스트 확인**
2. **인덱스와 네비게이션 사용**
3. **작업별로만 읽기**
4. **85%에서 체크포인트 업데이트**
5. **메모리 활용**

### 하지 말아야 할 것 ❌

1. **모든 것 읽지 않기**
2. **체크포인트 건너뛰지 않기**
3. **한국어 문서 읽지 않기**
4. **컨텍스트 경고 무시 안 함**
5. **필요 없으면 예제 읽지 않기**

---

## 🚀 빠른 결정 트리

```
새 세션 시작?
├─ Yes → SESSION_RESTORE + TODO 읽기 (5K 토큰)
└─ No → 계속

컨텍스트 사용량?
├─ < 30% → 포괄적으로 읽기
├─ 30-60% → 선택적으로 읽기 (작업별)
├─ 60-85% → 최소한으로 읽기 (최대 1-2개 파일)
└─ ≥ 85% → 중지 - 업데이트 & /clear

작업 유형?
├─ 구현 → 작업 + SPEC + 규칙
├─ 테스팅 → 품질 기준 + 테스트 가이드
├─ 문서화 → 문서 규칙 + 메타데이터
├─ 아키텍처 → 6계층 + scope 시스템
└─ 버그 수정 → 영향받는 클래스 SPEC + 규칙

기억으로 대체 가능?
├─ Yes (내용 알고 있음) → 읽기 생략
└─ No (익숙하지 않음) → 필요한 문서 읽기
```

---

**문서 상태**: Active
**유지관리**: HaroFramework Team
**최종 업데이트**: 2025-10-26

**기억하세요**: 효율적인 읽기 = 실제 작업을 위한 더 많은 컨텍스트! 🚀
