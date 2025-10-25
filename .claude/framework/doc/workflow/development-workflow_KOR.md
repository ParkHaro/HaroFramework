---
title: "개발 워크플로우"
version: "1.0.0"
scope: "framework"
created: "2025-10-25"
modified: "2025-10-25"
category: "Workflow"
tags: [workflow, development, process, testing, git]
paired_document: "development-workflow.md"
parent_documents:
  - "../../project/SPEC_KOR.md"
child_documents: []
references:
  - "../guidelines/coding-conventions_KOR.md"
  - "../architecture/project-overview_KOR.md"
  - "./commands-guide_KOR.md"
  - "./skills-guide_KOR.md"
status: "approved"
---

# 개발 워크플로우

## 개요

이 문서는 HaroFramework의 표준 개발 워크플로우를 설명합니다.

## 작업 전 체크리스트

작업을 시작하기 전에:

1. **문서 읽기**
   - `.claude/doc/coding-conventions.md` 검토
   - `.claude/doc/`의 관련 Skills/Commands 확인
   - `.claude/doc/project-overview.md`의 프로젝트 구조 검토

2. **요구사항 이해**
   - 기능/수정 사항은 무엇인가?
   - 어떤 컴포넌트가 영향을 받는가?
   - 수락 기준은 무엇인가?

3. **접근 방식 계획**
   - 어떤 패턴을 사용할 것인가?
   - 어떤 테스트가 필요한가?
   - 어떤 문서화가 필요한가?

## 개발 단계

### 1. 계획 단계

**활동:**
- 기능 요구사항 정의
- 영향받는 시스템 식별
- 아키텍처 및 디자인 계획
- 테스트 전략 결정

**도구:**
- Skills 활성화를 위한 자연어
- 구조 계획을 위한 `/component`, `/scriptable`

**결과물:**
- 기능 디자인 문서 (필요시)
- 생성/수정할 파일 목록
- 테스트 계획

### 2. 구현 단계

**활동:**
- 규칙을 따라 코드 작성
- 코드와 함께 테스트 생성 (TDD)
- XML 문서화 추가
- OnValidate 메서드로 검증

**모범 사례:**
- **작은 커밋**: 논리적 단위로 커밋
- **테스트 우선**: 코드 전/와 함께 테스트 작성
- **즉시 문서화**: XML 주석 즉시 추가
- **조기 검증**: 필드 검사를 위해 OnValidate 사용

**Unity 워크플로우:**
```
1. 적절한 네임스페이스로 스크립트 생성
2. Unity에 추가 (Scripts/Runtime/Category/)
3. 핵심 기능 구현
4. 툴팁이 있는 직렬화된 필드 추가
5. Awake()에서 참조 캐싱
6. 테스트 작성
7. Unity Editor에서 테스트
8. 반복
```

### 3. 테스트 단계

**Edit Mode 테스트:**
```csharp
// 순수 로직 테스트
[Test]
public void HealthSystem_TakeDamage_ReducesHealth()
{
    var health = new HealthSystem(100);
    health.TakeDamage(30);
    Assert.AreEqual(70, health.CurrentHealth);
}
```

**Play Mode 테스트:**
```csharp
// Unity 런타임 동작 테스트
[UnityTest]
public IEnumerator Player_OnDamage_TriggersAnimation()
{
    var player = CreateTestPlayer();
    player.TakeDamage(10);
    yield return null; // 한 프레임 대기
    Assert.IsTrue(player.IsPlayingDamageAnimation);
}
```

**테스트 명령:**
```bash
/test EditMode    # 로직 테스트 실행
/test PlayMode    # 런타임 테스트 실행
/test            # 모든 테스트 실행
```

### 4. 문서화 단계

**코드 문서화:**
```csharp
/// <summary>
/// 플스코프 체력과 데미지를 관리합니다.
/// </summary>
public class HealthSystem
{
    /// <summary>
    /// 데미지를 적용하고 체력이 0에 도달하면 사망을 트리거합니다.
    /// </summary>
    /// <param name="amount">적용할 데미지 양</param>
    public void TakeDamage(int amount) { }
}
```

**에셋 문서화:**
- 직렬화된 필드에 툴팁 추가
- 코드 주석에 사용 예시 포함
- 필요시 `.claude/doc/`의 관련 .md 파일 업데이트

### 5. 검토 단계

**자체 검토 체크리스트:**
- [ ] 코딩 규칙 준수
- [ ] 적절한 네임스페이스
- [ ] XML 문서화 포함
- [ ] 좋은 커버리지의 테스트
- [ ] 컴파일러 경고 없음
- [ ] 참조 적절히 캐싱
- [ ] 필드 검증을 위한 OnValidate
- [ ] 매직 넘버 없음
- [ ] Unity 모범 사례 준수
- [ ] 성능 고려사항 처리

**도구:**
- Unity Console (경고 확인)
- Test Runner (모든 테스트 통과 확인)
- `/build` (빌드 오류 없는지 확인)

