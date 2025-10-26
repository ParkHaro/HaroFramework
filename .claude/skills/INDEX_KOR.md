---
title: HaroFramework 스킬 인덱스
version: 1.0.0
scope: framework
created: 2025-10-26
modified: 2025-10-26
category: Skills
tags: [skills, index, auto-activation, unity, ai-driven]
paired_document: INDEX.md
parent_documents:
  - ../MASTER_INDEX_KOR.md
child_documents: []
references:
  - ../commands/INDEX_KOR.md
  - ../framework/doc/workflow/skills-guide_KOR.md
status: active
---


<!-- Navigation -->
**🏠 [HaroFramework Project](../MASTER_INDEX_KOR.md)** | **📂 [HaroFramework 스킬 인덱스](INDEX_KOR.md)** | **⬆️ [HaroFramework 프로젝트](../MASTER_INDEX_KOR.md)**

---
# HaroFramework 스킬 인덱스

Claude가 컨텍스트에 따라 자동으로 활성화하는 모델 호출 기능입니다. 스킬은 명시적인 명령 호출 없이 자연어 워크플로우를 가능하게 합니다.

**전체 스킬 수**: 5개

---

## 📋 빠른 참조

| 스킬 | 목적 | 자동 활성화 시기 | 출력 |
|------|------|------------------|------|
| `unity-component` | MonoBehaviour 생성 | 게임플레이 스크립트, 컨트롤러, 매니저 | 프로덕션 준비 컴포넌트 |
| `unity-scriptable` | ScriptableObject 생성 | 데이터 에셋, 게임 설정, 이벤트 | 디자이너 친화적 데이터 |
| `unity-editor` | Editor 확장 생성 | 커스텀 inspector, property drawer, 도구 | 향상된 에디터 워크플로우 |
| `unity-testing` | UTF 테스트 생성 | 단위 테스트, 통합 테스트, TDD | 완전한 테스트 커버리지 |
| `unity-shader` | URP 셰이더 생성 | 비주얼 이펙트, 머티리얼, 렌더링 | URP 호환 셰이더 |

---

## 🎯 Skills vs Commands

### Skills (모델 호출) ✨
**자연어 기반 자동 활성화**

**작동 방식**:
1. 원하는 것을 자연어로 설명
2. Claude가 컨텍스트와 의도 감지
3. 적절한 스킬 자동 활성화
4. 모범 사례를 따르는 결과 생성

**예시**:
```
사용자: "플레이어를 위한 체력 시스템 필요해"
→ Claude: *unity-component 스킬 활성화*
→ 생성: HealthSystem.cs (적절한 구조)
```

**장점**:
- 자연스러운 워크플로우
- 문법 암기 불필요
- 컨텍스트 인식
- 모범 사례 내장

---

### Commands (사용자 호출) ⌨️
**명시적 매개변수를 사용한 수동 호출**

**작동 방식**:
1. 특정 인자와 함께 `/command-name` 입력
2. 주어진 매개변수로 명령 실행
3. 지정된 대로 정확히 결과 생성

**예시**:
```
사용자: "/component HealthSystem HaroFramework.Player"
→ 생성: 지정된 네임스페이스의 HealthSystem.cs
```

**장점**:
- 명시적 제어
- 예측 가능한 출력
- 정확한 설정

**참고**: [Commands Index](../commands/INDEX_KOR.md)

---

## 📚 스킬 카탈로그

### 🎮 unity-component
**목적**: 잘 구조화된 Unity MonoBehaviour 컴포넌트 생성

**자동 활성화 트리거**:
- "플레이어 컨트롤러 만들어"
- "전투 시스템 필요해"
- "이동 스크립트 만들어"
- "...를 위한 매니저 만들어"
- 게임플레이 컴포넌트 요청

**생성되는 구조**:
```csharp
using UnityEngine;

namespace HaroFramework.{Category}
{
    /// <summary>
    /// 자동 생성된 XML 문서화
    /// </summary>
    public class ComponentName : MonoBehaviour
    {
        #region Inspector Fields
        [SerializeField] private float _speed = 5f;
        #endregion

        #region Unity Lifecycle
        private void Awake()
        {
            // 컴포넌트 캐싱
        }

        private void Start()
        {
            // 초기화
        }

        private void Update()
        {
            // 프레임 업데이트
        }
        #endregion

        #region Public Methods
        // Public API
        #endregion

        #region Private Methods
        // 내부 로직
        #endregion
    }
}
```

