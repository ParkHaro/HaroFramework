---
title: HaroFramework 명령 인덱스
version: 1.0.0
scope: framework
created: 2025-10-26
modified: 2025-10-26
category: Commands
tags: [commands, index, slash-commands, unity, reference]
paired_document: INDEX.md
parent_documents:
  - ../MASTER_INDEX_KOR.md
child_documents: []
references:
  - ../skills/INDEX_KOR.md
  - ../framework/doc/workflow/development-workflow_KOR.md
status: active
---


<!-- Navigation -->
**🏠 [HaroFramework Project](../MASTER_INDEX_KOR.md)** | **📂 [HaroFramework 명령 인덱스](INDEX_KOR.md)** | **⬆️ [HaroFramework 프로젝트](../MASTER_INDEX_KOR.md)**

---
# HaroFramework 명령 인덱스

Unity 개발 워크플로우를 위한 수동 슬래시 명령입니다. 명령은 `/명령-이름`을 입력하여 명시적으로 호출해야 합니다.

**전체 명령 수**: 9개

---

## 📋 빠른 참조

| 명령 | 설명 | 인자 | 사용 사례 |
|------|------|------|-----------|
| `/component` | MonoBehaviour 생성 | `<이름> [namespace]` | 게임플레이 스크립트, 컨트롤러 |
| `/scriptable` | ScriptableObject 생성 | `<이름> [namespace]` | 데이터 에셋, 게임 설정 |
| `/singleton` | Singleton 패턴 생성 | `<이름>` | 매니저 클래스 |
| `/test` | Unity 테스트 실행 | `[EditMode\|PlayMode\|All]` | 테스트 실행, 검증 |
| `/build` | Unity 프로젝트 빌드 | `[platform]` | 배포, 빌드 |
| `/asmdef` | Assembly Definition 생성 | `<이름> [Runtime\|Editor\|Tests]` | 코드 구조화 |
| `/scene-analyze` | 씬 구조 분석 | `<scene-name>` | 씬 디버깅, 최적화 |
| `/package-add` | Unity 패키지 추가 | `<package-name>` | 패키지 관리 |
| `/input-action` | Input Action map 생성 | `<ActionMapName>` | Input System 설정 |

---

## 🎯 Commands vs Skills

### 명령 사용 시기 (수동)
✅ **명시적 제어가 필요할 때**
- 원하는 것을 정확히 알고 있음
- 특정 설정이 필요함
- 수동 호출 선호

**예시**: `/component PlayerController HaroFramework.Player`

### 스킬 사용 시기 (자동)
✅ **자연어 워크플로우**
- 만들고 싶은 것을 설명
- Claude가 적절한 도구 선택
- 컨텍스트 기반 자동 활성화

**예시**: "플레이어를 위한 체력 시스템 만들어줘"
→ Claude가 자동으로 `unity-component` 스킬 사용

**참고**: 자동 활성화 기능은 [Skills Index](../skills/INDEX_KOR.md) 참조

---

## 📚 명령 카테고리

### 코드 생성 명령

#### `/component <ComponentName> [namespace]`
**목적**: 잘 구조화된 MonoBehaviour 컴포넌트 생성

**생성되는 구조**:
- XML 문서화
- 정리된 리전 (Inspector Fields, Unity Lifecycle, Methods)
- 적절한 네임스페이스
- Unity 6 모범 사례

**기본 네임스페이스**: `HaroFramework`

**예시**:
```bash
/component PlayerController HaroFramework.Player
```

**출력**:
```csharp
namespace HaroFramework.Player
{
    /// <summary>
    /// [설명 추가]
    /// </summary>
    public class PlayerController : MonoBehaviour
    {
        #region Serialized Fields
        // Inspector에 표시되는 필드
        #endregion

        #region Unity Lifecycle
        private void Awake() { }
        private void Start() { }
        #endregion

        #region Public Methods
        // Public API
        #endregion

        #region Private Methods
        // 내부 구현
        #endregion
    }
}
```

