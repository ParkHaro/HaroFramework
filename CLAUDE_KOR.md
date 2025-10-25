# CLAUDE_KOR.md

이 파일은 이 저장소의 코드 작업 시 Claude Code (claude.ai/code)에게 지침을 제공합니다.

## ⚠️ 중요: 2-Layer Architecture

HaroFramework는 **엄격한 2-layer architecture**를 사용합니다:

- **Framework Layer** (`.claude/framework/`): 재사용 가능한 게임 프레임워크
- **Game Layer** (`.claude/games/[game-name]/`): 특정 게임 구현

### Layer 의존성 규칙
```
✅ 허용:    Game → Framework (게임이 프레임워크 사용 가능)
❌ 금지:    Framework → Game (프레임워크는 게임 참조 불가)
```

**중요한 이유**: Framework는 모든 게임에서 재사용 가능해야 합니다. 이 규칙을 위반하면 프레임워크가 특정 게임에 결합됩니다.

---

## 📚 중요: 문서 먼저 읽기

### Framework 문서 (필수 읽기)

**작업 시작 전, `.claude/framework/doc/`의 다음 문서들을 읽으세요:**

#### Architecture & Guidelines (먼저 읽기)
1. **`doc/architecture/layer-system.md`** - 2-layer architecture 상세 내용 및 의존성 규칙
2. **`doc/architecture/project-overview.md`** - 프로젝트 구조, architecture, 기술 스택
3. **`doc/guidelines/coding-conventions.md`** - 명명 규칙, 코드 구조, Unity 모범 사례
4. **`doc/guidelines/documentation-rules.md`** - 이중 언어 문서 시스템 및 메타데이터 표준

#### Workflow & Tools
5. **`doc/workflow/development-workflow.md`** - 표준 개발 워크플로우
6. **`doc/workflow/skills-guide.md`** - Unity 개발을 위한 자동 활성화 기능
7. **`doc/workflow/commands-guide.md`** - 수동 slash commands 참조

#### Project Management
- **`project/SPEC.md`** - 종합 프로젝트 사양
- **`project/TODO.md`** - 현재 작업 및 진행 상황 추적

### 문서 읽기 가이드라인

**Claude Code용**:
- ✅ **영어 문서만 읽기** (`.md` 파일)
- ❌ **한글 번역본 읽지 않기** (`_KOR.md` 파일)
- 이유: 약 50% context token 절약, 원본 문서가 source of truth

**개발자용**:
- 언어 선호도 선택 (영어 `.md` 또는 한글 `_KOR.md`)
- 두 버전 모두 동일한 정보 포함

---

## 핵심 규칙

### 1. 문서 우선 접근
- 코드 작성 전 **항상** `.claude/framework/doc/`의 관련 문서 읽기
- `coding-conventions.md`의 규칙 따르기
- architecture 결정은 `project-overview.md` 참조
- `layer-system.md`에서 layer 경계 이해

### 2. Layer 인식
**코드 작성 시 자문하기**:
- Framework layer인가 Game layer인가?
- Framework인 경우: 게임 특정 코드를 참조하는가? (반드시 NO)
- Game인 경우: Framework 유틸리티를 사용할 수 있는가? (Yes, 권장)

### 3. Namespace 규칙
```csharp
// Framework 코드
namespace HaroFramework.[Category]
{
    // 모든 framework 코드는 반드시 HaroFramework namespace 사용
}

// Game 코드
namespace [GameName].[Category]
{
    // 게임 특정 코드는 게임 이름을 root namespace로 사용
}
```

**Framework Categories**: `Core`, `Player`, `AI`, `UI`, `Audio`, `Gameplay`, `Systems`, `Data`, `Editor`, `Tests`

### 4. 코드 구조
- 정리를 위해 **regions** 사용: `#region Inspector Fields`, `#region Unity Lifecycle` 등
- Private fields: `_camelCase` (밑줄 포함)
- Public properties: `PascalCase`
- `Awake()`에서 component 참조 캐싱

### 5. Unity 6 특정 사항
- 더 이상 사용되지 않는 `FindObjectOfType<T>()` 대신 `FindFirstObjectByType<T>()` 사용
- MonoBehaviour (Behavior 아님) - Unity 6 철자
- Universal Render Pipeline (URP) 활성화 - URP 호환 shader 사용

### 6. 테스트 필수
- 새 기능에 대한 테스트 작성
- `/test` 명령어로 테스트 실행
- 테스트는 `Assets/Scripts/Tests/`에 위치

### 7. 문서화 필수
- public API에 XML 문서화 (`///`) 추가
- serialized field에 `[Tooltip]` 포함
- inspector 정리를 위해 `[Header]` 추가
- `.md` 파일에 대한 이중 언어 문서화 규칙 준수

---

## 빠른 참조

### Unity 버전
- **Unity**: 6000.2.9f1 (Unity 6)
- **URP**: 17.2.0
- **Input System**: 1.14.2 (New Input System - legacy 사용 안 함)

### 주요 Commands
```bash
/test           # 테스트 실행
/build          # 프로젝트 빌드
/component      # MonoBehaviour 생성
/scriptable     # ScriptableObject 생성
```

### Skills (자동 활성화)
Skills는 자연어 요청에 따라 자동으로 활성화됩니다:
- **unity-component**: MonoBehaviour component 생성
- **unity-scriptable**: ScriptableObject 생성
- **unity-editor**: Editor extension 생성
- **unity-testing**: 테스트 생성
- **unity-shader**: URP shader 생성

---

## 파일 위치

