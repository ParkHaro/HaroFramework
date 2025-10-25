---
title: "슬래시 명령 가이드"
version: "1.0.0"
layer: "framework"
created: "2025-10-25"
modified: "2025-10-25"
category: "Workflow"
tags: [commands, slash-commands, tools, reference]
paired_document: "commands-guide.md"
parent_documents:
  - "../../project/SPEC_KOR.md"
child_documents: []
references:
  - "./skills-guide_KOR.md"
  - "./development-workflow_KOR.md"
  - "../guidelines/coding-conventions_KOR.md"
status: "approved"
---

# 슬래시 명령 가이드

슬래시 명령은 `/command-name`을 입력하여 명시적으로 호출하는 **사용자 호출** 명령입니다.

## 사용 가능한 명령

### 컴포넌트 생성 명령

#### `/component <Name> [namespace]`
적절한 구조를 가진 MonoBehaviour 컴포넌트를 생성합니다.

**인자:**
- `<Name>`: 컴포넌트 클래스 이름 (필수)
- `[namespace]`: 네임스페이스 (기본값: HaroFramework)

**예시:**
```
/component PlayerController HaroFramework.Player
/component HealthSystem
```

#### `/scriptable <Name> [namespace]`
ScriptableObject 클래스를 생성합니다.

**인자:**
- `<Name>`: ScriptableObject 클래스 이름 (필수)
- `[namespace]`: 네임스페이스 (기본값: HaroFramework.Data)

**예시:**
```
/scriptable GameSettings HaroFramework.Data
/scriptable WeaponData
```

#### `/singleton <Name>`
싱글톤 MonoBehaviour 패턴을 생성합니다.

**인자:**
- `<Name>`: 싱글톤 클래스 이름 (필수)

**예시:**
```
/singleton GameManager
/singleton AudioManager
```

### 프로젝트 관리 명령

#### `/build [platform]`
지정된 플랫폼용으로 프로젝트를 빌드합니다.

**인자:**
- `[platform]`: 타겟 플랫폼 (Windows/Mac/Linux/Android/iOS/WebGL)

**예시:**
```
/build Windows
/build Android
/build
```

#### `/test [mode]`
Unity Test Framework 테스트를 실행합니다.

**인자:**
- `[mode]`: 테스트 모드 (EditMode/PlayMode/All, 기본값: All)

**예시:**
```
/test EditMode
/test PlayMode
/test
```

#### `/package-add <package-name>`
프로젝트에 Unity 패키지를 추가합니다.

**인자:**
- `<package-name>`: Unity 패키지 이름 또는 URL

**예시:**
```
/package-add com.unity.cinemachine
/package-add com.unity.textmeshpro
```

#### `/asmdef <Name> [Type]`
Assembly Definition 파일을 생성합니다.

**인자:**
- `<Name>`: 어셈블리 이름 (필수)
- `[Type]`: 어셈블리 타입 (Runtime/Editor/Tests, 기본값: Runtime)

**예시:**
```
/asmdef HaroFramework.Runtime Runtime
/asmdef HaroFramework.Editor Editor
```

### 분석 및 도구 명령

#### `/scene-analyze <scene-name>`
Unity 씬 구조를 분석하고 인사이트를 제공합니다.

**인자:**
- `<scene-name>`: 씬 파일 이름 (.unity 확장자 제외)

**예시:**
```
/scene-analyze MainMenu
/scene-analyze Level1
```

#### `/input-action <ActionMapName>`
Input System 액션 맵을 생성합니다.

**인자:**
- `<ActionMapName>`: Input Action 에셋 이름

**예시:**
```
/input-action PlayerControls
/input-action UIControls
```

## 명령 구문

### 인자 유형
- `<required>` - 반드시 제공해야 함
- `[optional]` - 생략 가능 (기본값 사용)
- `$ARGUMENTS` - 모든 인자를 단일 문자열로
- `$1, $2, $3...` - 위치 매개변수

### 예시
```bash
# 필수 인자
/component PlayerController

# 필수 + 선택
/component PlayerController HaroFramework.Player

# 선택만
/build

# 선택 포함
/build Windows
```

## 커스텀 명령 생성

`.claude/commands/` 디렉토리에 `.md` 파일을 생성합니다:

```markdown
---
description: 명령에 대한 간단한 설명
argument-hint: <arg1> [arg2]
---

Claude를 위한 자세한 지침.

첫 번째 인자는 $1, 두 번째는 $2를 사용하거나, 모든 인자는 $ARGUMENTS를 사용.

이 명령을 언제 사용할지에 대한 예시와 컨텍스트를 포함하세요.
```

### 커스텀 명령 예시

**파일:** `.claude/commands/my-command.md`

```markdown
---
description: 커스텀 게임 컴포넌트 생성
argument-hint: <ComponentName>
---

HaroFramework를 위한 커스텀 게임 컴포넌트를 생성합니다.

컴포넌트 이름: $1

다음을 포함하는 MonoBehaviour 생성:
1. 적절한 네임스페이스 (HaroFramework.Gameplay)
2. 툴팁이 있는 Inspector 필드
3. Unity 생명주기 메서드
4. XML 문서화

Assets/Scripts/Runtime/Gameplay/에 배치
```

## 모범 사례

1. **설명적인 이름 사용**: 명령 이름은 목적을 명확히 나타내야 함
2. **힌트 제공**: `argument-hint`를 사용하여 예상 인자 표시
3. **컨텍스트 추가**: 명령을 언제 어떻게 사용할지 포함
4. **예시 사용**: 실제 사용 예시 표시
5. **집중 유지**: 각 명령은 한 가지 작업을 잘 수행해야 함

## 명령 vs 스킬 사용 시기

| 시나리오 | 명령 사용 | 스킬 사용 |
|---------|----------|---------|
| 정확한 제어 필요 | ✅ `/component PlayerController` | ❌ |
| 자연어 | ❌ | ✅ "Create a player script" |
| 반복 작업 | ✅ `/build Windows` | ❌ |
| 복잡한 작업 | ❌ | ✅ "Build a health system" |
| 문서화 | ✅ `/scene-analyze MainMenu` | ❌ |

## 명령 위치

명령은 `.claude/commands/`에 저장되며 자동으로:
- Claude Code에서 발견됨
- git을 통해 팀과 공유됨
- 명령 팔레트에서 사용 가능 (`/` 입력)

## 관련 문서

- [스킬 가이드](./skills-guide_KOR.md) - 자동 활성화 스킬 참조
- [개발 워크플로우](./development-workflow_KOR.md) - 개발 프로세스
- [코딩 규칙](../guidelines/coding-conventions_KOR.md) - 코드 표준
- [Claude Code 슬래시 명령 문서](https://docs.claude.com/en/docs/claude-code/slash-commands)

---

**문서 상태**: 승인됨
**버전**: 1.0.0
**마지막 업데이트**: 2025-10-25