**관련 문서**:
- [코딩 규칙](../framework/doc/guidelines/coding-conventions_KOR.md)
- [6계층 아키텍처](../framework/project/spec/02-architecture/6-layer-system_KOR.md)

---

#### `/scriptable <ClassName> [namespace]`
**목적**: 데이터 기반 설계를 위한 ScriptableObject 생성

**생성되는 구조**:
- `[CreateAssetMenu]` 속성
- 런타임 검증을 위한 OnValidate()
- 적절한 네임스페이스 구조

**기본 네임스페이스**: `HaroFramework.Data`

**예시**:
```bash
/scriptable ItemData HaroFramework.Data
```

**사용 사례**:
- 게임 설정 데이터
- 이벤트 시스템 (Event ScriptableObjects)
- 아이템/캐릭터 정의
- 레벨 데이터
- 디자이너 친화적 데이터 에셋

**관련 문서**:
- [Data Layer](../framework/project/spec/02-architecture/6-layer-system_KOR.md)

---

#### `/singleton <ClassName>`
**목적**: 스레드 안전 싱글톤 MonoBehaviour 패턴 생성

**기능**:
- 스레드 안전 지연 초기화
- DontDestroyOnLoad 지원
- 중복 인스턴스 방지
- Unity 6 호환 (`FindFirstObjectByType`)
- 애플리케이션 종료 처리

**기본 네임스페이스**: `HaroFramework.Core`

**예시**:
```bash
/singleton GameManager
```

**모범 사례**:
- 신중하게 사용 (싱글톤은 결합도를 높일 수 있음)
- 테스트 가능성을 위해 의존성 주입 선호
- 적합한 사례: GameManager, AudioManager, InputManager
- 피해야 할 사례: 데이터 클래스, 유틸리티 클래스

**관련 문서**:
- [Singleton Pattern Spec](../framework/project/spec/05-core-systems/foundation/singleton_KOR.md)

---

#### `/asmdef <AssemblyName> [Runtime|Editor|Tests]`
**목적**: 코드 구조화를 위한 Assembly Definition 생성

**장점**:
- 빠른 컴파일 (증분 컴파일)
- 명확한 의존성 경계
- Unity 패키지에 필수
- 더 나은 코드 구조화

**어셈블리 타입**:
- **Runtime**: 게임플레이 코드 (기본값)
- **Editor**: 에디터 전용 스크립트
- **Tests**: 테스트 어셈블리

**예시**:
```bash
/asmdef HaroFramework.Core Runtime
/asmdef HaroFramework.Editor Editor
/asmdef HaroFramework.Tests Tests
```

**권장 구조**:
```
Assets/Scripts/
├── Runtime/
│   └── HaroFramework.Runtime.asmdef
├── Editor/
│   └── HaroFramework.Editor.asmdef
└── Tests/
    ├── EditMode/
    │   └── HaroFramework.EditMode.Tests.asmdef
    └── PlayMode/
        └── HaroFramework.PlayMode.Tests.asmdef
```

**관련 문서**:
- [프로젝트 구조](../framework/project/spec/02-architecture/folder-structure_KOR.md)

---

#### `/input-action <ActionMapName>`
**목적**: Input System action map 에셋 생성

**참고**: 이 프로젝트는 Unity Input System (1.14.2)을 사용하며, **레거시 Input Manager를 사용하지 않습니다**

**생성되는 내용**:
- .inputactions 에셋 구조
- 일반적인 액션이 포함된 Action map
- 컨트롤 스킴 (Keyboard/Mouse, Gamepad, Touch)
- C# 래퍼 클래스 생성 가이드

**일반적인 액션**:
- Movement (Vector2)
- Look (Vector2)
- Jump (Button)
- Interact (Button)
- Pause (Button)

**예시**:
```bash
/input-action PlayerControls
```