### Scripts 구조
```
Assets/Scripts/
├── Runtime/         # Runtime 코드 (.asmdef로 정리 예정)
├── Editor/          # Editor 전용 코드
└── Tests/           # 테스트 코드
    ├── EditMode/    # Edit mode 테스트
    └── PlayMode/    # Play mode 테스트
```

### Framework 문서 (새 구조)
```
.claude/framework/
├── project/
│   ├── SPEC.md                         # 프로젝트 사양
│   ├── SPEC_KOR.md                     # 한글 번역
│   ├── TODO.md                         # 작업 추적
│   └── TODO_KOR.md                     # 한글 번역
├── doc/
│   ├── architecture/
│   │   ├── layer-system.md             # 2-layer architecture
│   │   ├── layer-system_KOR.md
│   │   ├── project-overview.md         # 프로젝트 구조
│   │   └── project-overview_KOR.md
│   ├── guidelines/
│   │   ├── coding-conventions.md       # 코드 표준
│   │   ├── coding-conventions_KOR.md
│   │   ├── documentation-rules.md      # 문서화 시스템
│   │   └── documentation-rules_KOR.md
│   └── workflow/
│       ├── development-workflow.md     # 개발 프로세스
│       ├── development-workflow_KOR.md
│       ├── skills-guide.md             # Skills 참조
│       ├── skills-guide_KOR.md
│       ├── commands-guide.md           # Commands 참조
│       └── commands-guide_KOR.md
└── scripts/                            # 자동화 스크립트
    ├── layer_validate.py
    ├── doc_validate.py
    ├── doc_sync.py
    └── version_bump.py
```

### Game Projects (향후)
```
.claude/games/
├── _template/                          # 새 게임용 템플릿
│   └── [project structure]
└── [game-name]/                        # 특정 게임 프로젝트
    ├── project/
    │   ├── GAME.md                     # 게임 사양
    │   ├── SPEC.md                     # 게임 특정 spec
    │   └── TODO.md                     # 게임 작업
    └── doc/                            # 게임 특정 문서
```

---

## 워크플로우 요약

1. **읽기** `.claude/framework/doc/`의 framework 문서
2. **이해** 작업 중인 layer (Framework vs Game)
3. **계획** 규칙과 layer 경계에 기반한 접근법
4. **구현** 코딩 표준을 따라서
5. **테스트** `/test` 명령어 사용
6. **검증** 코드가 규칙과 layer 규칙을 따르는지
7. **문서화** XML 주석과 필요시 .md 파일 업데이트

---

## Git Commit 가이드라인

### Commit Message 형식
Conventional commits 형식을 따르세요:
```
<type>(<scope>): <subject>

<body>
```

**Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

### 중요: Commit Message 규칙
- ❌ **포함 금지** `Generated with [Claude Code]` footer
- ❌ **포함 금지** `Co-Authored-By: Claude` attribution
- ✅ **포함 필수** 명확하고 간결한 변경 사항 설명
- ✅ **사용 필수** conventional commit 형식

**이유**: 커밋 히스토리를 깔끔하게 유지하고 실제 변경 사항에 집중하며, 도구 attribution은 제외합니다.

### 예시
```bash
# 좋은 커밋 메시지
feat: Add player health system

Implement health management with damage calculation:
- Add HealthComponent with configurable max health
- Implement damage reduction based on armor
- Add death event system for game over handling

# 나쁜 커밋 메시지 (이렇게 하지 마세요)
feat: Add player health system

🤖 Generated with [Claude Code](https://claude.com/claude-code)
Co-Authored-By: Claude <noreply@anthropic.com>
```

---

## 의문 사항이 있을 때

### 코드 표준 관련
1. `.claude/framework/doc/guidelines/coding-conventions.md` 확인
2. `.claude/framework/doc/architecture/project-overview.md` 확인
3. `.claude/framework/doc/workflow/development-workflow.md` 확인

### Architecture 질문
1. `.claude/framework/doc/architecture/layer-system.md` 확인
2. `.claude/framework/project/SPEC.md` 확인
3. 요구사항이 불명확하면 명확화 질문하기

### Layer 경계 질문
**자문하기**:
- Framework 코드가 Game 코드를 참조하려 하는가? → **중지, 재설계**
- Game 코드가 Framework 유틸리티를 사용하는가? → **OK, 진행**
- 어느 layer인지 확실하지 않은가? → **`layer-system.md` 확인**

---

## Claude Code를 위한 Context 관리

### Token 최적화
- **영어 `.md` 파일만** 읽기 (`_KOR.md` 번역본 건너뛰기)
- 점진적 context 로딩 사용 (필요한 것만 읽기)
- Context가 85% 도달 시 (170K/200K tokens):
  - 현재 진행 상황으로 SPEC.md와 TODO.md 업데이트
  - `/clear` 사용하여 context 리셋
  - 업데이트된 SPEC.md와 TODO.md에서 재개

### 세션 복원
새 세션 시작 시:
1. `.claude/framework/project/SPEC.md` 읽기
2. `.claude/framework/project/TODO.md` 읽기
3. 필요에 따라 작업 특정 문서 읽기
4. TODO.md의 "🔴 Currently In Progress" 섹션에서 계속

---

**기억하세요**:
- 이 파일은 핵심 규칙과 구조 개요만 포함
- **모든 상세 문서는 `.claude/framework/doc/`에 있으며** 작업 시작 전 반드시 참조
- **2-layer architecture 존중** - Framework는 절대 Game 코드 참조 불가
- **영어 문서만 읽기**로 context 사용 최적화
