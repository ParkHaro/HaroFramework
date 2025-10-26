---
title: HaroFramework TODO 인덱스
version: 3.0.0
scope: framework
created: 2025-10-26
modified: 2025-10-26
category: Task Management
tags: [todo, tasks, index, progress]
paired_document: README.md
parent_documents:
  - ../index_KOR.md
child_documents:
  - ./PROGRESS_KOR.md
  - ./phase1-core-foundation/README_KOR.md
  - ./phase2-core-modules/README_KOR.md
  - ./phase3-example/README_KOR.md
  - ./phase4-documentation/README_KOR.md
references:
  - ../spec/README_KOR.md
status: active
---

# HaroFramework TODO 인덱스

HaroFramework 개발을 위한 태스크 관리 및 진행 상황 추적입니다.

**총 TODO 파일 수**: 66개 (영어 33개 + 한국어 33개)

---

## 📊 전체 진행 상황

👉 **[상세 진행 상황 대시보드 보기](./PROGRESS_KOR.md)**

### 빠른 통계
- **총 단계 수**: 4개
- **총 태스크 수**: 40개 이상 (Phase 1에 14개)
- **완료**: 6개 (문서 설정, 자동화 스크립트)
- **진행 중**: 0개
- **대기 중**: 34개 이상

### 현재 집중 영역
**Phase 1: 핵심 기반** - 14개 태스크 (PENDING)

다음 태스크: **[CF-001: Singleton.cs](./phase1-core-foundation/phase-a-foundation/CF-001-singleton_KOR.md)**

---

## 📁 태스크 구조

### ✅ [완료된 태스크](./completed/)
**상태**: ARCHIVED

성공적으로 완료되고 참조를 위해 보관된 태스크입니다.

#### [문서 설정](./completed/documentation-setup/)
- **IP-001**: 초기 프로젝트 구조 및 SPEC/TODO 생성
- **완료**: 2025-10-26
- **성과**: 폴더 구조, 이중언어 문서 시스템, 메타데이터 표준

#### [자동화 스크립트](./completed/automation-scripts/)
- **P-002**: 4개 자동화 스크립트 개발
- **완료**: 2025-10-26
- **결과물**: scope_validate.py, doc_validate.py, doc_sync.py, version_bump.py

---

### 🔵 [Phase 1: 핵심 기반](./phase1-core-foundation/README_KOR.md)
**상태**: PENDING | **태스크**: 14개 | **완료율**: 0%

**목표**: 기초 기본 클래스 및 핵심 시스템 구현

**예상 노력**: 8-12시간

**단계**:
- [Phase A: 기반 계층](./phase1-core-foundation/phase-a-foundation/) - 3개 태스크 (50분)
- [Phase B: 핵심 시스템](./phase1-core-foundation/phase-b-core-systems/) - 4개 태스크 (2.5시간)
- [Phase C: 기본 클래스](./phase1-core-foundation/phase-c-base-classes/) - 5개 태스크 (3시간)
- [Phase D: 프레임워크 관리자](./phase1-core-foundation/phase-d-framework-manager/) - 2개 태스크 (2시간)

#### Phase A: 기반 계층 (3개 태스크)
| 태스크 | 이름 | 노력 | 상태 |
|------|------|--------|--------|
| [CF-001](./phase1-core-foundation/phase-a-foundation/CF-001-singleton_KOR.md) | Singleton.cs | 20분 | 🔴 PENDING |
| [CF-002](./phase1-core-foundation/phase-a-foundation/CF-002-imodule_KOR.md) | IModule.cs | 15분 | 🔴 PENDING |
| [CF-003](./phase1-core-foundation/phase-a-foundation/CF-003-iservice_KOR.md) | IService.cs | 15분 | 🔴 PENDING |

#### Phase B: 핵심 시스템 (4개 태스크)
| 태스크 | 이름 | 노력 | 의존성 | 상태 |
|------|------|--------|--------------|--------|
| [CF-004](./phase1-core-foundation/phase-b-core-systems/CF-004-eventbus_KOR.md) | EventBus.cs | 40분 | CF-001 | 🔴 PENDING |
| [CF-005](./phase1-core-foundation/phase-b-core-systems/CF-005-service-locator_KOR.md) | ServiceLocator.cs | 30분 | CF-001, CF-003 | 🔴 PENDING |
| [CF-006](./phase1-core-foundation/phase-b-core-systems/CF-006-data-manager_KOR.md) | DataManager.cs | 30분 | CF-001 | 🔴 PENDING |
| [CF-007](./phase1-core-foundation/phase-b-core-systems/CF-007-framework-logger_KOR.md) | FrameworkLogger.cs | 30분 | None | 🔴 PENDING |

