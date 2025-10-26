---
title: HaroFramework 명세서
version: 2.0.0
scope: framework
created: 2025-10-25
modified: 2025-10-26
category: Project Management
tags: [specification, architecture, documentation]
paired_document: SPEC.md
parent_documents: []
child_documents: []
references: []
---


<!-- Navigation -->
**🏠 [HaroFramework Project](../../MASTER_INDEX_KOR.md)** | **📂 [HaroFramework 프로젝트 인덱스](INDEX_KOR.md)** | **⬆️ [HaroFramework 프로젝트 인덱스](INDEX_KOR.md)**

---
# HaroFramework 명세서

## 1. 프로젝트 비전

### 1.1 개요
HaroFramework는 다양한 장르의 게임 개발을 위한 기반으로 설계된 재사용 가능한 Unity 게임 프레임워크입니다. 이 프레임워크는 코드 품질과 일관성을 유지하면서 게임 개발을 가속화할 수 있는 핵심 시스템, 도구 및 패턴을 제공합니다.

### 1.2 목표
- **재사용성**: 여러 게임 프로젝트에서 사용할 수 있는 프레임워크 생성
- **확장성**: 특정 게임 요구사항에 맞게 쉽게 확장 가능한 시스템 설계
- **품질**: 포괄적인 테스트 및 문서화를 통한 높은 코드 품질 유지
- **성능**: 프로덕션 게임에 최적화된 성능 보장
- **개발자 경험**: 명확한 문서와 직관적인 API 제공

### 1.3 대상 사용 사례
- 액션 게임
- RPG 게임
- 퍼즐 게임
- 플랫포머
- 그 외 Unity 기반 게임 장르

---

## 2. 아키텍처

### 2.1 2-Scope 시스템

프로젝트는 프레임워크 관심사와 게임별 구현을 분리하기 위해 엄격한 2-Scope 아키텍처를 사용합니다:

#### Framework Scope (독립적)
- **목적**: 재사용 가능한 게임 시스템 및 유틸리티 제공
- **독립성**: 게임별 코드를 참조하거나 의존해서는 안 됨
- **위치**: `.claude/framework/`
- **범위**: 핵심 시스템, 도구, 유틸리티, 공통 패턴

#### Game Scope (프레임워크 의존)
- **목적**: 특정 게임 로직 및 콘텐츠 구현
- **의존성**: Framework Layer를 참조하고 사용 가능
- **위치**: `.claude/games/[game-name]/`
- **범위**: 게임별 메카닉, 콘텐츠, 디자인

#### 의존성 규칙
```
✅ 허용:   Game → Framework (게임이 프레임워크 사용)
❌ 금지: Framework → Game (프레임워크가 게임 인식 불가)
```

**근거**: 이는 프레임워크가 특정 게임 구현에 결합되지 않고 다양한 게임 프로젝트에서 재사용 가능하도록 보장합니다.

### 2.2 폴더 구조

```
.claude/
│
├── framework/                        # 🔵 Framework Scope (독립적)
│   ├── doc/                         # 프레임워크 문서
│   │   ├── guidelines/              # 개발 가이드라인
│   │   │   ├── documentation-rules.md
│   │   │   ├── documentation-rules_KOR.md
│   │   │   ├── coding-conventions.md
│   │   │   └── coding-conventions_KOR.md
│   │   │
│   │   ├── architecture/            # 아키텍처 문서
│   │   │   ├── project-overview.md
│   │   │   ├── project-overview_KOR.md
│   │   │   ├── scope-system.md
│   │   │   └── scope-system_KOR.md
│   │   │
│   │   ├── systems/                 # 핵심 시스템 문서
│   │   │   ├── player/
│   │   │   ├── ai/
│   │   │   ├── ui/
│   │   │   └── audio/
│   │   │
│   │   ├── api/                     # API 레퍼런스 (자동 생성)
│   │   │
│   │   └── workflow/                # 개발 워크플로우
│   │       ├── development-workflow.md
│   │       └── development-workflow_KOR.md
│   │
│   ├── project/                     # 프레임워크 프로젝트 관리
│   │   ├── SPEC.md                  # 이 파일의 영문 버전
│   │   ├── SPEC_KOR.md              # 이 파일
│   │   ├── TODO.md
│   │   └── TODO_KOR.md
│   │
│   └── scripts/                     # 프레임워크 전용 스크립트
│       └── README.md
│
├── games/                            # 🟢 Game Scope (프레임워크 의존)
│   ├── _template/                   # 새 게임 프로젝트 템플릿
│   │   ├── doc/
│   │   │   ├── design/              # 게임 디자인 문서
│   │   │   ├── mechanics/           # 게임플레이 메카닉
│   │   │   ├── levels/              # 레벨 문서
│   │   │   └── assets/              # 에셋 문서
│   │   ├── project/
│   │   │   ├── SPEC.md
│   │   │   ├── SPEC_KOR.md
│   │   │   ├── TODO.md
│   │   │   └── TODO_KOR.md
│   │   └── GAME.md                  # 게임별 Claude 설정
│   │
│   └── [game-name]/                 # 실제 게임 프로젝트 (향후)
│
├── scripts/                          # 🔧 공통 자동화 스크립트
│   ├── doc_sync.py                  # 문서 동기화
│   ├── doc_validate.py              # 링크/메타데이터 검증
│   ├── scope_validate.py            # 스코프 의존성 검증
│   ├── version_bump.py              # 버전 관리
│   └── README.md
│
├── CLAUDE.md                         # 프레임워크 작업 설정
└── README.md                         # 프로젝트 README
```

