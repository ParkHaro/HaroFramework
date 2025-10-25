---
title: "스킬 가이드"
version: "1.0.0"
layer: "framework"
created: "2025-10-25"
modified: "2025-10-25"
category: "Workflow"
tags: [skills, automation, tools, reference, ai]
paired_document: "skills-guide.md"
parent_documents:
  - "../../project/SPEC_KOR.md"
child_documents: []
references:
  - "./commands-guide_KOR.md"
  - "./development-workflow_KOR.md"
  - "../guidelines/coding-conventions_KOR.md"
status: "approved"
---

# 스킬 가이드

스킬은 Claude가 컨텍스트를 기반으로 자동으로 활성화하는 **모델 호출** 기능입니다.

## 스킬이란?

수동으로 호출하는 슬래시 명령과 달리, 스킬은:
- **자동**: Claude가 사용 시기를 결정
- **컨텍스트 인식**: 자연어 요청을 기반으로 활성화
- **전문화**: 각 스킬은 해당 도메인의 전문가
- **프로덕션 준비**: 고품질의 완전한 코드 생성

## 사용 가능한 스킬

### 🎮 unity-component

**목적**: 잘 구조화된 Unity MonoBehaviour 컴포넌트를 생성합니다.

**다음을 요청할 때 자동 활성화:**
- 플레이어 컨트롤러
- 적 AI 스크립트
- 게임 매니저
- UI 컨트롤러
- 게임플레이 메커니즘
- 컴포넌트 기반 시스템

**이 스킬을 트리거하는 예시:**
- "Create a player movement controller"
- "I need a health system"
- "Build an enemy AI component"
- "Make a game manager singleton"

**생성된 코드 포함:**
- 적절한 네임스페이스 구성
- Unity 생명주기 메서드 (Awake, Start, Update 등)
- 툴팁이 있는 직렬화된 필드
- 영역 구성
- XML 문서화
- 성능 모범 사례
- Unity 6 호환성

---

### 📦 unity-scriptable

**목적**: 데이터 중심 디자인을 위한 Unity ScriptableObject를 생성합니다.

**다음을 요청할 때 자동 활성화:**
- 게임 구성 데이터
- 이벤트 시스템
- 아이템 정의
- 캐릭터 스탯
- 공유 데이터 에셋
- 설정 관리

**이 스킬을 트리거하는 예시:**
- "Create a game settings ScriptableObject"
- "I need a weapon data asset"
- "Build an event system"
- "Make a character stats data structure"

**생성된 코드 포함:**
- CreateAssetMenu 속성
- 데이터 무결성을 위한 OnValidate
- 적절한 네임스페이스 (HaroFramework.Data)
- Inspector 구성
- XML 문서화
- 사용 예시

---

### 🛠️ unity-editor

**목적**: Unity Editor 확장 및 커스텀 도구를 생성합니다.

**다음을 요청할 때 자동 활성화:**
- 커스텀 인스펙터
- 프로퍼티 드로어
- 에디터 윈도우
- 메뉴 아이템
- 씬 뷰 도구
- 에셋 프로세서

**이 스킬을 트리거하는 예시:**
- "Create a custom inspector for GameManager"
- "I need a property drawer for my struct"
- "Build an editor window for level management"
- "Add a menu item to create prefabs"

**생성된 코드 포함:**
- Custom Editor 클래스
- 프로퍼티 드로어 구현
- 에디터 윈도우 레이아웃
- Undo/Redo 지원
- 멀티 오브젝트 편집 지원
- Scene GUI 통합

---

### ✅ unity-testing

**목적**: Unity Test Framework 테스트를 생성합니다.

**다음을 요청할 때 자동 활성화:**
- 단위 테스트
- 통합 테스트
- PlayMode 테스트
- EditMode 테스트
- Test-Driven Development 설정
- 테스트 커버리지

**이 스킬을 트리거하는 예시:**
- "Write tests for the PlayerController"
- "Create unit tests for the damage system"
- "I need PlayMode tests for scene loading"
- "Set up TDD for this feature"

**생성된 코드 포함:**
- 테스트 어셈블리 정의
- EditMode 및 PlayMode 테스트
- AAA 패턴 (Arrange, Act, Assert)
- 테스트 헬퍼 및 유틸리티
- 성능 테스트
- 적절한 테스트 명명 규칙

---

### 🎨 unity-shader

**목적**: Universal Render Pipeline을 위한 Unity 셰이더를 생성합니다.

**다음을 요청할 때 자동 활성화:**
- 비주얼 이펙트
- 커스텀 셰이더
- Shader Graph 생성
- 머티리얼 이펙트
- 포스트 프로세싱
- 렌더링 최적화

**이 스킬을 트리거하는 예시:**
- "Create a dissolve shader effect"
- "I need a hologram shader"
- "Build a water shader for URP"
- "Make a toon shading effect"

**생성된 코드 포함:**
- URP 호환 셰이더
- Shader Graph 설정
- HLSL 커스텀 함수
- 적절한 조명 통합
- 그림자 지원
- 성능 최적화

---

## 스킬 활성화 방법

스킬은 **description** 필드를 사용하여 활성화 시기를 결정합니다. Claude는 요청을 분석하고 스킬 설명과 일치시킵니다.

### 활성화 흐름

```
사용자: "Create a player health system"
    ↓
Claude가 요청 분석
    ↓
일치: unity-component 스킬
    ↓
스킬 지침 로드
    ↓
MonoBehaviour 컴포넌트 생성
    ↓
프로덕션 준비 코드 반환
```

