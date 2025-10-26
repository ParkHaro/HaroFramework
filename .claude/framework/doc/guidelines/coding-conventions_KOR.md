---
title: "코딩 규칙"
version: "1.0.0"
scope: "framework"
created: "2025-10-25"
modified: "2025-10-25"
category: "Guidelines"
tags: [coding, conventions, standards, csharp, unity]
paired_document: "coding-conventions.md"
parent_documents:
  - "../../project/SPEC_KOR.md"
child_documents: []
references:
  - "./documentation-rules_KOR.md"
  - "../architecture/project-overview_KOR.md"
  - "../architecture/scope-system_KOR.md"
status: "approved"
---


<!-- Navigation -->
**🏠 [HaroFramework Project](../../../MASTER_INDEX_KOR.md)** | **📂 [코딩 규칙](./)** | **⬆️ [HaroFramework 명세서](../../project/SPEC_KOR.md)**

---
# 코딩 규칙

## 네임스페이스 구성

### 구조
```csharp
namespace HaroFramework.[Category]
{
    // 코드 작성
}
```

### 카테고리
- **Core**: 프레임워크 핵심 시스템
- **Player**: 플스코프 관련 시스템
- **AI**: 인공지능
- **UI**: 사용자 인터페이스
- **Audio**: 오디오 시스템
- **Gameplay**: 게임플레이 메커니즘
- **Systems**: 게임 시스템 (저장, 설정 등)
- **Data**: ScriptableObject 정의
- **Editor**: 에디터 확장
- **Tests**: 테스트 코드

### 예시
```csharp
namespace HaroFramework.Player
namespace HaroFramework.AI.Pathfinding
namespace HaroFramework.UI.Menus
namespace HaroFramework.Data
```

## 명명 규칙

### 클래스 및 구조체
- **PascalCase**
- 설명적인 이름
```csharp
public class PlayerController { }
public class HealthSystem { }
public struct DamageInfo { }
```

### 메서드
- **PascalCase**
- 동사-명사 형식
```csharp
public void TakeDamage(int amount) { }
private void UpdateHealth() { }
```

### 필드
- **Private**: 밑줄 접두사가 있는 `_camelCase`
- **Public**: `PascalCase`
- **Const/Static Readonly**: `PascalCase`

```csharp
private int _health;
private Transform _targetTransform;

public int MaxHealth { get; private set; }

private const int DefaultHealth = 100;
private static readonly Vector3 StartPosition = Vector3.zero;
```

### 속성
- **PascalCase**
- 자동 속성 선호
```csharp
public int Health { get; private set; }
public bool IsAlive => Health > 0;
```

### 직렬화된 필드
```csharp
[Header("Configuration")]
[Tooltip("최대 체력 값")]
[SerializeField] private int _maxHealth = 100;

[Range(0f, 1f)]
[SerializeField] private float _damageReduction = 0.1f;
```

### Unity 이벤트 함수
- 표준 Unity 명명
```csharp
private void Awake() { }
private void Start() { }
private void Update() { }
private void OnEnable() { }
private void OnDisable() { }
```

## 코드 구조

### 영역 구성
```csharp
public class ExampleComponent : MonoBehaviour
{
    #region Inspector Fields
    [SerializeField] private Type _field;
    #endregion

    #region Private Fields
    private Type _cachedComponent;
    #endregion

    #region Properties
    public Type Property { get; private set; }
    #endregion

    #region Unity Lifecycle
    private void Awake() { }
    private void Start() { }
    #endregion

    #region Public Methods
    public void PublicMethod() { }
    #endregion

    #region Private Methods
    private void PrivateMethod() { }
    #endregion

    #region Editor
    #if UNITY_EDITOR
    private void OnValidate() { }
    #endif
    #endregion
}
```

## Unity 모범 사례

### 컴포넌트 캐싱
```csharp
// Awake에서 캐싱
private Transform _transform;

private void Awake()
{
    _transform = transform;
}
```

### GetComponent 사용
```csharp
// Update에서 피하기
private void Update()
{
    // ❌ 나쁨
    GetComponent<Rigidbody>().AddForce(Vector3.up);
}

// Awake에서 캐싱
private Rigidbody _rigidbody;

private void Awake()
{
    _rigidbody = GetComponent<Rigidbody>();
}

private void Update()
{
    // ✅ 좋음
    _rigidbody.AddForce(Vector3.up);
}
```

### RequireComponent
```csharp
[RequireComponent(typeof(Rigidbody))]
public class PhysicsController : MonoBehaviour
{
    private Rigidbody _rigidbody;

    private void Awake()
    {
        _rigidbody = GetComponent<Rigidbody>();
    }
}
```