---

## 3. 문서화 시스템

### 3.1 문서 이중화 규칙

**모든 문서는 영어와 한국어로 이중화되어야 합니다.**

#### 파일 명명 규칙
- **원본문서**: `{문서}.md` (영어)
- **한글문서**: `{문서}_KOR.md` (한국어)

#### 예시
```
documentation-rules.md       → 원본 (영어)
documentation-rules_KOR.md   → 한글 번역

SPEC.md                      → 원본 (영어)
SPEC_KOR.md                  → 한글 번역
```

#### 동기화 규칙
1. **한글문서 언어**: 100% 한국어로 작성되어야 함
2. **내용 연결**: 두 문서는 동일한 내용을 유지해야 함
3. **업데이트 동기화**: 한 문서가 업데이트되면 쌍 문서도 함께 업데이트되어야 함
4. **구조 일관성**: 두 문서는 동일한 구조, 제목, 조직을 유지해야 함

### 3.2 메타데이터 표준

모든 문서는 파일 시작 부분에 YAML frontmatter 메타데이터를 포함해야 합니다.

#### 필수 필드
```yaml
---
title: "문서 제목"
version: "1.0.0"                    # Semantic versioning
scope: "framework|game"             # 스코프 분류
created: "2025-10-25"               # 생성일
modified: "2025-10-25"              # 최종 수정일
paired_document: "filename_KOR.md"  # 쌍 문서 참조
---
```

#### 선택 필드
```yaml
category: "카테고리"                # 문서 카테고리
tags: [tag1, tag2]                  # 검색 가능한 태그
status: "draft|review|approved"     # 문서 상태
parent_documents: []                # 상위 문서 링크
child_documents: []                 # 하위 문서 링크
references: []                      # 참조 문서
```

#### Scope 필드 값
- `framework`: 프레임워크 스코프 문서
- `game`: 게임 스코프 문서

**목적**: `scope` 필드는 금지된 크로스 스코프 참조를 방지하기 위한 자동 검증을 가능하게 합니다.

### 3.3 버전 관리

#### Semantic Versioning (MAJOR.MINOR.PATCH)

**MAJOR** - 다음의 경우 증가:
- 문서 구조가 크게 재구성됨
- 문서 형식이나 규칙에 파괴적 변경
- 문서화된 시스템의 근본적 변경
- 하위 호환성이 깨짐

**MINOR** - 다음의 경우 증가:
- 새로운 섹션이나 챕터가 추가됨
- 새로운 정보로 내용이 확장됨
- 새로운 기능이나 시스템이 문서화됨
- 하위 호환 가능한 추가

**PATCH** - 다음의 경우 증가:
- 오타나 문법 오류 수정
- 예제 개선이나 명확화
- 사소한 표현 개선
- 서식 수정

#### 버전 업데이트 프로세스
1. 변경 유형 결정 (MAJOR/MINOR/PATCH)
2. 메타데이터의 버전 업데이트
3. `modified` 날짜 업데이트
4. 쌍 문서 버전도 일치하도록 업데이트
5. CHANGELOG에 변경사항 문서화 (해당하는 경우)

#### 버전 관리 스크립트
`version_bump.py`를 사용하여 버전 업데이트 자동화:
```bash
python .claude/scripts/version_bump.py [문서] [major|minor|patch]
```

### 3.4 문서 작업 규칙

#### 읽기 최적화 (토큰 효율성)
**규칙**: Claude Code는 원본문서(*.md)만 읽고, 한글문서(*_KOR.md)는 읽지 않음

**근거**:
- 토큰 사용량을 약 50% 감소
- 원본 영어 문서에 모든 필요한 정보 포함
- 한글 문서는 한국어를 선호하는 사람을 위한 것

**구현**: 문서 읽기 도구와 프로세스는 `*_KOR.md` 파일을 제외해야 함.

#### Context 관리 프로토콜
**규칙**: Context 사용량이 85%에 도달하면 SPEC/TODO 작성 후 `/clear` 실행

**프로세스**:
1. 작업 중 Context 사용량 모니터링
2. 85% 임계치에서:
   - 현재 SPEC.md를 진행 상황으로 업데이트
   - 현재 TODO.md를 남은 작업으로 업데이트
   - 한글 쌍 문서도 업데이트
   - 세션 복원 가이드 제공
   - `/clear` 실행
3. 업데이트된 SPEC/TODO를 사용하여 새 세션에서 작업 재개

**근거**: Context 오버플로우를 방지하고 세션 간 연속성을 보장합니다.

#### Script 우선 접근
**규칙**: 반복 작업이 감지되면 사용자에게 스크립트 작성 제안

**스크립트화 가능한 작업 예시**:
- 문서 동기화 (doc_sync.py)
- 링크 검증 (doc_validate.py)
- 버전 증가 (version_bump.py)
- 메타데이터 검증
- 일괄 문서 작업