**기능**:
- 적절한 네임스페이스 구조
- 리전 기반 구조
- XML 문서화
- Unity 6 라이프사이클 메서드
- SerializeField 모범 사례
- 컴포넌트 캐싱 패턴

**적용된 모범 사례**:
- private 필드에 `[SerializeField]`
- 필요시 `[RequireComponent]`
- Awake()에서 컴포넌트 참조 캐싱
- 명확히 분리된 Public API
- Unity 6 API 사용 (FindFirstObjectByType)

**관련 문서**:
- [코딩 규칙](../framework/doc/guidelines/coding-conventions_KOR.md)
- [6계층 아키텍처](../framework/project/spec/02-architecture/6-layer-system_KOR.md)

---

### 📦 unity-scriptable
**목적**: 데이터 기반 설계를 위한 Unity ScriptableObject 생성

**자동 활성화 트리거**:
- "게임 설정 데이터 만들어"
- "이벤트 시스템 필요해"
- "아이템 정의 만들어"
- "캐릭터 스탯 데이터 만들어"
- 데이터 에셋 요청

**생성되는 구조**:
```csharp
using UnityEngine;

namespace HaroFramework.Data
{
    /// <summary>
    /// [목적]을 위한 ScriptableObject
    /// </summary>
    [CreateAssetMenu(fileName = "NewAssetName", menuName = "HaroFramework/Category/AssetName")]
    public class AssetName : ScriptableObject
    {
        #region Serialized Fields
        [Header("Configuration")]
        [SerializeField] private string _assetName;
        [SerializeField] private int _value;
        #endregion

        #region Properties
        public string AssetName => _assetName;
        public int Value => _value;
        #endregion

        #region Unity Callbacks
        private void OnValidate()
        {
            // 런타임 검증
            _value = Mathf.Max(0, _value);
        }
        #endregion

        #region Public Methods
        // 데이터 접근 API
        #endregion
    }
}
```

**기능**:
- 쉬운 생성을 위한 `[CreateAssetMenu]`
- 데이터 검증을 위한 OnValidate()
- 속성 기반 접근
- 디자이너 친화적 구조
- 적절한 네임스페이스 구조

**일반적인 사용 사례**:
- **게임 설정**: 설정, 난이도 레벨
- **이벤트 시스템**: 결합도 감소를 위한 ScriptableObject 이벤트
- **아이템 정의**: 인벤토리 아이템, 무기, 능력
- **캐릭터 데이터**: 스탯, 속성, 진행도
- **레벨 데이터**: 웨이브 정의, 스폰 포인트
- **오디오 이벤트**: 사운드 이펙트 트리거

**관련 문서**:
- [Data Layer](../framework/project/spec/02-architecture/6-layer-system_KOR.md)

---

### 🛠️ unity-editor
**목적**: Unity Editor 확장 및 커스텀 도구 생성

**자동 활성화 트리거**:
- "...을 위한 커스텀 inspector 만들어"
- "property drawer 만들어"
- "에디터 창 만들어"
- "메뉴 아이템 추가해"
- 에디터 확장 요청

**생성되는 카테고리**:

**1. Custom Inspectors**:
```csharp
using UnityEditor;
using UnityEngine;

namespace HaroFramework.Editor
{
    [CustomEditor(typeof(TargetScript))]
    public class TargetScriptEditor : Editor
    {
        public override void OnInspectorGUI()
        {
            serializedObject.Update();

            // 커스텀 inspector UI
            EditorGUILayout.PropertyField(serializedObject.FindProperty("_fieldName"));

            // 커스텀 버튼
            if (GUILayout.Button("Action"))
            {
                (target as TargetScript)?.PerformAction();
            }

            serializedObject.ApplyModifiedProperties();
        }
    }
}
```

**2. Property Drawers**, **3. Editor Windows**, **4. Menu Items** (상세 내용은 영어 버전 참조)

