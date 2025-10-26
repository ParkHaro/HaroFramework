---
title: 2-Scope 아키텍처 시스템
version: 1.0.0
scope: framework
created: 2025-10-25
modified: 2025-10-26
category: Architecture
tags: [architecture, scopes, design, separation-of-concerns]
paired_document: scope-system.md
parent_documents:
  - ../../project/SPEC_KOR.md
child_documents: []
references:
  - ../guidelines/documentation-rules_KOR.md
  - ../guidelines/coding-conventions_KOR.md
status: approved
---


<!-- Navigation -->
**🏠 [HaroFramework Project](../../../MASTER_INDEX_KOR.md)** | **📂 [2-Scope 아키텍처 시스템](./)** | **⬆️ [HaroFramework 명세서](../../project/SPEC_KOR.md)**

---
# 2-Scope 아키텍처 시스템

## 개요

HaroFramework는 프레임워크가 여러 게임 프로젝트에서 재사용 가능하도록 엄격한 **2-Scope 아키텍처**를 사용합니다. 이 아키텍처는 단방향 의존성 규칙을 통해 프레임워크 코드와 게임별 코드 간의 명확한 분리를 강제합니다.

**핵심 원칙**: 프레임워크는 게임에 구애받지 않고 재사용 가능해야 하며, 게임은 프레임워크를 자유롭게 사용하고 확장할 수 있습니다.

---

## 아키텍처 스코프

### Scope 1: Framework Scope (기반/토대)

**목적**: 여러 게임 프로젝트에서 활용할 수 있는 재사용 가능한 게임 시스템, 유틸리티, 패턴 제공.

**특징**:
- **독립적**: 어떤 게임 프로젝트도 인식하지 않음
- **재사용 가능**: 수정 없이 모든 게임에서 사용 가능
- **범용적**: 범용 시스템과 도구 제공
- **안정적**: 변경 빈도가 낮고 하위 호환성 유지
- **잘 문서화됨**: 포괄적인 문서와 예제 제공

**위치**:
- 코드: `Assets/Scripts/Runtime/` (HaroFramework 네임스페이스)
- 문서: `.claude/framework/`

**네임스페이스 규칙**:
```csharp
namespace HaroFramework.Core
namespace HaroFramework.Player
namespace HaroFramework.AI
namespace HaroFramework.UI
// 등등
```

**책임**:
- 핵심 시스템 (Player, AI, UI, Audio 등)
- 공통 유틸리티 및 헬퍼
- 프레임워크 초기화 및 생명주기
- 서비스 로케이터 및 의존성 주입
- 이벤트 시스템 및 메시징
- 오브젝트 풀링 및 메모리 관리
- 데이터 구조 및 컨테이너
- 에디터 도구 및 유틸리티
- 프레임워크 테스트 인프라

**Framework Scope가 포함하는 것**:
- ✅ 게임 시스템용 추상 기본 클래스
- ✅ 인터페이스 및 계약
- ✅ 유틸리티 함수 및 확장
- ✅ 공통 데이터 구조
- ✅ 디자인 패턴 구현
- ✅ 범용 시스템 (입력, 오디오 등)
- ✅ 프레임워크용 에디터 도구

**Framework Scope가 절대 포함하지 않는 것**:
- ❌ 게임별 로직이나 규칙
- ❌ 게임 콘텐츠나 에셋
- ❌ 게임 코드 참조
- ❌ 게임별 구성
- ❌ 게임 존재에 대한 인식

---

### Scope 2: Game Scope (구현)

**목적**: 프레임워크를 기반으로 특정 게임 로직, 콘텐츠, 메카닉 구현.

**특징**:
- **의존적**: Framework Scope에 의존하고 확장
- **특정적**: 게임별 구현 포함
- **유연함**: 게임 요구사항에 따라 자주 수정 가능
- **구체적**: 실제 게임 동작 구현
- **맞춤형**: 특정 게임 요구사항에 맞춤

**위치**:
- 코드: `Assets/Scripts/Runtime/` (게임별 네임스페이스)
- 문서: `.claude/games/[game-name]/`

**네임스페이스 규칙**:
```csharp
namespace GameName.Gameplay
namespace GameName.Characters
namespace GameName.Levels
// 등등
```