**이점**:
- 토큰 사용량 감소
- 일관성 보장
- 향후 작업 시간 절약
- 사람의 실수 감소

#### 폴더 구조 관리
**규칙**: Claude Code는 문서 작업 전에 적절한 폴더 구조 제안

**프로세스**:
1. 문서 목적과 카테고리 분석
2. 논리적 폴더 위치 제안
3. 사용자 승인 대기
4. 승인되면 폴더 생성
5. 구조 문서화

**근거**: 체계적이고 탐색 가능한 문서 구조를 유지합니다.

### 3.5 문서 링크 시스템

**규칙**: 관련 문서는 계층적으로 링크되어야 함

#### 링크 유형
- **부모-자식**: 계층적 관계 (개요 → 세부사항)
- **참조**: 관련 문서 간 상호 참조
- **참고**: 추가 컨텍스트를 위한 관련 문서

#### 메타데이터 링크
```yaml
parent_documents:
  - "../SPEC.md"
child_documents:
  - "systems/player.md"
  - "systems/ai.md"
references:
  - "../guidelines/coding-conventions.md"
```

#### 링크 검증
- `doc_validate.py`를 사용하여 모든 링크가 유효한지 확인
- 깨진 링크 감지
- 적절한 경우 양방향 링크 보장
- 스코프 경계가 존중되는지 확인

#### 스코프 인식 링크
```yaml
# 프레임워크 문서
references:
  - "./other-framework-doc.md"      # ✅ OK
  - "../../games/game1/design.md"   # ❌ 금지

# 게임 문서
references:
  - "../../framework/systems/player.md"  # ✅ OK
  - "./game-design.md"                   # ✅ OK
```

### 3.6 자동화 스크립트

#### doc_sync.py - 문서 동기화
**목적**: 원본 문서와 한글 문서 간 내용 동기화

**기능**:
- 원본 또는 한글 문서의 변경 감지
- 동기화가 필요할 때 알림
- 수동 동기화 워크플로우 지원
- 선택사항: 번역 API와 통합

**사용법**:
```bash
python .claude/scripts/doc_sync.py --check     # 동기화 상태 확인
python .claude/scripts/doc_sync.py --sync      # 수동 동기화 프롬프트
```

#### doc_validate.py - 문서 검증
**목적**: 문서 무결성 및 메타데이터 검증

**검사 항목**:
- 메타데이터 형식 및 필수 필드
- 쌍 문서 존재 여부
- 링크 무결성 (깨진 링크)
- 쌍 간 버전 일관성
- 상태 필드 유효성

**사용법**:
```bash
python .claude/scripts/doc_validate.py              # 전체 검증
python .claude/scripts/doc_validate.py [문서]       # 하나만 검증
```

#### scope_validate.py - 스코프 의존성 검증
**목적**: 스코프 의존성 규칙 강제

**검증 항목**:
- 문서 메타데이터에서 `scope` 필드 추출
- 모든 링크와 참조 파싱
- 프레임워크 문서가 게임 문서를 참조하지 않는지 확인
- 파일 및 라인 정보와 함께 위반 사항 보고

**알고리즘**:
```python
def validate_layer_dependency(doc_path):
    scope = get_document_layer(doc_path)
    references = extract_all_references(doc_path)

    for ref in references:
        ref_layer = get_document_layer(ref)

        if scope == "framework" and ref_layer == "game":
            raise DependencyViolationError(
                f"금지: 프레임워크 문서 '{doc_path}'는 "
                f"게임 문서 '{ref}'를 참조할 수 없습니다"
            )

    return True
```

**사용법**:
```bash
python .claude/scripts/scope_validate.py              # 전체 검증
python .claude/scripts/scope_validate.py [문서]       # 하나만 검증
```

#### version_bump.py - 버전 관리
**목적**: 버전 업데이트 자동화

**기능**:
- 버전 증가 (major/minor/patch)
- `modified` 날짜 자동 업데이트
- 쌍 문서 버전 업데이트
- CHANGELOG 항목 생성 (선택사항)

**사용법**:
```bash
python .claude/scripts/version_bump.py [문서] major
python .claude/scripts/version_bump.py [문서] minor
python .claude/scripts/version_bump.py [문서] patch
```

---

## 4. 스코프 의존성 규칙

### 4.1 절대 규칙

#### ❌ 금지: Framework → Game
프레임워크 스코프는 절대로:
- 게임별 코드를 임포트하거나 참조해서는 안 됨
- 게임 문서에 링크해서는 안 됨
- 게임별 로직이나 콘텐츠를 포함해서는 안 됨
- 게임 프로젝트의 존재를 알아서는 안 됨

**이유**: 프레임워크는 모든 게임 프로젝트에서 재사용 가능해야 합니다.

#### ✅ 허용: Game → Framework
게임 스코프는:
- 프레임워크 시스템을 임포트하고 사용할 수 있음
- 프레임워크 문서를 참조할 수 있음
- 프레임워크 클래스를 확장할 수 있음
- 프레임워크 유틸리티를 활용할 수 있음

**이유**: 게임은 프레임워크를 활용하도록 설계되었습니다.

### 4.2 검증 방법