## 스킬 vs 명령 비교

| 기능 | 스킬 | 슬래시 명령 |
|------|------|------------|
| **호출** | Claude가 자동 | 사용자가 수동 (`/cmd`) |
| **사용** | 자연어 | 명시적 명령 |
| **유연성** | 높음 - 컨텍스트에 적응 | 고정 - 특정 작업 |
| **발견** | AI 기반 | 사용자가 명령을 알아야 함 |
| **최적** | 복잡하고 컨텍스트가 있는 작업 | 빠르고 특정한 작업 |

### 예시 비교

**플레이어 컨트롤러를 만들고 싶을 때:**

**스킬 사용 (권장):**
```
"I need a player controller with movement and jumping"
→ Claude가 unity-component 스킬 사용
→ 요구사항이 포함된 완전한 컨트롤러 생성
```

**명령 사용 (대안):**
```
/component PlayerController HaroFramework.Player
→ 기본 컴포넌트 템플릿 생성
→ 추가 요구사항은 별도로 지정
```

## 스킬 파일 구조

각 스킬은 `.claude/skills/`의 디렉토리에 다음을 포함합니다:

```
.claude/skills/
└── skill-name/
    ├── SKILL.md           # 필수: 주요 지침
    ├── reference.md       # 선택: 참조 문서
    ├── examples.md        # 선택: 코드 예시
    ├── scripts/           # 선택: 헬퍼 스크립트
    └── templates/         # 선택: 코드 템플릿
```

### SKILL.md 형식

```markdown
---
name: skill-name
description: 이 스킬이 무엇을 하는지, Claude가 언제 사용해야 하는지. 활성화에 중요!
allowed-tools: Read, Write, Edit, Glob, Grep
---

# Skill Name

## When to Use This Skill

자세한 활성화 기준...

## Instructions

Claude를 위한 단계별 지침...

## Best Practices

가이드라인 및 표준...

## Output Format

예상 출력 구조...
```

## 커스텀 스킬 생성

### 1. 디렉토리 구조 생성
```bash
mkdir -p .claude/skills/my-skill
```

### 2. SKILL.md 생성

**좋은 설명 (안정적으로 활성화):**
```yaml
description: Create inventory systems with item management, storage, and UI integration. Use when implementing item collection, equipment, or crafting systems.
```

**나쁜 설명 (활성화되지 않음):**
```yaml
description: Inventory stuff
```

### 3. 명확한 지침 작성

포함 사항:
- 활성화 시기
- 생성할 내용
- 따라야 할 코드 표준
- 예시 및 패턴
- 출력 형식 기대사항

### 4. 활성화 테스트

스킬을 트리거해야 하는 자연어 요청을 시도:
- "Create an inventory system"
- "I need item management"
- "Build a crafting system"

## 모범 사례

### 스킬 설명
1. **"What" 포함**: 이 스킬이 무엇을 하는가?
2. **"When" 포함**: Claude가 언제 사용해야 하는가?
3. **구체적으로**: 도메인 키워드 사용
4. **간결하게**: 최대 1024자
5. **예시 사용**: 사용 사례 예시 포함

### 스킬 지침
1. **명시적으로**: 지식을 가정하지 말 것
2. **템플릿 제공**: 코드 구조 포함
3. **패턴 표시**: 규칙 시연
4. **컨텍스트 설명**: 왜 이렇게 하는지
5. **검증 포함**: 정확성을 검증하는 방법

### 도구 제한
```yaml
# 읽기/쓰기 접근 (기본값)
allowed-tools: Read, Write, Edit, Glob, Grep

# 읽기 전용 (분석 스킬용)
allowed-tools: Read, Grep, Glob

# 특정 도구만
allowed-tools: Read, Edit
```

## 점진적 컨텍스트 로딩

Claude는 스킬 파일을 점진적으로 로드합니다:
1. **SKILL.md** - 항상 먼저 로드
2. **reference.md** - 더 자세한 정보가 필요할 때 로드
3. **examples.md** - 예시가 요청될 때 로드
4. **기타 파일** - 필요에 따라 로드

이는 풍부한 컨텍스트를 유지하면서 토큰 사용을 최적화합니다.

## 스킬 디버깅

### 스킬이 활성화되지 않나요?

**확인:**
1. 설명에 관련 키워드가 언급됨
2. 설명이 언제 사용할지 설명함
3. 스킬 이름이 디렉토리 이름과 일치
4. SKILL.md에 유효한 YAML 프론트매터
5. 요청이 도메인 용어 사용

### 스킬이 잘못된 출력을 생성하나요?

**검토:**
1. 지침이 명확하고 명시적
2. 코드 템플릿이 정확
3. 예시가 원하는 출력과 일치
4. 프로젝트 구조에 대한 컨텍스트 포함

## 관련 문서

- [명령 가이드](./commands-guide_KOR.md) - 수동 슬래시 명령 참조
- [개발 워크플로우](./development-workflow_KOR.md) - 개발 프로세스
- [코딩 규칙](../guidelines/coding-conventions_KOR.md) - 코드 표준
- [Claude Code Skills](https://docs.claude.com/en/docs/claude-code/skills) - 공식 문서
- [Anthropic Skills Repo](https://github.com/anthropics/skills) - 예시 스킬

---

**문서 상태**: 승인됨
**버전**: 1.0.0
**마지막 업데이트**: 2025-10-25