**책임**:
- 게임별 구현
- 게임 규칙 및 메카닉
- 게임 콘텐츠 및 데이터
- 레벨 디자인 및 진행
- 게임 UI 및 메뉴
- 게임별 에디터 도구
- 게임 테스트

**Game Scope가 포함하는 것**:
- ✅ 프레임워크 시스템의 구체적 구현
- ✅ 게임별 로직 및 규칙
- ✅ 게임 콘텐츠 및 구성
- ✅ 커스텀 게임 메카닉
- ✅ 레벨별 스크립트
- ✅ 게임 UI 구현
- ✅ 프레임워크 코드 참조

**Game Scope가 피해야 할 것**:
- ⚠️ 프레임워크 코드 직접 수정 (대신 확장)
- ⚠️ 프레임워크 기능 중복
- ⚠️ 프레임워크 제한사항 우회 (프레임워크 변경 요청)

---

## 의존성 규칙

### 황금 규칙: 단방향 의존성

```
┌─────────────┐
│  Game Scope │
└──────┬──────┘
       │ 의존
       ↓ (✅ 허용)
┌─────────────────┐
│ Framework Scope │
└─────────────────┘
       │
       ↑ (❌ 금지)
       │ 의존 불가
┌──────────────┐
│  Game Scope  │
└──────────────┘
```

### 규칙 1: Game → Framework (✅ 허용)

**Game Scope가 할 수 있는 것**:
- 프레임워크 클래스 임포트 및 사용
- 프레임워크 기본 클래스 상속
- 프레임워크 인터페이스 구현
- 프레임워크 API 호출
- 프레임워크 문서 참조
- 프레임워크 기능 확장
- 프레임워크 유틸리티 사용

**예제**:
```csharp
// ✅ 프레임워크에서 상속하는 게임 클래스
namespace MyGame.Characters
{
    using HaroFramework.Player;

    public class MyGamePlayer : PlayerController
    {
        // 게임별 플레이어 구현
    }
}

// ✅ 프레임워크 유틸리티를 사용하는 게임
namespace MyGame.Gameplay
{
    using HaroFramework.Core;

    public class GameManager : MonoBehaviour
    {
        private ServiceLocator _services;

        private void Awake()
        {
            _services = ServiceLocator.Instance;
        }
    }
}
```

### 규칙 2: Framework → Game (❌ 금지)

**Framework Scope가 할 수 없는 것**:
- 게임 클래스 임포트
- 게임별 코드 참조
- 게임 존재 인식
- 게임별 로직 포함
- 게임 문서 링크
- 게임 API 호출

**이 규칙이 존재하는 이유**:
1. **재사용성**: 프레임워크를 모든 게임에서 사용 가능
2. **유지보수성**: 프레임워크 변경이 게임 변경을 요구하지 않음
3. **테스트 가능성**: 프레임워크를 독립적으로 테스트 가능
4. **모듈성**: 관심사의 명확한 분리
5. **확장성**: 새 게임 추가가 쉬움

---

## 아키텍처 다이어그램

### 상위 수준 구조

```
┌───────────────────────────────────────────┐
│           여러 게임들                      │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│  │  Game A  │ │  Game B  │ │  Game C  │ │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ │
│       └────────────┼────────────┘       │
└────────────────────┼──────────────────────┘
                     ↓ (모두 의존)
         ┌───────────────────────┐
         │   HaroFramework       │
         │  (공유 토대)           │
         └───────────────────────┘
```

### 폴더 구조

```
Assets/Scripts/
├── Runtime/
│   ├── HaroFramework/          # Framework Scope
│   │   ├── Core/
│   │   ├── Player/
│   │   ├── AI/
│   │   └── UI/
│   │
│   └── [GameName]/             # Game Scope
│       ├── Gameplay/
│       ├── Characters/
│       └── Levels/
│
├── Editor/
│   ├── HaroFramework/          # Framework Editor
│   └── [GameName]/             # Game Editor
│
└── Tests/
    ├── Framework/              # Framework Tests
    └── [GameName]/             # Game Tests
```

### 의존성 흐름