#### 메타데이터 기반 검증
모든 문서는 자신의 스코프를 선언합니다:
```yaml
scope: framework  # 또는 "game"
```

검증 스크립트가 확인:
1. 문서의 선언된 스코프
2. 모든 참조된 문서의 스코프
3. 강제: `framework`는 `game`을 참조할 수 없음

#### 지속적 검증
- 커밋 전에 `scope_validate.py` 실행
- CI/CD 파이프라인에 통합 (향후)
- 문서 작업 중 자동 검사

#### 수동 검토
- 코드 리뷰 체크리스트에 스코프 확인 포함
- 아키텍처 리뷰에서 스코프 경계 검사
- 문서 리뷰에서 적절한 분류 확인

---

## 5. 핵심 프레임워크 시스템

### 5.1 프레임워크 아키텍처 (6계층 시스템)

프레임워크는 명확한 관심사 분리와 의존성 규칙을 가진 엄격한 6계층 아키텍처를 구현합니다.

```
┌─────────────────────────────────────────────────────────┐
│                    Gameplay Layer                        │
│                   (게임플레이 영역)                        │
│  - MonoBehaviour 기반 게임 오브젝트                        │
│  - 실제 게임 로직 (Player, Enemy, UI 등)                  │
│  - BaseGameplay 상속                                     │
└─────────────────────────────────────────────────────────┘
                         ↓ 사용
┌─────────────────────────────────────────────────────────┐
│                     Service Layer                        │
│                    (서비스 영역)                          │
│  - 게임 특화 기능 구현                                     │
│  - Interface 구체 구현                                    │
│  - BaseService 상속                                      │
└─────────────────────────────────────────────────────────┘
                         ↓ 구현
┌─────────────────────────────────────────────────────────┐
│                   Interface Layer                        │
│                  (인터페이스 영역)                         │
│  - 게임 특화 계약 정의                                     │
│  - IService 인터페이스                                    │
│  - 의존성 역전 (DIP) 적용                                 │
└─────────────────────────────────────────────────────────┘
                         ↓ 참조
┌─────────────────────────────────────────────────────────┐
│                      Core Layer                          │
│                     (코어 영역)                           │
│  - 범용 모듈 (UI, Audio, Scene, Network)                 │
│  - BaseModule 상속                                       │
│  - 게임 독립적 (모든 프로젝트 공통)                         │
└─────────────────────────────────────────────────────────┘
       ↓ 사용                                  ↑ 접근
┌──────────────────────┐      ┌──────────────────────────┐
│    Domain Layer      │      │      Data Layer          │
│   (도메인 영역)       │←─────│     (데이터 영역)         │
│  - 데이터 가공/계산   │ 접근 │  - 순수 데이터 구조       │
│  - 게임 룰 적용       │      │  - BaseData 상속         │
│  - BaseDomain 상속    │      │  - 직렬화 가능           │
└──────────────────────┘      └──────────────────────────┘
```

#### 의존성 흐름
```
Gameplay → Service → Interface → Core
   ↓          ↓
   └─→ Domain ←─┘
          ↓
        Data
```

**원칙**:
- 상위 계층은 하위 계층을 참조 가능
- 하위 계층은 상위 계층을 참조 불가
- Data 계층은 모든 계층에서 접근 가능 (읽기만)

#### 통신 방식
```
1. 직접 참조 (Direct Reference)
   Gameplay → Service
   Service → Domain
   Domain → Data

2. 이벤트 버스 (Event Bus)
   모든 계층 ↔ 모든 계층
   - 느슨한 결합
   - 비동기 처리

3. 서비스 로케이터 (Service Locator)
   Gameplay/Service → 등록된 Service
   - 중앙 집중 관리
   - 런타임 해결
```

### 5.2 계층별 상세

#### 5.2.1 Data Layer (데이터 계층)

**목적**:
- 순수 데이터 구조 정의
- 직렬화/역직렬화 지원
- 게임 로직 배제

**구조**:
```csharp
// 필수 구현: BaseData 상속
public abstract class BaseData
{
    public int Id { get; set; }

    // 모든 데이터는 검증 로직 제공
    public abstract bool Validate();
}
```

**규칙**:
1. **로직 금지**: 데이터 저장/표현만 담당
2. **불변성**: 가능한 읽기 전용 속성 사용
3. **직렬화**: `[System.Serializable]` 속성 필수
4. **명명 규칙**: `{Entity}Data` (예: `PlayerData`, `ItemData`)

**예시**:
```csharp
[System.Serializable]
public class ItemData : BaseData
{
    public string Name;
    public int BaseAttack;
    public float BaseCritRate;
    public ItemType Type;

    public override bool Validate()
    {
        return !string.IsNullOrEmpty(Name) && BaseAttack >= 0;
    }
}
```

**위치**: `Assets/Data/Base/` (BaseData), `Assets/Data/Game/` (게임별)

---

#### 5.2.2 Domain Layer (도메인 계층)

**목적**:
- Raw Data 가공 및 변환
- 게임 계산식 적용 (스탯, 데미지, 확률 등)
- 데이터 캐싱 및 최적화
- 비즈니스 룰 구현