#### Phase C: 기본 클래스 (5개 태스크)
| 태스크 | 이름 | 노력 | 의존성 | 상태 |
|------|------|--------|--------------|--------|
| [CF-008](./phase1-core-foundation/phase-c-base-classes/CF-008-base-data_KOR.md) | BaseData.cs | 20분 | None | 🔴 PENDING |
| [CF-009](./phase1-core-foundation/phase-c-base-classes/CF-009-base-domain_KOR.md) | BaseDomain.cs | 30분 | CF-008, CF-006 | 🔴 PENDING |
| [CF-010](./phase1-core-foundation/phase-c-base-classes/CF-010-base-module_KOR.md) | BaseModule.cs | 30분 | CF-002, CF-004, CF-005, CF-006 | 🔴 PENDING |
| [CF-011](./phase1-core-foundation/phase-c-base-classes/CF-011-base-service_KOR.md) | BaseService.cs | 30분 | CF-003, CF-004, CF-005, CF-006 | 🔴 PENDING |
| [CF-012](./phase1-core-foundation/phase-c-base-classes/CF-012-base-gameplay_KOR.md) | BaseGameplay.cs | 40분 | CF-004, CF-005 | 🔴 PENDING |

#### Phase D: 프레임워크 관리자 (2개 태스크)
| 태스크 | 이름 | 노력 | 의존성 | 상태 |
|------|------|--------|--------------|--------|
| [CF-013](./phase1-core-foundation/phase-d-framework-manager/CF-013-framework-config_KOR.md) | FrameworkConfig.cs | 30분 | None | 🔴 PENDING |
| [CF-014](./phase1-core-foundation/phase-d-framework-manager/CF-014-framework-manager_KOR.md) | FrameworkManager.cs | 90분 | All previous | 🔴 PENDING |

---

### ⏳ [Phase 2: 핵심 모듈](./phase2-core-modules/README_KOR.md)
**상태**: PLANNING | **태스크**: TBD | **완료율**: 0%

**목표**: 게임 독립적인 핵심 모듈 구현

**예상 노력**: 10-15시간

**모듈**:
- UIModule - 캔버스 관리 및 UI 풀링
- AudioModule - BGM/SFX 재생 및 볼륨 제어
- SceneModule - 씬 로딩 및 전환
- NetworkModule - 기본 네트워킹 (선택사항)

**세부사항**: Phase 1 완료 후 상세화 예정

---

### ⏳ [Phase 3: 예제 구현](./phase3-example/README_KOR.md)
**상태**: PLANNING | **태스크**: TBD | **완료율**: 0%

**목표**: 모든 6계층을 시연하는 완전한 RPG 예제 생성

**예상 노력**: 12-18시간

**구성요소**:
- Data 계층: ItemData, PlayerData
- Domain 계층: ItemDomain, PlayerStatsDomain
- Interface 계층: IInventorySystem, IBattleSystem
- Service 계층: InventoryService, BattleService
- Gameplay 계층: PlayerController
- 이벤트: ItemAddedEvent, PlayerDamagedEvent

**세부사항**: Phase 2 완료 후 상세화 예정

---

### ⏳ [Phase 4: 문서화 및 테스트](./phase4-documentation/README_KOR.md)
**상태**: PLANNING | **태스크**: TBD | **완료율**: 0%

**목표**: 포괄적인 문서화 및 테스트 커버리지

**예상 노력**: 6-8시간

**영역**:
- API 문서 생성
- 튜토리얼 문서
- 단위 테스트 (>80% 커버리지)
- 통합 테스트
- 성능 벤치마크

**세부사항**: Phase 3 완료 후 상세화 예정

---

## 🎯 TODO 시스템 사용 방법

### 태스크 실행용