```
게임 게임플레이 로직
        ↓ 사용
게임 캐릭터 컨트롤러 (구체적)
        ↓ 확장
프레임워크 PlayerController (추상)
        ↓ 사용
프레임워크 핵심 시스템
```

---

## 올바른 아키텍처 예제

### 예제 1: 프레임워크 기본 클래스, 게임 구현

**Framework Scope** (`HaroFramework.Player`):
```csharp
namespace HaroFramework.Player
{
    /// <summary>
    /// 모든 플레이어 컨트롤러의 기본 클래스.
    /// 플레이어 이동과 입력의 공통 기능 제공.
    /// </summary>
    public abstract class PlayerController : MonoBehaviour
    {
        [SerializeField] protected float _moveSpeed = 5f;

        protected virtual void Update()
        {
            HandleInput();
            Move();
        }

        protected abstract void HandleInput();
        protected abstract void Move();

        /// <summary>
        /// 프레임워크 유틸리티: 입력에서 이동 방향 얻기.
        /// </summary>
        protected Vector2 GetMovementInput()
        {
            // 범용 입력 처리
            return new Vector2(Input.GetAxis("Horizontal"),
                             Input.GetAxis("Vertical"));
        }
    }
}
```

**Game Scope** (`MyPlatformer.Player`):
```csharp
namespace MyPlatformer.Player
{
    using HaroFramework.Player;

    /// <summary>
    /// 점프 메카닉을 가진 플랫포머별 플레이어 컨트롤러.
    /// </summary>
    public class PlatformerPlayer : PlayerController
    {
        [SerializeField] private float _jumpForce = 10f;
        private Rigidbody2D _rigidbody;
        private bool _isGrounded;

        protected override void HandleInput()
        {
            // 게임별: 점프 입력 처리
            if (Input.GetButtonDown("Jump") && _isGrounded)
            {
                Jump();
            }
        }

        protected override void Move()
        {
            Vector2 input = GetMovementInput(); // 프레임워크 유틸리티 사용
            _rigidbody.velocity = new Vector2(input.x * _moveSpeed,
                                             _rigidbody.velocity.y);
        }

        private void Jump()
        {
            // 게임별 점프 구현
            _rigidbody.AddForce(Vector2.up * _jumpForce, ForceMode2D.Impulse);
        }
    }
}
```

### 예제 2: 프레임워크 인터페이스, 게임 구현

**Framework Scope** (`HaroFramework.Core`):
```csharp
namespace HaroFramework.Core
{
    /// <summary>
    /// 데미지를 받을 수 있는 오브젝트의 인터페이스.
    /// </summary>
    public interface IDamageable
    {
        int Health { get; }
        int MaxHealth { get; }
        bool IsAlive { get; }

        void TakeDamage(int amount);
        void Heal(int amount);
    }
}
```

**Game Scope** (`MyGame.Combat`):
```csharp
namespace MyGame.Combat
{
    using HaroFramework.Core;

    /// <summary>
    /// 커스텀 데미지 동작을 가진 게임별 적.
    /// </summary>
    public class Enemy : MonoBehaviour, IDamageable
    {
        [SerializeField] private int _maxHealth = 100;
        private int _currentHealth;

        public int Health => _currentHealth;
        public int MaxHealth => _maxHealth;
        public bool IsAlive => _currentHealth > 0;

        private void Start()
        {
            _currentHealth = _maxHealth;
        }

        public void TakeDamage(int amount)
        {
            _currentHealth -= amount;

            // 게임별: 피격 애니메이션 재생
            PlayHurtAnimation();

            if (!IsAlive)
            {
                Die();
            }
        }

        public void Heal(int amount)
        {
            _currentHealth = Mathf.Min(_currentHealth + amount, _maxHealth);
        }

        private void PlayHurtAnimation()
        {
            // 게임별 애니메이션 로직
        }

        private void Die()
        {
            // 게임별 사망 로직
            Destroy(gameObject);
        }
    }
}
```

---

## 안티패턴 (하지 말아야 할 것)

### ❌ 안티패턴 1: 프레임워크가 게임 참조