**구조**:
```csharp
// 필수 구현: BaseDomain<TData> 상속
public abstract class BaseDomain<TData> where TData : BaseData
{
    public abstract string DomainName { get; }

    // 데이터 로드 → 가공 → 캐싱
    public abstract void LoadData();

    // ID로 데이터 조회
    public abstract TData GetData(int id);

    // 전체 데이터 조회
    public abstract IEnumerable<TData> GetAllData();
}
```

**규칙**:
1. **데이터 중심**: Data를 읽고 가공만 수행
2. **상태 비저장**: 게임 상태를 Domain에 저장 금지
3. **캐싱 활용**: 반복 계산 방지
4. **명명 규칙**: `{Entity}Domain` (예: `ItemDomain`, `PlayerStatsDomain`)

**예시**:
```csharp
public class ItemDomain : BaseDomain<ItemData>
{
    public override string DomainName => "Item";

    private Dictionary<int, ItemData> itemCache = new Dictionary<int, ItemData>();

    public override void LoadData()
    {
        // JSON/CSV에서 로드
        var json = Resources.Load<TextAsset>("Data/Items");
        var itemList = JsonUtility.FromJson<ItemDataList>(json.text);

        foreach (var item in itemList.items)
        {
            // 게임 룰 적용
            item.FinalAttack = CalculateFinalAttack(item);
            itemCache[item.Id] = item;
        }
    }

    private int CalculateFinalAttack(ItemData item)
    {
        return item.BaseAttack + (item.Level * 5);
    }
}
```

**위치**: `Assets/Scripts/Domain/Base/` (BaseDomain), `Assets/Scripts/Domain/{GameName}/` (게임별)

---

#### 5.2.3 Core Layer (코어 계층)

**목적**:
- 게임 독립적인 범용 모듈 제공
- 모듈 생명주기 관리
- 프레임워크 기반 시스템 제공

**구조**:
```csharp
// 필수 구현: BaseModule 상속
public abstract class BaseModule : IModule
{
    public abstract string ModuleName { get; }
    public abstract int Priority { get; }

    // 생명주기 메서드
    public void Initialize();
    public void Shutdown();
    public void OnUpdate();
}
```

**기본 제공 모듈**:

| 모듈 | 책임 | 우선순위 |
|--------|------|----------|
| **DataModule** | 데이터 로드/저장 | 5 |
| **UIModule** | UI 캔버스 관리 | 10 |
| **SceneModule** | 씬 전환 관리 | 15 |
| **AudioModule** | BGM/SFX 재생 | 20 |
| **NetworkModule** | 네트워크 통신 | 25 |

**규칙**:
1. **게임 독립성**: 특정 게임 로직 포함 금지
2. **독립 동작**: 다른 모듈에 의존하지 않음
3. **선택적 활성화**: Config에서 On/Off 가능
4. **명명 규칙**: `{Feature}Module` (예: `UIModule`, `AudioModule`)

**위치**: `Assets/Framework/Core/Modules/`

---

#### 5.2.4 Interface Layer (인터페이스 계층)

**목적**:
- 게임 특화 계약 정의
- 의존성 역전 (DIP) 적용
- Service 구현 강제

**구조**:
```csharp
// 필수 구현: IService 상속
public interface IService
{
    string ServiceName { get; }
    void Initialize();
    void Dispose();
}

// 게임 특화 인터페이스
public interface IInventorySystem : IService
{
    bool AddItem(int itemId, int count);
    bool RemoveItem(int itemId, int count);
    ItemData GetItem(int itemId);
}
```

**규칙**:
1. **계약 정의**: 구현 세부사항 배제
2. **IService 상속**: 모든 인터페이스는 IService 구현
3. **명명 규칙**: `I{System}System` (예: `IInventorySystem`, `IBattleSystem`)

**위치**: `Assets/Scripts/Interface/`

---

#### 5.2.5 Service Layer (서비스 계층)

**목적**:
- Interface 구체 구현
- 게임 비즈니스 로직 처리
- Core 모듈 + Domain 조합 활용

**구조**:
```csharp
// 필수 구현: BaseService 상속 + Interface 구현
public abstract class BaseService : IService
{
    public abstract string ServiceName { get; }

    protected EventBus EventBus { get; }
    protected ServiceLocator Services { get; }

    public virtual void Initialize();
    public virtual void Dispose();
}
```

**규칙**:
1. **Interface 구현**: 반드시 Interface 정의 후 구현
2. **BaseService 상속**: 생명주기 통일
3. **상태 관리**: 게임 상태를 Service에서 관리
4. **이벤트 발행**: 상태 변경 시 이벤트 Publish
5. **명명 규칙**: `{System}Service` (예: `InventoryService`, `BattleService`)

**예시**:
```csharp
public class InventoryService : BaseService, IInventorySystem
{
    public override string ServiceName => "Inventory";

    private ItemDomain itemDomain;
    private Dictionary<int, int> inventory = new Dictionary<int, int>();

    protected override void InitializeService()
    {
        itemDomain = DataManager.Instance.GetDomain<ItemDomain>();
    }

    public bool AddItem(int itemId, int count)
    {
        var itemData = itemDomain.GetData(itemId);
        if (itemData == null) return false;

        if (!inventory.ContainsKey(itemId))
            inventory[itemId] = 0;

        inventory[itemId] += count;

        EventBus.Publish(new ItemAddedEvent
        {
            ItemId = itemId,
            Count = count
        });

        return true;
    }
}
```