**관련 문서**:
- [Input System Package](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.14/manual/index.html)

---

### 테스팅 & 품질 명령

#### `/test [EditMode|PlayMode|All]`
**목적**: Unity Test Framework 테스트 실행

**테스트 타입**:
- **EditMode**: 플레이 모드 없이 에디터에서 실행 (빠름)
- **PlayMode**: 플레이 모드 실행 필요 (느림, 더 현실적)
- **All**: 두 테스트 타입 모두 실행 (기본값)

**예시**:
```bash
/test EditMode        # 빠른 테스트
/test PlayMode        # 통합 테스트
/test All             # 전체 테스트 스위트
```

**수행되는 작업**:
1. 모든 테스트 어셈블리 찾기 (.asmdef with test references)
2. Tests/ 디렉토리에서 테스트 스크립트 찾기
3. 테스트 실행 및 결과 수집
4. 커버리지 및 실패 보고
5. 일반적인 문제에 대한 수정 제안

**관련 문서**:
- [테스팅 가이드](../framework/project/spec/06-quality/code-quality_KOR.md)
- [unity-testing Skill](../skills/unity-testing/SKILL.md)

---

### 프로젝트 관리 명령

#### `/build [platform]`
**목적**: 대상 플랫폼을 위한 Unity 프로젝트 빌드

**지원 플랫폼**:
- Windows (기본값)
- Mac
- Linux
- Android
- iOS
- WebGL

**예시**:
```bash
/build                # 현재 설정 분석
/build Windows        # Windows용 빌드
/build Android        # Android용 빌드
```

**수행되는 작업**:
1. EditorBuildSettings에서 씬 확인
2. 에셋 및 의존성 검증
3. 컴파일 오류 확인
4. Unity CLI 빌드 인자 제공
5. 최적화 기회 제안

**관련 문서**:
- [빌드 설정](../framework/project/spec/07-tech-stack/unity-environment_KOR.md)

---

#### `/scene-analyze <scene-name>`
**목적**: Unity 씬 구조 및 최적화 분석

**예시**:
```bash
/scene-analyze MainMenu
/scene-analyze GameLevel01
```

**분석 내용**:
- GameObject 계층 구조
- 컴포넌트 타입 및 개수
- 스크립트 의존성
- 누락된 참조
- 깨진 프리팹
- 성능 문제
- 최적화 제안

**보고서 지표**:
- 전체 GameObject 수 (Active/Inactive)
- 컴포넌트 사용 통계
- 프리팹 인스턴스
- 누락된 참조
- 성능 병목

**관련 문서**:
- 씬 구조 모범 사례

---

#### `/package-add <package-name>`
**목적**: Package Manager를 통한 Unity 패키지 추가

**패키지 소스**:
- Unity Registry (공식 패키지)
- Git 저장소
- 로컬 패키지

**예시**:
```bash
/package-add Cinemachine
/package-add com.unity.cinemachine
/package-add https://github.com/user/repo.git#1.0.0
```

**일반적인 패키지**:
- `com.unity.cinemachine` - 카메라 시스템
- `com.unity.probuilder` - 레벨 디자인
- `com.unity.textmeshpro` - 텍스트 렌더링
- `com.unity.addressables` - 에셋 관리
- `com.unity.2d.*` - 2D 게임 패키지

**수행되는 작업**:
1. 현재 Packages/manifest.json 읽기
2. 패키지 소스 식별
3. 호환 버전 결정
4. 의존성 충돌 확인
5. manifest.json 업데이트

**관련 문서**:
- [의존성](../framework/project/spec/07-tech-stack/dependencies_KOR.md)

---

## 🚀 사용 패턴

### 일반적인 워크플로우 예시

#### 1. 새 게임플레이 기능 생성
```bash
# 1. 컴포넌트 생성
/component HealthSystem HaroFramework.Gameplay

# 2. 데이터 에셋 생성
/scriptable HealthConfig HaroFramework.Data

# 3. 테스트 생성
# (자연어를 통해 unity-testing 스킬 사용)
"HealthSystem을 위한 테스트 만들어줘"

# 4. 테스트 실행
/test EditMode
```