**잘못됨** - 특정 게임을 인식하는 프레임워크 코드:
```csharp
namespace HaroFramework.Player
{
    using MyGame.Characters; // ❌ 프레임워크가 게임 임포트!

    public class PlayerController : MonoBehaviour
    {
        public void Initialize()
        {
            // ❌ 프레임워크가 게임별 오브젝트 생성
            var gamePlayer = new MyGamePlayer();
        }
    }
}
```

**올바름** - 추상화 사용:
```csharp
namespace HaroFramework.Player
{
    // ✅ 프레임워크가 추상 기반 제공
    public abstract class PlayerController : MonoBehaviour
    {
        public abstract void Initialize();
    }
}

namespace MyGame.Characters
{
    using HaroFramework.Player;

    // ✅ 게임이 구체적 동작 구현
    public class MyGamePlayer : PlayerController
    {
        public override void Initialize()
        {
            // 게임별 초기화
        }
    }
}
```

### ❌ 안티패턴 2: 프레임워크에 하드코딩된 게임 값

**잘못됨** - 게임별 상수가 있는 프레임워크:
```csharp
namespace HaroFramework.Combat
{
    public class DamageSystem
    {
        // ❌ 프레임워크의 게임별 값
        private const int SWORD_DAMAGE = 25;
        private const int AXE_DAMAGE = 35;

        public void ApplyWeaponDamage(string weaponType)
        {
            // ❌ 프레임워크가 특정 무기 인식
        }
    }
}
```

**올바름** - 프레임워크가 범용 시스템 제공:
```csharp
namespace HaroFramework.Combat
{
    // ✅ 프레임워크가 범용 데미지 시스템 제공
    public class DamageSystem
    {
        public void ApplyDamage(IDamageable target, int amount)
        {
            target.TakeDamage(amount);
        }
    }
}

namespace MyGame.Items
{
    using HaroFramework.Combat;

    // ✅ 게임이 특정 무기 정의
    public class Weapon : MonoBehaviour
    {
        [SerializeField] private int _damage = 25;

        public void Attack(IDamageable target)
        {
            DamageSystem.Instance.ApplyDamage(target, _damage);
        }
    }
}
```

### ❌ 안티패턴 3: 프레임워크와 게임 코드 혼합

**잘못됨** - 같은 클래스에 프레임워크와 게임 로직:
```csharp
namespace HaroFramework.UI
{
    public class MainMenu : MonoBehaviour
    {
        public void OnPlayClicked()
        {
            // ❌ 게임별 로직이 있는 프레임워크 UI
            StartMySpecificGame();
            LoadMyGameLevel("Level1");
        }
    }
}
```

**올바름** - 관심사 분리:
```csharp
namespace HaroFramework.UI
{
    // ✅ 프레임워크가 범용 메뉴 시스템 제공
    public abstract class MenuBase : MonoBehaviour
    {
        public abstract void OnPlayClicked();
        public abstract void OnQuitClicked();
    }
}

namespace MyGame.UI
{
    using HaroFramework.UI;

    // ✅ 게임이 특정 메뉴 동작 구현
    public class MyGameMainMenu : MenuBase
    {
        public override void OnPlayClicked()
        {
            // 게임별 로직
            GameManager.Instance.StartGame();
        }

        public override void OnQuitClicked()
        {
            Application.Quit();
        }
    }
}
```

---

## 실용적 가이드라인

### 프레임워크 개발자를 위한

**해야 할 것**:
- ✅ 다양한 게임 장르에서 재사용 가능하도록 설계
- ✅ 추상화 사용 (추상 클래스, 인터페이스)
- ✅ 게임을 위한 확장 지점 제공
- ✅ 포괄적인 문서 작성
- ✅ "게임"이 아닌 "시스템" 관점으로 생각
- ✅ 의존성 주입과 서비스 로케이터 사용
- ✅ 프레임워크 구성을 위한 에디터 도구 생성

**하지 말아야 할 것**:
- ❌ 특정 게임에 대한 가정
- ❌ 게임별 값이나 로직 하드코딩
- ❌ 어떤 방식으로든 게임 코드 참조
- ❌ 게임별 기능 생성

### 게임 개발자를 위한