**위치**: `Assets/Scripts/Service/Base/` (BaseService), `Assets/Scripts/Service/{GameName}/` (게임별)

---

#### 5.2.6 Gameplay Layer (게임플레이 계층)

**목적**:
- 실제 게임 로직 구현
- MonoBehaviour 기반
- Service 조합 활용

**구조**:
```csharp
// 필수 구현: BaseGameplay 상속
public abstract class BaseGameplay : MonoBehaviour
{
    protected ServiceLocator Services { get; }
    protected EventBus EventBus { get; }

    // Unity 생명주기와 통합
    protected virtual void Awake() { }
    protected virtual void Start() { }
    protected virtual void OnDestroy() { }

    // 프레임워크 생명주기
    protected abstract void RegisterServices();
    protected abstract void SubscribeEvents();
    protected abstract void UnsubscribeEvents();
}
```

**규칙**:
1. **BaseGameplay 상속**: 생명주기 통일
2. **Service 사용**: 직접 로직 구현 금지, Service 호출
3. **이벤트 구독**: 필요한 이벤트만 구독
4. **명명 규칙**: `{Entity}Controller` (예: `PlayerController`, `EnemyController`)

**위치**: `Assets/Scripts/Gameplay/Base/` (BaseGameplay), `Assets/Scripts/Gameplay/{GameName}/` (게임별)

### 5.3 핵심 시스템

#### 5.3.1 EventBus (이벤트 버스)

**목적**:
- 계층 간 느슨한 결합
- 비동기 통신
- 이벤트 기반 아키텍처

**인터페이스**:
```csharp
public interface IGameEvent { }

public class EventBus : Singleton<EventBus>
{
    // 이벤트 구독
    public void Subscribe<T>(Action<T> handler) where T : IGameEvent;

    // 이벤트 구독 해제
    public void Unsubscribe<T>(Action<T> handler) where T : IGameEvent;

    // 이벤트 발행
    public void Publish<T>(T gameEvent) where T : IGameEvent;
}
```

**사용 규칙**:
1. **이벤트 정의**: IGameEvent 구현
2. **명명 규칙**: `{Action}{Entity}Event` (예: `ItemAddedEvent`, `PlayerDamagedEvent`)
3. **데이터 포함**: 필요한 정보만 최소한으로
4. **불변 권장**: readonly 필드 사용

**위치**: `Assets/Framework/Core/Systems/EventBus.cs`

---

#### 5.3.2 ServiceLocator (서비스 로케이터)

**목적**:
- 서비스 중앙 관리
- 런타임 의존성 해결
- 전역 접근 제공

**인터페이스**:
```csharp
public class ServiceLocator : Singleton<ServiceLocator>
{
    // 서비스 등록
    public void Register<T>(T service) where T : IService;

    // 서비스 조회
    public T Get<T>() where T : IService;

    // 서비스 존재 확인
    public bool Has<T>() where T : IService;

    // 모든 서비스 정리
    public void Clear();
}
```

**사용 규칙**:
1. **초기화 시점**: 게임 시작 시 모든 Service 등록
2. **단일 인스턴스**: 하나의 Service는 한 번만 등록
3. **타입 기반**: Interface 타입으로 등록/조회

**위치**: `Assets/Framework/Core/Systems/ServiceLocator.cs`

---

#### 5.3.3 DataManager (데이터 관리자)

**목적**:
- Domain 중앙 관리
- 데이터 로딩 통합
- Domain 접근 제공

**인터페이스**:
```csharp
public class DataManager : Singleton<DataManager>
{
    // Domain 등록
    public void RegisterDomain<TDomain, TData>(TDomain domain)
        where TDomain : BaseDomain<TData>
        where TData : BaseData;

    // Domain 조회
    public TDomain GetDomain<TDomain>() where TDomain : class;

    // 모든 Domain 로드
    public void LoadAllDomains();
}
```

**위치**: `Assets/Framework/Core/Systems/DataManager.cs`

### 5.4 생명주기 관리

#### 초기화 흐름
```
[Application Start]
       ↓
┌─────────────────┐
│ FrameworkManager│
│    .Awake()     │
└─────────────────┘
       ↓
┌─────────────────┐
│  Core Systems   │
│  - EventBus     │
│  - ServiceLocator│
│  - DataManager  │
└─────────────────┘
       ↓
┌─────────────────┐
│ Modules Init    │
│ (Priority 순서)  │
└─────────────────┘
       ↓
┌─────────────────┐
│ Domain LoadData │
└─────────────────┘
       ↓
┌─────────────────┐
│Services Register│
└─────────────────┘
       ↓
┌─────────────────┐
│ Scene Load      │
└─────────────────┘
       ↓
┌─────────────────┐
│Gameplay Init    │
└─────────────────┘
       ↓
   [Game Ready]
```

#### 종료 흐름
```
[Application Quit]
       ↓
┌─────────────────┐
│ Gameplay        │
│  .OnDestroy()   │
└─────────────────┘
       ↓
┌─────────────────┐
│ Services        │
│  .Dispose()     │
└─────────────────┘
       ↓
┌─────────────────┐
│ Modules         │
│  .Shutdown()    │
│  (역순)          │
└─────────────────┘
       ↓
   [Clean Exit]
```