#### 2. 프로젝트 구조 설정
```bash
# 1. Assembly definition 생성
/asmdef HaroFramework.Core Runtime
/asmdef HaroFramework.Editor Editor
/asmdef HaroFramework.Tests Tests

# 2. 필요한 패키지 추가
/package-add Cinemachine
/package-add TextMeshPro

# 3. Input system 생성
/input-action PlayerControls
```

#### 3. 품질 보증 워크플로우
```bash
# 1. 씬 분석
/scene-analyze GameLevel01

# 2. 테스트 실행
/test All

# 3. 플랫폼 빌드
/build Windows
```

---

## 💡 팁 & 모범 사례

### 명령 사용법
- **탭 완성**: `/`를 입력하고 탭을 눌러 사용 가능한 명령 확인
- **인자**: 여러 단어 인자는 따옴표 사용: `/component "Player Controller"`
- **기본값**: 대부분의 명령은 인자를 생략하면 합리적인 기본값 사용

### Commands와 Skills 선택
**Commands 사용 시**:
- 매개변수에 대한 정확한 제어 필요
- 특정 패턴 반복
- 명시적 설정 원함

**Skills 사용 시**:
- 빌드할 기능 설명
- Claude가 최선의 접근 방식 선택하도록
- 자연어로 작업

### 프레임워크 통합
모든 명령:
- HaroFramework 규칙 준수
- 2-scope 아키텍처 존중 (Framework vs Game)
- Unity 6 호환 코드 생성
- XML 문서화 포함
- 적절한 네임스페이스 구조 사용

---

## 🔗 관련 문서

### Skills (자동 활성화)
- [Skills Index](../skills/INDEX_KOR.md) - 자동 기능
- [Skills vs Commands](../skills/README.md) - 언제 무엇을 사용할지

### 개발 가이드
- [개발 워크플로우](../framework/doc/workflow/development-workflow_KOR.md)
- [코딩 규칙](../framework/doc/guidelines/coding-conventions_KOR.md)
- [문서화 규칙](../framework/doc/guidelines/documentation-rules_KOR.md)

### 아키텍처
- [6계층 시스템](../framework/project/spec/02-architecture/6-layer-system_KOR.md)
- [Scope 시스템](../framework/doc/architecture/scope-system_KOR.md)
- [프로젝트 개요](../framework/doc/architecture/project-overview_KOR.md)

### 빠른 시작
- [빠른 시작 가이드](../framework/project/QUICK_START_KOR.md)
- [읽기 가이드](../framework/project/READING_GUIDE_KOR.md)

---

## 📝 커스텀 명령 추가

프로젝트별 명령 생성 방법:

1. **명령 파일 생성**: `.claude/commands/your-command.md`

2. **메타데이터 추가**:
```markdown
---
description: 이 명령이 하는 일에 대한 간단한 설명
argument-hint: <필수> [선택]
---
```

3. **동작 문서화**:
- 명령이 하는 일
- 인자와 기본값
- 사용 예시
- 생성되는 출력

4. **명령 테스트**:
```bash
/your-command arg1 arg2
```

**커스텀 명령 예시**:
```markdown
---
description: 전투 시스템 생성
argument-hint: <SystemName>
---

데미지 계산과 히트 감지가 포함된 전투 시스템을 생성합니다.

시스템 이름: $ARGUMENTS

[구현 세부사항...]
```

---

**문서 상태**: Active
**유지관리**: HaroFramework Team
**최종 업데이트**: 2025-10-26

**참고**:
- [Skills Index](../skills/INDEX_KOR.md) - 자동 활성화 기능
- [Master Index](../MASTER_INDEX_KOR.md) - 모든 프로젝트 문서