**해야 할 것**:
- ✅ 게임 요구사항에 맞게 프레임워크 클래스 확장
- ✅ 프레임워크 인터페이스 구현
- ✅ 프레임워크 유틸리티와 시스템 사용
- ✅ 프레임워크 규칙과 패턴 따르기
- ✅ 프레임워크 제한사항이나 버그 보고
- ✅ 필요시 새 프레임워크 기능 요청

**하지 말아야 할 것**:
- ❌ 프레임워크 코드 직접 수정
- ❌ 프레임워크 기능 중복
- ❌ 프레임워크 우회 (대신 프레임워크 수정)
- ❌ 프레임워크 시스템 무시

---

## 검증 및 강제

### 자동화된 검증

스코프 규칙을 강제하려면 `scope_validate.py` 스크립트 사용:
```bash
python .claude/scripts/scope_validate.py
```

이 스크립트는:
- 모든 문서 메타데이터 파싱
- scope 필드와 참조 추출
- 금지된 framework → game 참조 감지
- 파일 및 라인 정보와 함께 위반 사항 보고

### 수동 검토 체크리스트

코드 리뷰 중 확인:
- [ ] 프레임워크 코드에 게임 임포트 없음
- [ ] 네임스페이스가 스코프 규칙 준수
- [ ] 프레임워크에 하드코딩된 게임별 값 없음
- [ ] 프레임워크 클래스가 추상적/범용적
- [ ] 게임 코드가 프레임워크 확장 (수정 아님)
- [ ] 문서 참조가 스코프 경계 존중

---

## 2-Scope 아키텍처의 이점

### 프레임워크를 위한
- **재사용성**: 여러 게임 프로젝트에서 사용
- **유지보수성**: 변경사항이 게임과 격리
- **테스트 가능성**: 프레임워크를 독립적으로 테스트
- **모듈성**: 명확한 시스템 경계
- **품질**: 집중을 통한 높은 품질

### 게임을 위한
- **생산성**: 검증된 프레임워크 시스템 활용
- **일관성**: 게임 간 균일한 패턴
- **집중**: 게임별 로직에 집중
- **품질**: 프레임워크 버그 수정이 모든 게임에 적용
- **속도**: 프레임워크 토대로 빠른 개발

---

## 모놀리식에서 2-Scope로 마이그레이션

프레임워크와 게임 관심사가 섞인 기존 코드가 있다면:

1. **식별**: 어떤 코드가 프레임워크인지 게임인지 결정
2. **추출**: 범용 코드를 프레임워크 네임스페이스로 이동
3. **추상화**: 프레임워크에 추상 기본 클래스 생성
4. **구현**: 게임 스코프에 게임별 동작 구현
5. **검증**: `scope_validate.py` 실행하여 분리 확인
6. **테스트**: 리팩토링 후 기능 변경 없음 확인

---

## FAQ

**Q: 프레임워크 코드가 Unity 특정 클래스를 사용할 수 있나요?**
A: 네! 프레임워크는 Unity 클래스(MonoBehaviour, Vector3 등)를 사용할 수 있지만 게임에 구애받지 않아야 합니다.

**Q: 프레임워크에 게임별 동작이 필요하면?**
A: 추상화를 사용하세요. 프레임워크가 추상 기반이나 인터페이스를 제공하고, 게임이 구체적 동작을 구현합니다.

**Q: 하나의 Unity 프로젝트에 여러 게임을 가질 수 있나요?**
A: 권장하지 않습니다. 프레임워크를 패키지/서브모듈로 사용하고 게임 프로젝트를 분리하세요.

**Q: 프레임워크에 필요한 기능이 없으면?**
A: 게임 코드에서 우회하지 말고 프레임워크 개선을 요청하세요.

**Q: 게임 간 코드를 어떻게 공유하나요?**
A: 정말 재사용 가능하다면 프레임워크에 추가하세요. 게임별이라면 게임마다 분리 유지하세요.

---

## 관련 문서

- [SPEC_KOR.md](../../project/SPEC_KOR.md) - 전체 프로젝트 명세서
- [documentation-rules_KOR.md](../guidelines/documentation-rules_KOR.md) - 문서화 표준
- [coding-conventions_KOR.md](../guidelines/coding-conventions_KOR.md) - 코드 표준

---

**문서 상태**: 승인됨
**버전**: 1.0.0
**최종 업데이트**: 2025-10-26