#### 모듈 우선순위 시스템
- **DataModule**: Priority 5 (첫 번째 초기화)
- **UIModule**: Priority 10
- **SceneModule**: Priority 15
- **AudioModule**: Priority 20
- **NetworkModule**: Priority 25 (마지막 초기화)
- **종료**: 역순 (25 → 20 → 15 → 10 → 5)

### 5.5 폴더 구조 템플릿

```
Assets/
├── Framework/                  # 공통 (재사용)
│   ├── Core/
│   │   ├── Base/
│   │   │   ├── IModule.cs
│   │   │   ├── IService.cs
│   │   │   ├── BaseModule.cs
│   │   │   ├── BaseService.cs
│   │   │   ├── BaseDomain.cs
│   │   │   └── BaseGameplay.cs
│   │   ├── Modules/
│   │   │   ├── UIModule.cs
│   │   │   ├── AudioModule.cs
│   │   │   ├── SceneModule.cs
│   │   │   └── NetworkModule.cs
│   │   ├── Systems/
│   │   │   ├── EventBus.cs
│   │   │   ├── ServiceLocator.cs
│   │   │   ├── DataManager.cs
│   │   │   └── FrameworkLogger.cs
│   │   ├── FrameworkManager.cs
│   │   └── FrameworkConfig.cs
│   └── Data/
│       └── Base/
│           └── BaseData.cs
│
├── Data/                       # 게임 데이터
│   ├── Json/
│   │   ├── Items.json
│   │   └── Stages.json
│   └── CSV/
│       └── Monsters.csv
│
└── Scripts/                    # 게임 특화
    ├── {GameName}/
    │   ├── Data/
    │   │   ├── ItemData.cs
    │   │   ├── PlayerData.cs
    │   │   └── StageData.cs
    │   ├── Domain/
    │   │   ├── ItemDomain.cs
    │   │   ├── PlayerStatsDomain.cs
    │   │   └── StageDomain.cs
    │   ├── Interface/
    │   │   ├── IInventorySystem.cs
    │   │   ├── IBattleSystem.cs
    │   │   └── IQuestSystem.cs
    │   ├── Service/
    │   │   ├── InventoryService.cs
    │   │   ├── BattleService.cs
    │   │   └── QuestService.cs
    │   └── Gameplay/
    │       ├── Player/
    │       │   └── PlayerController.cs
    │       ├── Enemy/
    │       │   └── EnemyAI.cs
    │       └── Stage/
    │           └── StageManager.cs
    │
    └── Common/                 # 게임 공통
        ├── Events/
        │   ├── ItemAddedEvent.cs
        │   ├── PlayerDamagedEvent.cs
        │   └── StageCompletedEvent.cs
        └── Utilities/
            └── Singleton.cs
```

### 5.6 명명 규칙

| 계층 | 접미사 | 예시 |
|------|--------|------|
| Data | Data | `ItemData`, `PlayerData` |
| Domain | Domain | `ItemDomain`, `StatsDomain` |
| Interface | System | `IInventorySystem`, `IBattleSystem` |
| Service | Service | `InventoryService`, `BattleService` |
| Gameplay | Controller / Manager | `PlayerController`, `StageManager` |
| Event | Event | `ItemAddedEvent`, `StageCompletedEvent` |
| Module | Module | `UIModule`, `AudioModule` |

### 5.7 시스템 문서화 요구사항

각 핵심 시스템은 다음을 포함해야 합니다:
- 아키텍처 개요
- API 레퍼런스
- 사용 예제
- 통합 가이드
- 모범 사례

위치: `.claude/framework/doc/systems/[카테고리]/`

---

## 6. 품질 기준

### 6.1 코드 품질

#### 문서화 요구사항
- **XML 문서화**: 모든 공개 API는 XML 문서화 주석을 가져야 함
- **코드 주석**: 복잡한 알고리즘과 명확하지 않은 로직은 주석 처리되어야 함
- **README 파일**: 각 시스템은 목적과 사용법을 설명하는 README를 가져야 함

#### 테스트 요구사항
- **단위 테스트**: 모든 핵심 로직은 단위 테스트를 가져야 함
- **통합 테스트**: 시스템 간 상호작용은 테스트되어야 함
- **커버리지**: 중요 시스템에서 >80% 코드 커버리지 목표

#### 코드 표준
- `.claude/framework/doc/guidelines/coding-conventions.md` 준수
- 모든 린터 규칙 통과
- 컴파일러 경고 없음
- 성능을 고려한 구현

### 6.2 문서 품질

#### 완전성
- 모든 필수 메타데이터 필드 존재
- 모든 섹션이 적절히 문서화됨
- 적절한 경우 예제 포함
- 관련 문서에 링크

#### 정확성
- 내용이 구현과 일치
- 예제가 테스트되고 작동함
- 버전 정보가 최신임
- 오래된 정보 없음

#### 일관성
- documentation-rules.md 준수
- 일관된 용어 사용
- 일관된 서식
- 이중 언어 문서 동기화

### 6.3 검증 요구사항