**새 태스크 시작:**
1. 현재 단계에 대한 [진행 상황 대시보드](./PROGRESS_KOR.md) 확인
2. 단계 폴더로 이동 (예: [Phase 1](./phase1-core-foundation/README_KOR.md))
3. 다음 대기 중 태스크 찾기 (예: [CF-001](./phase1-core-foundation/phase-a-foundation/CF-001-singleton_KOR.md))
4. 태스크 세부사항 및 체크리스트 읽기
5. 관련 [SPEC 문서](../spec/05-core-systems/foundation/singleton_KOR.md) 읽기
6. 구현 체크리스트 따르기
7. 검증 기준 완료
8. 태스크를 완료로 표시
9. 다음 태스크로 이동

**태스크 문서 구조:**
각 태스크 문서는 다음을 포함합니다:
- 📊 태스크 개요 (ID, 상태, 우선순위, 노력, 의존성)
- 🎯 목표 (목적)
- 📝 상세 설명
- ✅ 구현 체크리스트
- 🧪 검증 기준
- 📚 참고 문서
- ✔️ 완료 조건
- 📦 Git Commit (커밋 메시지 템플릿)
- 🔗 연관 태스크
- 📅 타임라인 (날짜 및 기간)
- 💬 노트 (팁 및 알려진 문제)

### 진행 상황 추적용

**일일 진행 상황 검토:**
- [진행 상황 대시보드](./PROGRESS_KOR.md) 확인
- 전날 완료된 태스크 검토
- 다음 태스크 식별
- 태스크 상태 업데이트

**주간 계획:**
- 단계 진행 상황 검토
- 실제 소요 시간에 따라 예상치 조정
- 차단 요인 식별
- 다음 주 집중 영역 계획

### 프로젝트 관리용

**상태 표시:**
- 🔴 PENDING - 시작하지 않음
- 🟡 IN_PROGRESS - 현재 작업 중
- 🟢 COMPLETED - 완료 및 검증됨
- ⏸️ BLOCKED - 의존성 대기 중
- 🚧 ON_HOLD - 일시 중지됨

**태스크 상태 업데이트:**
1. 태스크 마크다운 파일 열기
2. 메타데이터의 `status` 필드 업데이트
3. README의 상태 아이콘 업데이트
4. [진행 상황 대시보드](./PROGRESS_KOR.md) 업데이트
5. 변경사항 커밋

---

## 📈 진행 상황 대시보드 링크

상세 지표, 타임라인 및 분석:

👉 **[전체 진행 상황 대시보드 보기](./PROGRESS_KOR.md)**

포함 내용:
- 단계별 세부 분석
- 태스크 완료 타임라인
- 노력 추적 (예상 vs 실제)
- 차단 요인 분석
- 속도 지표

---

## 🔗 관련 문서

### SPEC 참조
- [프로젝트 인덱스](../index_KOR.md)
- [SPEC 인덱스](../spec/README_KOR.md)
- [핵심 시스템 SPEC](../spec/05-core-systems/README_KOR.md)
- [핵심 기반 세부사항](../spec/05-core-systems/foundation/singleton_KOR.md)

### 개발 리소스
- [코딩 규칙](../../doc/guidelines/coding-conventions_KOR.md)
- [개발 워크플로우](../../doc/workflow/development-workflow_KOR.md)
- [문서화 규칙](../../doc/guidelines/documentation-rules_KOR.md)

### 도구
- [스코프 검증](../../../scripts/scope_validate.py)
- [문서 검증](../../../scripts/doc_validate.py)

---

## 📝 태스크 관리 가이드라인

### 태스크 생성
- **세분화**: 태스크당 15분 - 2시간
- **의존성**: 명확하게 지정됨
- **검증**: 측정 가능한 완료 기준
- **문서화**: 관련 SPEC에 링크

### 태스크 실행
- **한 번에 하나씩**: 단일 집중
- **체크리스트 기반**: 모든 단계 따르기
- **검증**: 완료 표시 전 테스트
- **문서화**: 진행하면서 업데이트

### 태스크 완료
- **모든 기준 충족**: 검증 건너뛰지 않기
- **테스트 통과**: 해당하는 경우
- **문서 업데이트됨**: 필요한 경우
- **커밋됨**: 적절한 메시지로 Git 커밋

---

**문서 상태**: Active
**관리자**: HaroFramework Team
**마지막 업데이트**: 2025-10-26
**현재 단계**: Phase 1 - 핵심 기반
**다음 태스크**: [CF-001: Singleton.cs](./phase1-core-foundation/phase-a-foundation/CF-001-singleton_KOR.md)
