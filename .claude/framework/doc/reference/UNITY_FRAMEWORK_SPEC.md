---
title: Unity Game Framework Specification
version: 1.0.0
scope: framework
created: 2025-10-25
modified: 2025-10-27
category: Reference
tags: [framework, architecture, specification, unity]
paired_document: ""
parent_documents: []
child_documents: []
references: []
status: approved
---



<!-- Navigation -->
**🏠 [HaroFramework Project](../../../MASTER_INDEX.md)** | **📂 [Unity Framework Spec](./)** | **⬆️ [Unity Framework Spec](./)**

---


# Unity 범용 게임 프레임워크 스펙 문서

**버전**: 1.0  
**작성일**: 2025-10-25  
**문서 목적**: 장르 독립적 Unity 게임 개발 프레임워크 명세

---

## 📑 목차

1. [개요](#1-개요)
2. [아키텍처](#2-아키텍처)
3. [계층별 상세 스펙](#3-계층별-상세-스펙)
4. [핵심 시스템](#4-핵심-시스템)
5. [생명주기 관리](#5-생명주기-관리)
6. [구현 가이드](#6-구현-가이드)
7. [확장 방법](#7-확장-방법)
8. [구현 TODO](#8-구현-todo)

---

## 1. 개요

### 1.1 프레임워크 목적

- **일관된 개발 방식**: 게임 장르와 무관하게 동일한 구조와 패턴 사용
- **모듈화**: 필요한 기능만 선택적으로 활성화
- **재사용성**: Core 레이어는 모든 프로젝트에서 공통 사용
- **확장성**: 게임별 요구사항에 맞춰 Domain/Service/Gameplay 확장

### 1.2 설계 철학

```
"게임의 내용은 다르지만, 구조와 구현 방식은 동일하다"
```

- **계층 분리**: 각 계층은 명확한 책임을 가짐
- **의존성 방향**: 상위 계층 → 하위 계층 (단방향)
- **통신 표준화**: EventBus, ServiceLocator를 통한 느슨한 결합
- **패턴 통일**: Base 클래스 상속으로 일관된 구현 강제

### 1.3 적용 범위

#### ✅ 적합한 프로젝트
- 중대형 게임 (개발 기간 3개월 이상)
- 팀 프로젝트 (3인 이상)
- 지속적 업데이트 및 확장 예정
- 멀티플랫폼 대응

#### ⚠️ 선택적 적용
- 소규모 프로젝트: Core + Domain만 사용
- 프로토타입: 필요한 계층만 선택적 구현

---

## 2. 아키텍처

### 2.1 전체 구조

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

### 2.2 의존성 흐름

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
- Data는 모든 계층에서 접근 가능 (읽기만)

### 2.3 통신 방식

```
┌─────────────────────────────────────────┐
│         계층 간 통신 규칙                 │
└─────────────────────────────────────────┘

1. 직접 참조 (Direct Reference)
   Gameplay → Service
   Service → Domain
   Domain → Data

2. 이벤트 통신 (Event Bus)
   모든 계층 ↔ 모든 계층
   - 느슨한 결합
   - 비동기 처리

3. 서비스 로케이터 (Service Locator)
   Gameplay/Service → 등록된 Service
   - 중앙 집중 관리
   - 런타임 해결
```

---

## 3. 계층별 상세 스펙

### 3.1 Data Layer (데이터 계층)

#### 목적
- 순수 데이터 구조 정의
- 직렬화/역직렬화 지원
- 게임 로직 배제

#### 구조
```csharp
// 필수 구현: BaseData 상속
public abstract class BaseData
{
    public int Id { get; set; }
    
    // 모든 데이터는 검증 로직 제공
    public abstract bool Validate();
}
```

#### 규칙
1. **로직 금지**: 데이터 저장/표현만 담당
2. **불변성**: 가능한 읽기 전용 속성 사용
3. **직렬화**: `[System.Serializable]` 속성 필수
4. **명명 규칙**: `{Entity}Data` (예: `PlayerData`, `ItemData`)

#### 예시
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

#### 저장 위치
```
Assets/
└── Data/
    ├── Base/
    │   └── BaseData.cs
    └── Game/
        ├── ItemData.cs
        ├── PlayerData.cs
        └── StageData.cs
```

---

### 3.2 Domain Layer (도메인 계층)

#### 목적
- Raw Data 가공 및 변환
- 게임 계산식 적용 (스탯, 데미지, 확률 등)
- 데이터 캐싱 및 최적화
- 비즈니스 룰 구현

#### 구조
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

#### 규칙
1. **데이터 중심**: Data를 읽고 가공만 수행
2. **상태 비저장**: 게임 상태를 Domain에 저장 금지
3. **캐싱 활용**: 반복 계산 방지
4. **명명 규칙**: `{Entity}Domain` (예: `ItemDomain`, `PlayerStatsDomain`)

#### 예시
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
            item.FinalCritRate = CalculateFinalCritRate(item);
            
            itemCache[item.Id] = item;
        }
    }
    
    public override ItemData GetData(int id)
    {
        return itemCache.GetValueOrDefault(id);
    }
    
    public override IEnumerable<ItemData> GetAllData()
    {
        return itemCache.Values;
    }
    
    // 도메인 특화 계산 로직
    private int CalculateFinalAttack(ItemData item)
    {
        return item.BaseAttack + (item.Level * 5);
    }
    
    private float CalculateFinalCritRate(ItemData item)
    {
        return Mathf.Min(item.BaseCritRate * 1.5f, 0.8f);
    }
}
```

#### 저장 위치
```
Assets/
└── Scripts/
    └── Domain/
        ├── Base/
        │   └── BaseDomain.cs
        └── {GameName}/
            ├── ItemDomain.cs
            ├── PlayerStatsDomain.cs
            └── StageDomain.cs
```

---

### 3.3 Core Layer (코어 계층)

#### 목적
- 게임 독립적인 범용 모듈 제공
- 모듈 생명주기 관리
- 프레임워크 기반 시스템 제공

#### 구조
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

#### 기본 제공 모듈

| 모듈명 | 책임 | 우선순위 |
|--------|------|----------|
| **DataModule** | 데이터 로드/저장 | 5 |
| **UIModule** | UI 캔버스 관리 | 10 |
| **SceneModule** | 씬 전환 관리 | 15 |
| **AudioModule** | BGM/SFX 재생 | 20 |
| **NetworkModule** | 네트워크 통신 | 25 |

#### 규칙
1. **게임 독립성**: 특정 게임 로직 포함 금지
2. **독립 동작**: 다른 모듈에 의존하지 않음
3. **선택적 활성화**: Config에서 On/Off 가능
4. **명명 규칙**: `{Feature}Module` (예: `UIModule`, `AudioModule`)

#### 예시
```csharp
public class AudioModule : BaseModule
{
    public override string ModuleName => "Audio";
    public override int Priority => 20;
    
    private AudioSource bgmSource;
    private AudioSource sfxSource;
    
    protected override void OnInitialize()
    {
        var audioObj = new GameObject("AudioManager");
        bgmSource = audioObj.AddComponent<AudioSource>();
        sfxSource = audioObj.AddComponent<AudioSource>();
        
        bgmSource.loop = true;
        GameObject.DontDestroyOnLoad(audioObj);
    }
    
    public void PlayBGM(AudioClip clip, float volume = 1f)
    {
        bgmSource.clip = clip;
        bgmSource.volume = volume;
        bgmSource.Play();
    }
    
    public void PlaySFX(AudioClip clip, float volume = 1f)
    {
        sfxSource.PlayOneShot(clip, volume);
    }
}
```

#### 저장 위치
```
Assets/
└── Framework/
    └── Core/
        ├── Base/
        │   └── BaseModule.cs
        ├── FrameworkManager.cs
        └── Modules/
            ├── UIModule.cs
            ├── AudioModule.cs
            ├── SceneModule.cs
            └── NetworkModule.cs
```

---

### 3.4 Interface Layer (인터페이스 계층)

#### 목적
- 게임 특화 계약 정의
- 의존성 역전 (DIP) 적용
- Service 구현 강제

#### 구조
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

#### 규칙
1. **계약 정의**: 구현 세부사항 배제
2. **IService 상속**: 모든 인터페이스는 IService 구현
3. **명명 규칙**: `I{System}System` (예: `IInventorySystem`, `IBattleSystem`)

#### 저장 위치
```
Assets/
└── Scripts/
    └── Interface/
        ├── IService.cs
        ├── IInventorySystem.cs
        ├── IBattleSystem.cs
        └── IQuestSystem.cs
```

---

### 3.5 Service Layer (서비스 계층)

#### 목적
- Interface 구체 구현
- 게임 비즈니스 로직 처리
- Core 모듈 + Domain 조합 활용

#### 구조
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

#### 규칙
1. **Interface 구현**: 반드시 Interface 정의 후 구현
2. **BaseService 상속**: 생명주기 통일
3. **상태 관리**: 게임 상태를 Service에서 관리
4. **이벤트 발행**: 상태 변경 시 이벤트 Publish
5. **명명 규칙**: `{System}Service` (예: `InventoryService`, `BattleService`)

#### 예시
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
        
        // 이벤트 발행
        EventBus.Publish(new ItemAddedEvent 
        { 
            ItemId = itemId, 
            Count = count 
        });
        
        return true;
    }
    
    public bool RemoveItem(int itemId, int count)
    {
        if (!inventory.ContainsKey(itemId) || inventory[itemId] < count)
            return false;
        
        inventory[itemId] -= count;
        EventBus.Publish(new ItemRemovedEvent 
        { 
            ItemId = itemId, 
            Count = count 
        });
        
        return true;
    }
}
```

#### 저장 위치
```
Assets/
└── Scripts/
    └── Service/
        ├── Base/
        │   └── BaseService.cs
        └── {GameName}/
            ├── InventoryService.cs
            ├── BattleService.cs
            └── QuestService.cs
```

---

### 3.6 Gameplay Layer (게임플레이 계층)

#### 목적
- 실제 게임 로직 구현
- MonoBehaviour 기반
- Service 조합 활용

#### 구조
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

#### 규칙
1. **BaseGameplay 상속**: 생명주기 통일
2. **Service 사용**: 직접 로직 구현 금지, Service 호출
3. **이벤트 구독**: 필요한 이벤트만 구독
4. **명명 규칙**: `{Entity}Controller` (예: `PlayerController`, `EnemyController`)

#### 예시
```csharp
public class PlayerController : BaseGameplay
{
    private IInventorySystem inventorySystem;
    private IBattleSystem battleSystem;
    
    protected override void RegisterServices()
    {
        inventorySystem = Services.Get<IInventorySystem>();
        battleSystem = Services.Get<IBattleSystem>();
    }
    
    protected override void SubscribeEvents()
    {
        EventBus.Subscribe<ItemAddedEvent>(OnItemAdded);
        EventBus.Subscribe<PlayerDamagedEvent>(OnPlayerDamaged);
    }
    
    protected override void UnsubscribeEvents()
    {
        EventBus.Unsubscribe<ItemAddedEvent>(OnItemAdded);
        EventBus.Unsubscribe<PlayerDamagedEvent>(OnPlayerDamaged);
    }
    
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            battleSystem.Attack(targetEnemy);
        }
    }
    
    private void OnItemAdded(ItemAddedEvent e)
    {
        Debug.Log($"아이템 획득: {e.ItemId}");
    }
    
    private void OnPlayerDamaged(PlayerDamagedEvent e)
    {
        Debug.Log($"데미지 받음: {e.Damage}");
    }
}
```

#### 저장 위치
```
Assets/
└── Scripts/
    └── Gameplay/
        ├── Base/
        │   └── BaseGameplay.cs
        └── {GameName}/
            ├── Player/
            │   └── PlayerController.cs
            ├── Enemy/
            │   └── EnemyAI.cs
            └── Stage/
                └── StageManager.cs
```

---

## 4. 핵심 시스템

### 4.1 EventBus (이벤트 버스)

#### 목적
- 계층 간 느슨한 결합
- 비동기 통신
- 이벤트 기반 아키텍처

#### 인터페이스
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

#### 사용 규칙
1. **이벤트 정의**: IGameEvent 구현
2. **명명 규칙**: `{Action}{Entity}Event` (예: `ItemAddedEvent`, `PlayerDamagedEvent`)
3. **데이터 포함**: 필요한 정보만 최소한으로
4. **불변 권장**: readonly 필드 사용

#### 이벤트 예시
```csharp
public class ItemAddedEvent : IGameEvent
{
    public int ItemId { get; set; }
    public int Count { get; set; }
}

public class PlayerDamagedEvent : IGameEvent
{
    public int Damage { get; set; }
    public int CurrentHP { get; set; }
}
```

#### 사용 예시
```csharp
// 발행 (Publisher)
EventBus.Instance.Publish(new ItemAddedEvent 
{ 
    ItemId = 1001, 
    Count = 5 
});

// 구독 (Subscriber)
EventBus.Instance.Subscribe<ItemAddedEvent>(OnItemAdded);

private void OnItemAdded(ItemAddedEvent e)
{
    Debug.Log($"아이템 추가: {e.ItemId} x{e.Count}");
}

// 구독 해제
EventBus.Instance.Unsubscribe<ItemAddedEvent>(OnItemAdded);
```

---

### 4.2 ServiceLocator (서비스 로케이터)

#### 목적
- 서비스 중앙 관리
- 런타임 의존성 해결
- 전역 접근 제공

#### 인터페이스
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

#### 사용 규칙
1. **초기화 시점**: 게임 시작 시 모든 Service 등록
2. **단일 인스턴스**: 하나의 Service는 한 번만 등록
3. **타입 기반**: Interface 타입으로 등록/조회

#### 사용 예시
```csharp
// 등록
var inventoryService = new InventoryService();
ServiceLocator.Instance.Register<IInventorySystem>(inventoryService);

// 조회
var inventory = ServiceLocator.Instance.Get<IInventorySystem>();
inventory.AddItem(1001, 5);

// 확인
if (ServiceLocator.Instance.Has<IBattleSystem>())
{
    var battle = ServiceLocator.Instance.Get<IBattleSystem>();
}
```

---

### 4.3 DataManager (데이터 관리자)

#### 목적
- Domain 중앙 관리
- 데이터 로딩 통합
- Domain 접근 제공

#### 인터페이스
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

---

### 4.4 LifecycleManager (생명주기 관리자)

#### 목적
- 모든 컴포넌트의 생명주기 통일
- 초기화 순서 보장
- 종료 처리 자동화

#### 생명주기 순서
```
1. FrameworkManager.Awake()
   ├─ Core Systems 초기화
   │  ├─ EventBus
   │  ├─ ServiceLocator
   │  └─ DataManager
   │
   ├─ Modules 초기화 (Priority 순)
   │  ├─ DataModule (5)
   │  ├─ UIModule (10)
   │  ├─ SceneModule (15)
   │  └─ AudioModule (20)
   │
   └─ Game 초기화
      ├─ Domain.LoadData()
      └─ Services 등록

2. Scene 로드 후
   └─ Gameplay 초기화

3. 게임 종료 시
   ├─ Gameplay.OnDestroy()
   ├─ Services.Dispose()
   └─ Modules.Shutdown() (역순)
```

---

## 5. 생명주기 관리

### 5.1 초기화 흐름

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
│  - Service      │
│    Locator      │
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

### 5.2 종료 흐름

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

---

## 6. 구현 가이드

### 6.1 신규 게임 시작 체크리스트

```
□ 1단계: 프로젝트 설정
  □ Framework Core 임포트
  □ FrameworkManager 씬에 배치
  □ FrameworkConfig 생성 및 설정

□ 2단계: Data 정의
  □ BaseData 상속 클래스 작성
  □ JSON/CSV 데이터 파일 준비
  □ Validate() 구현

□ 3단계: Domain 구현
  □ BaseDomain<TData> 상속
  □ LoadData() 구현
  □ 게임 계산식 추가

□ 4단계: Interface 정의
  □ IService 상속 인터페이스 작성
  □ 필요한 메서드 선언

□ 5단계: Service 구현
  □ BaseService + Interface 구현
  □ Domain 활용 로직 작성
  □ 이벤트 발행 추가

□ 6단계: Gameplay 구현
  □ BaseGameplay 상속
  □ Service 등록/사용
  □ 이벤트 구독

□ 7단계: 테스트
  □ 초기화 순서 확인
  □ 이벤트 흐름 검증
  □ 메모리 누수 체크
```

### 6.2 폴더 구조 템플릿

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

### 6.3 명명 규칙

| 계층 | 접미사 | 예시 |
|------|--------|------|
| Data | Data | `ItemData`, `PlayerData` |
| Domain | Domain | `ItemDomain`, `StatsDomain` |
| Interface | System | `IInventorySystem`, `IBattleSystem` |
| Service | Service | `InventoryService`, `BattleService` |
| Gameplay | Controller / Manager | `PlayerController`, `StageManager` |
| Event | Event | `ItemAddedEvent`, `StageCompletedEvent` |
| Module | Module | `UIModule`, `AudioModule` |

---

## 7. 확장 방법

### 7.1 새로운 Module 추가

```csharp
// 1. BaseModule 상속
public class CustomModule : BaseModule
{
    public override string ModuleName => "Custom";
    public override int Priority => 30;
    
    protected override void OnInitialize()
    {
        // 초기화 로직
    }
    
    protected override void OnShutdown()
    {
        // 종료 로직
    }
}

// 2. FrameworkConfig에 등록
[SerializeField] private bool enableCustomModule = true;

// 3. GetEnabledModules()에 추가
if (enableCustomModule) 
    modules.Add(new CustomModule());
```

### 7.2 새로운 System 추가

```csharp
// 1. Interface 정의
public interface ICustomSystem : IService
{
    void DoSomething();
}

// 2. Service 구현
public class CustomService : BaseService, ICustomSystem
{
    public override string ServiceName => "Custom";
    
    protected override void InitializeService()
    {
        // 초기화
    }
    
    public void DoSomething()
    {
        // 구현
    }
}

// 3. 등록
ServiceLocator.Instance.Register<ICustomSystem>(new CustomService());

// 4. 사용
var custom = Services.Get<ICustomSystem>();
custom.DoSomething();
```

### 7.3 게임별 커스터마이징

```csharp
// FrameworkManager 상속으로 게임별 초기화 확장
public class RPGFrameworkManager : FrameworkManager
{
    protected override void InitializeGame()
    {
        base.InitializeGame();
        
        // RPG 특화 Domain 로드
        var itemDomain = new ItemDomain();
        DataManager.Instance.RegisterDomain<ItemDomain, ItemData>(itemDomain);
        
        // RPG 특화 Service 등록
        ServiceLocator.Instance.Register<IInventorySystem>(new InventoryService());
        ServiceLocator.Instance.Register<IBattleSystem>(new BattleService());
    }
}
```

---

## 8. 구현 TODO

### Phase 1: Core Foundation (우선순위: 최상)
```
□ Framework/Core/Base/
  □ IModule.cs - 모듈 인터페이스
  □ IService.cs - 서비스 인터페이스
  □ BaseModule.cs - 모듈 베이스 클래스
  □ BaseService.cs - 서비스 베이스 클래스
  □ BaseDomain.cs - 도메인 베이스 클래스
  □ BaseGameplay.cs - 게임플레이 베이스 클래스

□ Framework/Core/Systems/
  □ Singleton.cs - 싱글톤 패턴
  □ EventBus.cs - 이벤트 버스 시스템
  □ ServiceLocator.cs - 서비스 로케이터
  □ DataManager.cs - 데이터 매니저
  □ FrameworkLogger.cs - 로깅 시스템

□ Framework/Core/
  □ FrameworkManager.cs - 프레임워크 매니저
  □ FrameworkConfig.cs - 설정 ScriptableObject

□ Framework/Data/Base/
  □ BaseData.cs - 데이터 베이스 클래스
```

### Phase 2: Core Modules (우선순위: 상)
```
□ Framework/Core/Modules/
  □ UIModule.cs - UI 관리 모듈
  □ AudioModule.cs - 오디오 관리 모듈
  □ SceneModule.cs - 씬 관리 모듈
  □ NetworkModule.cs - 네트워크 모듈 (선택)
```

### Phase 3: Example Game Implementation (우선순위: 중)
```
□ Example RPG 구현
  □ Data/
    □ ItemData.cs
    □ PlayerData.cs
  □ Domain/
    □ ItemDomain.cs
    □ PlayerStatsDomain.cs
  □ Interface/
    □ IInventorySystem.cs
    □ IBattleSystem.cs
  □ Service/
    □ InventoryService.cs
    □ BattleService.cs
  □ Gameplay/
    □ PlayerController.cs
  □ Events/
    □ ItemAddedEvent.cs
    □ PlayerDamagedEvent.cs
```

### Phase 4: Documentation & Testing (우선순위: 중)
```
□ 문서화
  □ API 문서 작성
  □ 튜토리얼 작성
  □ 예제 코드 정리

□ 테스트
  □ Unit Tests
  □ Integration Tests
  □ Performance Tests
```

### Phase 5: Advanced Features (우선순위: 하)
```
□ 고급 기능
  □ 세이브/로드 시스템
  □ 리소스 풀링
  □ 상태 머신
  □ AI 프레임워크
```

---

## 📎 부록

### A. 주요 인터페이스 요약

```csharp
// Core Interfaces
public interface IModule { }
public interface IService { }
public interface IGameEvent { }

// Base Classes
public abstract class BaseData { }
public abstract class BaseDomain<TData> where TData : BaseData { }
public abstract class BaseModule : IModule { }
public abstract class BaseService : IService { }
public abstract class BaseGameplay : MonoBehaviour { }

// Core Systems
public class EventBus : Singleton<EventBus> { }
public class ServiceLocator : Singleton<ServiceLocator> { }
public class DataManager : Singleton<DataManager> { }
public class FrameworkManager : MonoBehaviour { }
```

### B. 개발 시 주의사항

1. **순환 참조 방지**: Service가 다른 Service를 참조할 때 주의
2. **메모리 관리**: EventBus 구독 해제 필수
3. **초기화 순서**: Priority 값으로 명확히 관리
4. **null 체크**: Service/Data 조회 시 항상 확인
5. **로깅**: FrameworkLogger 활용하여 디버깅 용이하게

### C. 성능 최적화 팁

1. **Domain 캐싱**: 반복 계산 결과 저장
2. **이벤트 최소화**: 불필요한 이벤트 발행 지양
3. **Service 재사용**: 싱글톤 패턴 활용
4. **데이터 로딩**: 비동기 로드 고려
5. **오브젝트 풀링**: 빈번히 생성/파괴되는 객체 풀링

### D. 디버깅 가이드

```csharp
// FrameworkLogger 사용
FrameworkLogger.Log("일반 로그");
FrameworkLogger.Warning("경고 로그");
FrameworkLogger.Error("에러 로그");

// 초기화 추적
FrameworkLogger.Log($"[{ModuleName}] Initializing...");

// 이벤트 추적
EventBus.Instance.Subscribe<DebugEvent>(e => {
    FrameworkLogger.Log($"Event: {e.GetType().Name}");
});
```

---

**문서 끝**

다음 단계: Phase 1의 Core Foundation 구현부터 시작하세요.