모든 문서는 다음을 통과해야 합니다:
- ✅ `doc_validate.py` - 메타데이터 및 링크 검증
- ✅ `scope_validate.py` - 스코프 의존성 검증
- ✅ 쌍 문서 존재 및 동기화
- ✅ 모든 링크가 유효하고 접근 가능

---

## 7. 기술 스택

### 7.1 Unity 환경
- **Unity 버전**: 6000.2.9f1 (Unity 6)
- **렌더 파이프라인**: Universal Render Pipeline (URP) 17.2.0
- **입력 시스템**: New Input System 1.14.2
- **대상 플랫폼**: PC, 콘솔 (향후: 모바일)

### 7.2 개발 도구
- **IDE**: Visual Studio / Rider
- **버전 관리**: Git
- **문서화**: Markdown
- **스크립팅**: C# (Unity), Python (자동화)

### 7.3 프레임워크 의존성
- 외부 의존성 최소화
- 가능한 Unity 내장 패키지 사용
- 모든 서드파티 패키지 문서화
- 의존성 추가 정당화

---

## 8. 개발 워크플로우

### 8.1 프레임워크 개발 프로세스

1. **계획**: SPEC에서 시스템 요구사항 정의
2. **설계**: 아키텍처 및 API 문서화
3. **구현**: 규칙을 따라 코드 작성
4. **테스트**: 포괄적인 테스트 생성
5. **문서화**: 시스템 문서 작성
6. **검토**: 코드 및 문서 리뷰
7. **통합**: 프레임워크에 병합
8. **검증**: 모든 검증 스크립트 실행

### 8.2 문서화 워크플로우

1. **생성**: 원본 문서 작성 (*.md)
2. **번역**: 한글 문서 생성 (*_KOR.md)
3. **메타데이터**: 필수 frontmatter 추가
4. **링크**: 관련 문서 연결
5. **검증**: 검증 스크립트 실행
6. **검토**: 동료 검토
7. **승인**: 승인됨으로 표시
8. **유지**: 변경사항과 동기화 유지

### 8.3 세션 관리

Context 사용량이 85%에 근접할 때:
1. SPEC.md를 현재 진행 상황으로 업데이트
2. TODO.md를 남은 작업으로 업데이트
3. 한글 문서 동기화
4. 세션 복원 가이드 생성
5. `/clear` 실행
6. 업데이트된 컨텍스트로 새 세션에서 재개

---

## 9. 성공 기준

### 9.1 프레임워크 목표
- ✅ 모든 핵심 시스템 구현 및 문서화
- ✅ 포괄적인 테스트 커버리지 (>80%)
- ✅ 완전한 API 문서화
- ✅ 프레임워크를 사용하여 최소 하나의 게임 성공적 빌드

### 9.2 문서화 목표
- ✅ 모든 문서 이중 언어 (영어 + 한국어)
- ✅ 모든 문서 검증 통과
- ✅ 깨진 링크 제로
- ✅ 모든 스코프 의존성 준수

### 9.3 품질 목표
- ✅ 컴파일러 경고 없음
- ✅ 모든 테스트 통과
- ✅ 성능 목표 달성
- ✅ 코드 리뷰 표준 충족

---

## 10. 향후 고려사항

### 10.1 계획된 기능
- 멀티플스코프 프레임워크 기반
- 고급 AI 유틸리티
- 절차적 생성 도구
- 모바일 플랫폼 지원

### 10.2 문서화 발전
- API 레퍼런스 자동 생성
- 인터랙티브 문서화
- 비디오 튜토리얼
- 커뮤니티 기여

### 10.3 도구 개선
- 자동 번역 통합
- 검증을 위한 CI/CD 파이프라인
- 문서화 웹사이트
- 코드 생성 도구

---

## 부록 A: 용어집

**Framework Scope**: 재사용 가능한, 게임에 구애받지 않는 기반 스코프
**Game Scope**: 프레임워크를 사용하는 게임별 구현
**원본문서**: 영어 .md 파일
**한글문서**: 한국어 _KOR.md 파일
**문서 이중화**: 이중 언어 문서화 시스템
**스코프 검증**: 의존성 규칙의 자동 검사
**쌍 문서**: 문서의 해당 번역

---

## 부록 B: 빠른 참조

### 필수 명령어
```bash
# 검증
python .claude/scripts/scope_validate.py
python .claude/scripts/doc_validate.py

# 문서화
python .claude/scripts/doc_sync.py --check
python .claude/scripts/version_bump.py [파일] [major|minor|patch]
```

### 폴더 위치
- 프레임워크 문서: `.claude/framework/doc/`
- 프레임워크 SPEC/TODO: `.claude/framework/project/`
- 게임 템플릿: `.claude/games/_template/`
- 스크립트: `.claude/scripts/`

### 중요 파일
- 프레임워크 Spec: `.claude/framework/project/SPEC.md`
- 프레임워크 TODO: `.claude/framework/project/TODO.md`
- Claude 설정: `CLAUDE.md`
- 코딩 규칙: `.claude/framework/doc/guidelines/coding-conventions.md`
- 문서화 규칙: `.claude/framework/doc/guidelines/documentation-rules.md`

---

**문서 상태**: 초안
**다음 검토 날짜**: 미정
**관리자**: HaroFramework Team