### 6. 통합 단계

**커밋 전:**
```bash
# 테스트 통과 확인
/test

# 빌드 확인
/build

# 변경사항 검토
git status
git diff
```

**커밋 메시지 형식:**
```
짧은 요약 (50자 이하)

필요시 자세한 설명:
- 무엇이 변경되었는지
- 왜 변경되었는지
- 호환성을 깨는 변경사항
- 관련 이슈 번호
```

## 기능 개발 패턴

### 예시: 체력 시스템 생성

**1. 계획:**
```
요청: "Create a health system"
→ unity-component 스킬 활성화
→ 계획: MonoBehaviour + 설정용 ScriptableObject
```

**2. 데이터 에셋 생성:**
```
요청: "Create health configuration data"
→ unity-scriptable 스킬 활성화
→ 생성: HealthData.cs (ScriptableObject)
```

**3. 컴포넌트 생성:**
```
요청: "Create health system component"
→ unity-component 스킬 활성화
→ 생성: HealthSystem.cs (MonoBehaviour)
```

**4. 테스트 생성:**
```
요청: "Write tests for health system"
→ unity-testing 스킬 활성화
→ 생성: HealthSystemTests.cs
```

**5. 커스텀 Inspector 생성 (필요시):**
```
요청: "Create custom inspector for health system"
→ unity-editor 스킬 활성화
→ 생성: HealthSystemEditor.cs
```

## 반복 워크플로우

```
요구사항 → 계획 → 구현 → 테스트 → 검토
           ↑                         ↓
           └────── 개선 ←───────────┘
```

### 빠른 반복:
1. 작은 변경 수행
2. Unity에서 즉시 테스트
3. 자동화된 테스트 실행: `/test`
4. 결과에 따라 개선
5. 반복

## 일반적인 워크플로우

### 새 기능 추가
```
1. 규칙 읽기: .claude/doc/coding-conventions.md
2. Skill 사용: "Create [feature] system"
3. 테스트 작성: "Create tests for [feature]"
4. 통합: 기존 시스템에 추가
5. 테스트: /test
6. 문서화: 관련 문서 업데이트
7. 커밋: 명확한 메시지로 git commit
```

### 버그 수정
```
1. 테스트로 버그 재현
2. 테스트 실패하게 만들기 (버그 입증)
3. 테스트 통과하도록 코드 수정
4. 수정 확인: /test
5. 부작용 없는지 확인: /build
6. 이슈 참조와 함께 수정 커밋
```

### 리팩토링
```
1. 테스트가 존재하고 통과하는지 확인
2. 코드 리팩토링
3. 테스트가 여전히 통과하는지 확인
4. 경고 없는지 확인
5. 리팩토링 커밋
```

### 테스트 추가
```
1. 스킬 사용: "Write tests for [component]"
2. 생성된 테스트 검토
3. 엣지 케이스 테스트 추가
4. 실행: /test
5. 커버리지 확인
6. 테스트 커밋
```

## 빌드 워크플로우

### 개발 빌드
```bash
/build          # 현재 설정 확인
/build Windows  # Windows용 빌드
```

### 릴리스 빌드
```
1. 모든 테스트 통과 확인: /test
2. 버전 번호 업데이트
3. 타겟 플랫폼용 빌드
4. 타겟 플랫폼에서 빌드 테스트
5. 릴리스 노트 생성
6. git에 릴리스 태그
```

## Git 워크플로우

### 브랜치 전략
```
main (안정)
  └── feature/pscope-system (작업중)
  └── fix/health-bug (작업중)
```

### 표준 플로우
```bash
# 새 기능 시작
git checkout -b feature/feature-name

# 작업 및 커밋
git add .
git commit -m "Implement feature"

# 병합 준비
/test
/build

# 준비되면 병합
git checkout main
git merge feature/feature-name
```

## 성능 테스트

```
1. 기능 구현
2. Unity Profiler에서 프로파일링
3. 병목 지점 식별
4. 핫 패스 최적화
5. 참조 캐싱
6. 필요시 오브젝트 풀링 사용
7. 개선 확인을 위해 재프로파일링
```

## 디버깅 워크플로우

```
1. 이슈 재현
2. Unity Console에서 오류 확인
3. Debug.Log 문 추가
4. Unity Debugger 사용
5. 컴포넌트 inspector 값 확인
6. 참조가 null이 아닌지 확인
7. 실행 순서 확인
8. 이슈 수정
9. 재발 방지를 위한 테스트 추가
```

## 관련 문서

- [코딩 규칙](../guidelines/coding-conventions_KOR.md) - 코드 표준
- [프로젝트 개요](../architecture/project-overview_KOR.md) - 프로젝트 구조
- [명령 가이드](./commands-guide_KOR.md) - 명령 참조
- [스킬 가이드](./skills-guide_KOR.md) - 스킬 참조

---

**문서 상태**: 승인됨
**버전**: 1.0.0
**마지막 업데이트**: 2025-10-25