### 코루틴
```csharp
// 나중에 중지하기 위해 참조 저장
private Coroutine _damageCoroutine;

public void StartDamageOverTime()
{
    if (_damageCoroutine != null)
        StopCoroutine(_damageCoroutine);

    _damageCoroutine = StartCoroutine(DamageCoroutine());
}

private IEnumerator DamageCoroutine()
{
    while (true)
    {
        TakeDamage(1);
        yield return new WaitForSeconds(1f);
    }
}
```

## 문서화

### XML 주석
```csharp
/// <summary>
/// 엔티티에 데미지를 적용하고 데미지 이벤트를 트리거합니다.
/// </summary>
/// <param name="amount">적용할 데미지 양</param>
/// <returns>데미지가 성공적으로 적용되었으면 true</returns>
public bool TakeDamage(int amount)
{
    // 구현
}
```

### TODO 주석
```csharp
// TODO: 데미지 저항 구현
// FIXME: 체력이 음수가 될 수 있음
// NOTE: 이 메서드는 애니메이션 이벤트에서 호출됨
```

## 오류 처리

### Null 검사
```csharp
// Inspector 참조
private void Start()
{
    if (_targetTransform == null)
    {
        Debug.LogError($"{name}: Target transform not assigned!", this);
        enabled = false;
        return;
    }
}
```

### 검증
```csharp
#if UNITY_EDITOR
private void OnValidate()
{
    _maxHealth = Mathf.Max(1, _maxHealth);

    if (_healthBar == null)
        Debug.LogWarning($"{name}: Health bar reference missing", this);
}
#endif
```

## 성능 가이드라인

### Update에서 피해야 할 것
- 문자열 연결
- GetComponent 호출
- Find 작업
- Instantiate/Destroy
- 복잡한 계산

### 선호해야 할 것
- 캐싱된 참조
- 오브젝트 풀링
- 물리 연산을 위한 Fixed timestep
- 지연된 작업을 위한 코루틴
- 폴링보다 이벤트

### 문자열 처리
```csharp
// ❌ 루프에서 피하기
for (int i = 0; i < 100; i++)
{
    string result = "Item " + i;
}

// ✅ StringBuilder 사용
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 100; i++)
{
    sb.Clear();
    sb.Append("Item ").Append(i);
}
```

## Unity 6 전용

### FindObjectOfType 대체
```csharp
// Unity 6 - FindFirstObjectByType 사용
var manager = FindFirstObjectByType<GameManager>();

// 이전 방식 (더 이상 사용되지 않음)
var manager = FindObjectOfType<GameManager>();
```

### MonoBehaviour 철자
```csharp
// Unity 6 - 올바른 철자
public class MyComponent : MonoBehaviour { }

// 더 이상 "Behavior"가 아님
```

## 어셈블리 정의

### 명명
- `HaroFramework.Runtime` - 런타임 코드
- `HaroFramework.Editor` - 에디터 코드
- `HaroFramework.Tests` - 테스트 코드

### 참조
- Editor 어셈블리는 Runtime 참조
- Tests는 테스트할 대상 참조
- 어셈블리 간 의존성 최소화

## 파일 구성

```
Scripts/
├── Runtime/
│   ├── Core/
│   ├── Player/
│   ├── AI/
│   └── HaroFramework.Runtime.asmdef
├── Editor/
│   ├── Inspectors/
│   ├── Tools/
│   └── HaroFramework.Editor.asmdef
└── Tests/
    ├── EditMode/
    ├── PlayMode/
    └── *.asmdef files
```

## 코드 검토 체크리스트

- [ ] 명명 규칙 준수
- [ ] 적절한 네임스페이스 사용
- [ ] 공개 API에 대한 XML 문서화
- [ ] 컴파일러 경고 없음
- [ ] 캐싱된 컴포넌트 참조
- [ ] 필수 참조에 대한 Null 검사
- [ ] 필드 검증을 위한 OnValidate
- [ ] 매직 넘버 없음 (const/readonly 사용)
- [ ] 적절한 영역 구성
- [ ] 성능 고려사항 처리

## 관련 문서

- [SPEC.md](../../project/SPEC_KOR.md) - 완전한 프로젝트 사양
- [문서화 규칙](./documentation-rules_KOR.md) - 문서화 표준
- [스코프 시스템](../architecture/scope-system_KOR.md) - 2-Scope 아키텍처
- [프로젝트 개요](../architecture/project-overview_KOR.md) - 프로젝트 구조

---

**문서 상태**: 승인됨
**버전**: 1.0.0
**마지막 업데이트**: 2025-10-25