**관련 문서**:
- [Editor Extension Guide](https://docs.unity3d.com/Manual/ExtendingTheEditor.html)

---

### ✅ unity-testing
**목적**: 포괄적인 커버리지를 가진 Unity Test Framework 테스트 생성

**자동 활성화 트리거**:
- "...을 위한 테스트 작성해"
- "단위 테스트 만들어"
- "통합 테스트 필요해"
- "체력 시스템 테스트해"
- 테스팅 요청

**생성되는 구조**:

**EditMode Tests** (빠름, 플레이 모드 불필요):
```csharp
using NUnit.Framework;
using UnityEngine;

namespace HaroFramework.Tests
{
    public class ComponentNameTests
    {
        [Test]
        public void Method_Condition_ExpectedBehavior()
        {
            // Arrange (준비)
            var component = new GameObject().AddComponent<ComponentName>();
            var expectedValue = 10;

            // Act (실행)
            component.SetValue(expectedValue);

            // Assert (검증)
            Assert.AreEqual(expectedValue, component.GetValue());
        }

        [Test]
        public void Method_InvalidInput_ThrowsException()
        {
            // Arrange
            var component = new GameObject().AddComponent<ComponentName>();

            // Act & Assert
            Assert.Throws<ArgumentException>(() => component.SetValue(-1));
        }
    }
}
```

**PlayMode Tests** (느림, 현실적):
```csharp
using System.Collections;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;

namespace HaroFramework.Tests
{
    public class ComponentNamePlayModeTests
    {
        [UnityTest]
        public IEnumerator Component_AfterFrames_BehavesCorrectly()
        {
            // Arrange
            var go = new GameObject();
            var component = go.AddComponent<ComponentName>();

            // Act
            component.Initialize();
            yield return null; // 한 프레임 대기

            // Assert
            Assert.IsTrue(component.IsInitialized);

            // Cleanup
            Object.Destroy(go);
        }
    }
}
```

**기능**:
- AAA 패턴 (Arrange, Act, Assert)
- 설명적인 테스트 이름
- Setup/TearDown 메서드
- 테스트 어셈블리 구조화
- EditMode 및 PlayMode 테스트 모두
- 코루틴을 위한 UnityTest

**모범 사례**:
- 테스트 메서드 명명: `Method_Condition_ExpectedBehavior`
- 테스트당 하나의 단언 (가능하면)
- 명확한 setup과 cleanup
- 복잡한 객체를 위한 테스트 데이터 빌더
- `[TestCase]`를 사용한 매개변수화된 테스트

**관련 문서**:
- [테스팅 가이드](../framework/project/spec/06-quality/code-quality_KOR.md)
- [Unity Test Framework](https://docs.unity3d.com/Packages/com.unity.test-framework@latest)

---

### 🎨 unity-shader
**목적**: Universal Render Pipeline (URP)을 위한 Unity 셰이더 생성

**자동 활성화 트리거**:
- "디졸브 셰이더 만들어"
- "커스텀 머티리얼 필요해"
- "홀로그램 효과 만들어"
- "툰 셰이더 만들어"
- 셰이더/비주얼 이펙트 요청

**셰이더 접근 방식**:

**1. Shader Graph (대부분의 경우 권장)**:
- 비주얼 노드 기반 편집
- 아티스트 친화적
- URP 최적화
- 쉬운 반복 작업

**2. HLSL/ShaderLab (고급 사례)**:
- 완전한 제어
- 성능 최적화
- 복잡한 효과

**생성되는 Shader Graph 구조**:
```
Properties:
- Base Color (Color)
- Base Map (Texture2D)
- Metallic (Float)
- Smoothness (Float)
- Normal Map (Texture2D)
- Emission (Color)

Nodes:
- Sample Texture 2D (Base Map)
- Multiply (Color Tint)
- Sample Texture 2D (Normal Map)
- PBR Master (URP output)

Output:
- URP/Lit or URP/Unlit target
```

**HLSL Shader Template** (상세 내용은 영어 버전 참조)

**URP-Specific Features**:
- SRP Batcher 호환성
- 적절한 render pipeline 태그
- URP 셰이더 라이브러리 포함
- Forward rendering path
- 다중 pass 지원

**일반적인 셰이더 타입**:
- **PBR Materials**: Metallic, specular 워크플로우
- **Toon/Cel Shading**: 스타일라이즈드 렌더링
- **Dissolve Effects**: 객체 디졸브/구체화
- **Outline Shaders**: 캐릭터 외곽선
- **Water/Liquids**: 애니메이션 표면
- **Particle Effects**: 커스텀 파티클 셰이더

**관련 문서**:
- [URP Shader Documentation](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest)
- [Shader Graph Manual](https://docs.unity3d.com/Packages/com.unity.shadergraph@latest)

---

## 🚀 사용 패턴

### 자연어 워크플로우

**예시 1: 컴포넌트 생성**
```
사용자: "WASD 컨트롤이 있는 플레이어 이동 시스템 만들어"

Claude: *unity-component 스킬 활성화*
→ 생성: PlayerMovement.cs
→ 포함: 입력 처리, 이동 로직, 리전
→ 준수: HaroFramework 규칙
```

**예시 2: 데이터 에셋**
```
사용자: "데미지, 사거리, 발사 속도가 있는 무기 데이터 필요해"

Claude: *unity-scriptable 스킬 활성화*
→ 생성: WeaponData.cs
→ 포함: ScriptableObject 설정, 검증
→ 메뉴: HaroFramework/Weapons/WeaponData
```

**예시 3: 테스팅**
```
사용자: "HealthSystem 컴포넌트를 위한 테스트 작성해"

Claude: *unity-testing 스킬 활성화*
→ 생성: HealthSystemTests.cs
→ 포함: AAA 패턴 테스트, 엣지 케이스
→ 커버리지: Public API, 엣지 케이스, 통합
```

### 결합된 워크플로우

**전체 기능 구현**:
```
1. "인벤토리 시스템 만들어"
   → unity-component: InventorySystem.cs

2. "인벤토리 아이템 데이터 만들어"
   → unity-scriptable: InventoryItemData.cs

3. "인벤토리를 위한 커스텀 inspector 만들어"
   → unity-editor: InventorySystemEditor.cs

4. "인벤토리를 위한 테스트 작성해"
   → unity-testing: InventorySystemTests.cs

5. "아이템 하이라이트 셰이더 만들어"
   → unity-shader: ItemHighlight shader graph
```

---

## 💡 팁 & 모범 사례

### 스킬 활성화
- **구체적으로**: "체력 시스템 만들어" > "스크립트 만들어"
- **컨텍스트 제공**: Unity 관련 용어 언급 (MonoBehaviour, ScriptableObject)
- **자연어**: 어떻게가 아닌 무엇을 원하는지 설명

### 스킬이 활성화되지 않을 때
Claude가 예상한 스킬을 사용하지 않는 경우:
1. Unity 컨텍스트를 더 구체적으로 설명
2. 컴포넌트 타입을 명시적으로 언급
3. Unity 용어 사용
4. 기능에 대한 더 많은 세부사항 제공

### Skills와 Commands 결합
**최선의 접근**:
- 기능 설명에는 **Skills** 사용
- 정확하고 반복되는 패턴에는 **Commands** 사용

**예시**:
```
Skill: "전투 시스템 만들어"
Command: /component DamageReceiver HaroFramework.Combat
Skill: "전투 시스템 테스트해"
```

---

## 🔗 관련 문서

### Commands (수동)
- [Commands Index](../commands/INDEX_KOR.md) - 수동 슬래시 명령
- [Commands Guide](../framework/doc/workflow/commands-guide_KOR.md)

### 개발 가이드
- [Skills Guide](../framework/doc/workflow/skills-guide_KOR.md) - 자세한 스킬 문서
- [개발 워크플로우](../framework/doc/workflow/development-workflow_KOR.md)
- [코딩 규칙](../framework/doc/guidelines/coding-conventions_KOR.md)

### 아키텍처
- [6계층 시스템](../framework/project/spec/02-architecture/6-layer-system_KOR.md)
- [프로젝트 개요](../framework/doc/architecture/project-overview_KOR.md)

### 빠른 시작
- [빠른 시작 가이드](../framework/project/QUICK_START_KOR.md)
- [읽기 가이드](../framework/project/READING_GUIDE_KOR.md)

---

## 📚 공식 리소스

- [Claude Code Skills Documentation](https://docs.claude.com/en/docs/claude-code/skills)
- [Unity 6 Documentation](https://docs.unity3d.com/)
- [URP Documentation](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest)
- [Unity Test Framework](https://docs.unity3d.com/Packages/com.unity.test-framework@latest)

---

**문서 상태**: Active
**유지관리**: HaroFramework Team
**최종 업데이트**: 2025-10-26
**프로젝트 컨텍스트**: Unity 6, URP 17.2.0, Input System 1.14.2

**참고**: 스킬은 자동으로 활성화됩니다 - 문법 암기 불필요, 원하는 것을 설명하기만 하세요!
