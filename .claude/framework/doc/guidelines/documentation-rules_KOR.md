---
title: 문서화 표준 및 규칙
version: 1.0.0
layer: framework
created: 2025-10-25
modified: 2025-10-25
category: Guidelines
tags: [documentation, standards, rules, workflow, bilingual]
paired_document: documentation-rules.md
parent_documents:
  - ../../project/SPEC_KOR.md
child_documents: []
references:
  - ./coding-conventions_KOR.md
  - ../architecture/layer-system_KOR.md
status: approved
---

# 문서화 표준 및 규칙

## 개요

이 문서는 HaroFramework를 위한 포괄적인 문서화 표준과 규칙을 정의합니다. 모든 문서는 프로젝트 전반에 걸쳐 일관성, 유지보수성, 접근성을 보장하기 위해 이 규칙을 따라야 합니다.

**핵심 철학**: "명확한 문서화는 효과적인 개발을 가능하게 합니다. 이중 언어 문서화는 글로벌 팀을 지원합니다. 자동화는 수동 작업을 줄입니다."

---

## 1. 이중 언어 문서화 규칙

### 1.1 황금 규칙

**모든 문서는 영어와 한국어 두 가지 언어로 반드시 작성되어야 합니다.**

이 규칙은 타협할 수 없으며 프로젝트의 모든 문서에 적용됩니다.

### 1.2 파일 이름 규칙

**원본 문서 (영어)**:
```
{document-name}.md
```

**한국어 문서**:
```
{document-name}_KOR.md
```

### 1.3 예시

```
SPEC.md                          → 원본 (영어)
SPEC_KOR.md                      → 한국어 번역

layer-system.md                  → 원본 (영어)
layer-system_KOR.md              → 한국어 번역

documentation-rules.md           → 원본 (영어)
documentation-rules_KOR.md       → 한국어 번역
```

### 1.4 동기화 요구사항

#### 언어 규칙
- **원본 문서**: 영어로 작성
- **한국어 문서**: 100% 한국어로 작성
- 두 문서 모두 언어 혼용 금지

#### 내용 연결
두 문서는 다음을 유지해야 합니다:
- 동일한 구조 (같은 제목, 섹션, 하위 섹션)
- 동등한 내용 (같은 정보, 번역됨)
- 일치하는 예시 (코드 샘플은 그대로, 주석만 번역)
- 일관된 형식 (같은 마크다운 스타일)

#### 업데이트 동기화
문서 중 하나가 업데이트될 때:
1. 변경된 모든 내용 식별
2. 쌍을 이루는 문서에 동등한 변경사항 적용
3. 두 문서의 `modified` 날짜 업데이트
4. `doc_sync.py`로 동기화 검증

### 1.5 생성 워크플로우

**새 문서를 생성할 때**:
1. 원본 문서(영어)를 먼저 작성
2. 즉시 한국어 문서 생성
3. 두 문서에 메타데이터 추가
4. `paired_document` 필드로 문서 연결
5. `doc_validate.py`로 검증

**템플릿**:
```markdown
---
title: "Document Title"
version: "1.0.0"
layer: "framework|game"
created: "2025-10-25"
modified: "2025-10-25"
paired_document: "filename_KOR.md"  # or "filename.md"
---

# Document Title

Content here...
```

---

## 2. 메타데이터 표준

### 2.1 YAML 프론트매터

모든 문서는 시작 부분에 반드시 YAML 프론트매터 메타데이터를 포함해야 합니다.

### 2.2 필수 필드

```yaml
---
title: "문서 제목"
version: "1.0.0"                    # 시맨틱 버저닝
layer: "framework|game"             # 레이어 분류
created: "YYYY-MM-DD"               # 생성 날짜
modified: "YYYY-MM-DD"              # 최종 수정 날짜
paired_document: "filename_KOR.md"  # 쌍을 이루는 문서 파일명
---
```

**필드 설명**:

**`title`** (문자열, 필수)
- 사람이 읽을 수 있는 문서 제목
- 제목 대소문자 사용
- 간결하게 유지 (< 60자)

**`version`** (문자열, 필수)
- 시맨틱 버저닝: `MAJOR.MINOR.PATCH`
- 초안은 `0.1.0`, 승인된 문서는 `1.0.0`으로 시작
- 버전 관리 섹션의 규칙 참조

**`layer`** (열거형, 필수)
- 값: `framework` 또는 `game`
- 레이어 경계 검증을 결정
- 문서 위치와 일치해야 함

**`created`** (날짜, 필수)
- ISO 8601 형식: `YYYY-MM-DD`
- 문서가 생성될 때 한 번만 설정
- 절대 변경되지 않음

**`modified`** (날짜, 필수)
- ISO 8601 형식: `YYYY-MM-DD`
- 문서가 변경될 때마다 업데이트
- 항상 created 날짜 이상

**`paired_document`** (문자열, 필수)
- 쌍을 이루는 번역 문서의 파일명
- 영어 문서: `filename_KOR.md`
- 한국어 문서: `filename.md`

### 2.3 선택적 필드

```yaml
category: "카테고리 이름"          # 문서 카테고리
tags: [tag1, tag2, tag3]           # 검색 가능한 태그
status: "draft|review|approved"    # 문서 상태
parent_documents: []               # 상위 문서 링크
child_documents: []                # 하위 문서 링크
references: []                     # 참조 문서
author: "작성자 이름"              # 문서 작성자
---
```

**필드 설명**:

**`category`** (문자열, 선택)
- 광범위한 분류
- 예시: "Guidelines", "Architecture", "API"

**`tags`** (배열, 선택)
- 검색 및 필터링을 위한 키워드
- 소문자와 하이픈 사용: `documentation-standards`

**`status`** (열거형, 선택)
- `draft`: 작업 중
- `review`: 검토 준비 완료
- `approved`: 검토 및 승인 완료
- `deprecated`: 더 이상 유효하지 않음

**`parent_documents`** (배열, 선택)
- 상위 문서로의 상대 경로
- 예시: `["../../project/SPEC.md"]`

**`child_documents`** (배열, 선택)
- 하위 문서로의 상대 경로
- 예시: `["systems/player.md"]`

**`references`** (배열, 선택)
- 참조된 문서로의 상대 경로
- 레이어 경계를 준수해야 함

**`author`** (문자열, 선택)
- 문서 작성자 또는 관리자
- 팀이 관리하는 문서의 경우 선택 사항

### 2.4 예시: 완전한 메타데이터

```yaml
---
title: "플레이어 시스템 문서"
version: "1.2.0"
layer: "framework"
created: "2025-10-20"
modified: "2025-10-25"
category: "Systems"
tags: [player, movement, input, core-system]
paired_document: "player_KOR.md"
parent_documents:
  - "../project-overview.md"
child_documents:
  - "player/movement.md"
  - "player/input.md"
references:
  - "../core/input-system.md"
  - "../architecture/layer-system.md"
status: "approved"
author: "Framework Team"
---
```

---

## 3. 버전 관리

### 3.1 시맨틱 버저닝

형식: `MAJOR.MINOR.PATCH`

### 3.2 버전 증가 규칙

**MAJOR** (X.0.0) - 다음의 경우 증가:
- 문서 구조가 크게 재구성됨
- 문서화된 인터페이스나 API의 호환성이 깨지는 변경
- 이전 이해를 무효화하는 근본적인 변경
- 하위 호환성이 깨짐
- 주요 섹션이 제거되거나 완전히 다시 작성됨

**예시**:
- 전체 문서 구조 재구성
- 핵심 개념이나 원칙 변경
- 문서화된 코드의 API 호환성을 깨는 변경

**MINOR** (x.Y.0) - 다음의 경우 증가:
- 새로운 섹션이나 챕터 추가
- 새로운 정보로 내용 확장
- 새로운 기능이나 시스템 문서화
- 하위 호환 가능한 추가
- 추가 예시나 설명

**예시**:
- 기존 섹션에 새로운 하위 섹션 추가
- 새로운 기능 문서화
- FAQ 섹션 추가
- 기존 내용 확장

**PATCH** (x.y.Z) - 다음의 경우 증가:
- 오타나 문법 오류 수정
- 예시 개선 또는 명확화
- 사소한 표현 개선
- 형식 수정
- 링크 수정
- 메타데이터 업데이트 (버전 제외)

**예시**:
- 철자 오류 수정
- 코드 예시 명확성 개선
- 깨진 링크 수정
- 형식 조정

### 3.3 버전 업데이트 프로세스

1. **변경 유형 결정**
   - 모든 변경사항 검토
   - MAJOR, MINOR, PATCH로 분류
   - 확실하지 않을 때는 높은 수준 선택

2. **메타데이터 업데이트**
   ```yaml
   version: "1.2.0"  # 이전 버전
   version: "1.3.0"  # 새 버전 (MINOR 업데이트)
   modified: "2025-10-25"  # 날짜 업데이트
   ```

3. **쌍을 이루는 문서 업데이트**
   - 쌍을 이루는 문서에도 같은 버전 적용
   - 두 문서의 버전이 일치하는지 확인
   - 두 `modified` 날짜 모두 업데이트

4. **변경사항 문서화** (선택 사항이지만 권장됨)
   - 변경 로그 항목 추가
   - 문서 상단에 중요한 변경사항 기록
   - 관련 이슈나 PR 참조

### 3.4 자동화된 버전 관리

`version_bump.py` 스크립트 사용:

```bash
# MAJOR 버전 증가
python .claude/scripts/version_bump.py {document}.md major

# MINOR 버전 증가
python .claude/scripts/version_bump.py {document}.md minor

# PATCH 버전 증가
python .claude/scripts/version_bump.py {document}.md patch
```

스크립트가 자동으로:
- 버전 번호 증가
- `modified` 날짜 업데이트
- 쌍을 이루는 문서 업데이트
- 변경 로그 항목 생성 (설정된 경우)

---

## 4. 문서 워크플로우 규칙

### 4.1 읽기 최적화 (토큰 효율성)

**규칙**: Claude Code는 원본 문서(`*.md`)만 읽고, 한국어 문서(`*_KOR.md`)는 읽지 않습니다

**근거**:
- 토큰 사용량을 약 50% 감소
- 원본 영어 문서에 모든 필요한 정보 포함
- 한국어 문서는 한국어를 선호하는 인간 독자를 위한 것
- 동일한 내용의 중복 처리 방지

**구현**:
- 문서 읽기 도구는 `*_KOR.md` 파일을 제외
- 검색 작업은 한국어 문서를 건너뜀
- 분석은 원본 문서에만 집중

**한국어 문서를 읽는 경우**:
- 사용자의 수동 요청
- 번역 검증
- 동기화 확인

### 4.2 문서 작성 및 생성

**표준 워크플로우**:

1. **계획**
   - 문서 목적과 대상 결정
   - 적절한 폴더 위치 식별
   - 유사한 문서가 있는지 확인

2. **원본 문서 생성**
   - 내용을 영어로 작성
   - 완전한 메타데이터 추가
   - 마크다운 형식 표준 준수
   - 해당되는 경우 코드 예시 포함

3. **한국어 문서 생성**
   - 내용을 한국어로 번역
   - 동일한 구조 유지
   - 코드 예시는 그대로 유지 (주석만 번역)
   - 완전한 메타데이터 추가

4. **문서 연결**
   - 메타데이터에 `paired_document` 설정
   - 상위/하위 관계 추가
   - 관련 문서에 대한 참조 추가

5. **검증**
   - `doc_validate.py` 실행
   - 깨진 링크 확인
   - 메타데이터 완전성 검증

### 4.3 문서 업데이트

**표준 워크플로우**:

1. **원본 문서 편집**
   - `*.md` 파일에 변경사항 적용
   - `modified` 날짜 업데이트
   - `version`을 적절하게 증가

2. **한국어 문서 동기화**
   - `*_KOR.md`에 동등한 변경사항 적용
   - `modified` 날짜 일치
   - `version` 번호 일치

3. **검증**
   - `doc_sync.py --check` 실행
   - `doc_validate.py` 실행
   - 동기화 검증

### 4.4 문서 삭제

**표준 워크플로우**:

1. **사용 중단으로 표시**
   - status를 `deprecated`로 업데이트
   - 상단에 사용 중단 공지 추가
   - 해당되는 경우 대체 문서 지정

2. **대기 기간**
   - 전환 기간 동안 사용 중단된 문서 유지
   - 사용자가 새 문서로 마이그레이션할 수 있도록 허용

3. **두 문서 모두 삭제**
   - 원본 문서 삭제
   - 한국어 문서 삭제
   - 다른 문서의 모든 참조 업데이트
   - `doc_validate.py` 실행하여 깨진 링크 확인

---

## 5. 컨텍스트 관리 프로토콜

### 5.1 85% 규칙

**규칙**: 컨텍스트 사용량이 85%에 도달하면 SPEC/TODO를 작성하고 `/clear` 실행

**목적**:
- 컨텍스트 오버플로우 방지
- 세션 간 연속성 보장
- Claude의 작업 메모리 유지

### 5.2 컨텍스트 모니터링

**지속적인 모니터링**:
- 모든 작업 중 토큰 사용량 추적
- 사용 비율 계산 (사용된_토큰 / 전체_토큰)
- 임계값 수준에서 경고

**임계값**:
- 🟢 **0-60%**: 정상 작업
- 🟡 **60-75%**: 마무리 계획 시작
- 🟠 **75-85%**: SPEC/TODO 업데이트 준비
- 🔴 **85%+**: SPEC/TODO 업데이트 및 `/clear` 필수

### 5.3 세션 마무리 프로세스

**85% 컨텍스트에 도달했을 때**:

1. **SPEC.md 업데이트**
   - 현재 진행 상황 문서화
   - 내린 결정 사항 기록
   - 완료된 작업 나열
   - 관련 섹션 업데이트

2. **TODO.md 업데이트**
   - 완료된 작업 표시
   - 새로 발견된 작업 추가
   - 우선순위 및 예상치 업데이트
   - 세션 복원 노트 추가

3. **한국어 문서 동기화**
   - SPEC_KOR.md 업데이트
   - TODO_KOR.md 업데이트

4. **세션 복원 가이드 생성**
   ```markdown
   ## 세션 복원
   - **마지막 세션**: 2025-10-25
   - **사용된 컨텍스트**: 170K/200K (85%)
   - **완료**: [작업 목록]
   - **다음 단계**: [다음 작업 목록]
   - **중요한 컨텍스트**: [기억해야 할 핵심 정보]
   ```

5. **`/clear` 실행**

### 5.4 세션 복원

**새 세션 시작 시**:

1. **SPEC 읽기** (원본 문서만)
2. **TODO 읽기** (원본 문서만)
3. **세션 복원 가이드 검토**
4. **마지막 체크포인트부터 계속**

---

## 6. 폴더 구조 관리

### 6.1 폴더 구성 원칙

**문서를 생성하기 전에**:
- 문서 목적과 카테고리 분석
- 사용자에게 논리적 폴더 위치 제안
- 폴더를 생성하기 전에 승인 대기
- 폴더 구조 결정 문서화

**폴더 이름 지정**:
- 소문자와 하이픈 사용: `folder-name`
- 이름을 짧지만 설명적으로 유지
- 관련 문서를 함께 그룹화
- 레이어별로 분리 (framework vs game)

### 6.2 프레임워크 문서 구조

```
.claude/framework/
├── doc/
│   ├── guidelines/              # 개발 가이드라인
│   │   ├── documentation-rules.md
│   │   ├── documentation-rules_KOR.md
│   │   ├── coding-conventions.md
│   │   └── coding-conventions_KOR.md
│   │
│   ├── architecture/            # 아키텍처 문서
│   │   ├── project-overview.md
│   │   ├── project-overview_KOR.md
│   │   ├── layer-system.md
│   │   └── layer-system_KOR.md
│   │
│   ├── systems/                 # 시스템별 문서
│   │   ├── player/
│   │   ├── ai/
│   │   ├── ui/
│   │   └── audio/
│   │
│   ├── api/                     # API 참조
│   │
│   └── workflow/                # 개발 워크플로우
│       ├── development-workflow.md
│       └── development-workflow_KOR.md
│
├── project/                     # 프로젝트 관리
│   ├── SPEC.md
│   ├── SPEC_KOR.md
│   ├── TODO.md
│   └── TODO_KOR.md
│
└── scripts/                     # 프레임워크 스크립트
    └── README.md
```

### 6.3 게임 문서 구조

```
.claude/games/
├── _template/                   # 게임 프로젝트 템플릿
│   ├── doc/
│   │   ├── design/              # 게임 디자인 문서
│   │   ├── mechanics/           # 게임플레이 메커니즘
│   │   ├── levels/              # 레벨 문서
│   │   └── assets/              # 에셋 문서
│   │
│   ├── project/
│   │   ├── SPEC.md
│   │   ├── SPEC_KOR.md
│   │   ├── TODO.md
│   │   └── TODO_KOR.md
│   │
│   └── GAME.md                  # Game Claude 설정
│
└── [game-name]/                 # 실제 게임 프로젝트
    └── (템플릿과 동일한 구조)
```

---

## 7. 문서 링크 시스템

### 7.1 링크 유형

**상위-하위 링크**:
- 계층적 관계
- 상위는 개요를 제공하고, 하위는 세부 정보를 제공
- 메타데이터 필드에 사용

**참조**:
- 관련 문서로의 교차 참조
- 계층적이지 않지만 관련된 내용
- 메타데이터 및 문서 본문에 사용

**참조 항목**:
- 추가 컨텍스트나 관련 주제
- 일반적으로 문서 끝에 위치
- 참조보다 덜 중요

### 7.2 메타데이터 링크

```yaml
parent_documents:
  - "../SPEC.md"                   # 상위로의 상대 경로

child_documents:
  - "systems/player.md"            # 하위로의 상대 경로
  - "systems/ai.md"

references:
  - "../coding-conventions.md"     # 관련 문서
  - "layer-system.md"
```

### 7.3 문서 내 링크

**상대 링크**:
```markdown
자세한 내용은 [레이어 시스템](../architecture/layer-system.md)을 참조하세요.
```

**앵커 링크** (같은 문서):
```markdown
위의 [메타데이터 표준](#메타데이터-표준) 섹션을 참조하세요.
```

**외부 링크**:
```markdown
[Unity 문서](https://docs.unity3d.com/)
```

### 7.4 레이어 인식 링크

**규칙**: 문서 링크에서 레이어 경계를 준수

**프레임워크 문서**:
```yaml
# ✅ 허용
references:
  - "./other-framework-doc.md"
  - "../guidelines/coding-conventions.md"

# ❌ 금지
references:
  - "../../games/game1/design.md"  # 게임 레이어를 참조할 수 없음
```

**게임 문서**:
```yaml
# ✅ 허용
references:
  - "./game-design.md"                         # 게임 내부
  - "../../framework/systems/player.md"        # 프레임워크 참조

# ✅ 허용 (주의 필요)
references:
  - "../other-game/shared-pattern.md"  # 게임 간 참조 (드문 경우)
```

### 7.5 링크 검증

`doc_validate.py`를 사용하여 검증:
- 모든 링크가 유효하고 접근 가능한지
- 깨진 링크가 없는지
- 레이어 경계가 준수되는지
- 양방향 링크가 일관성 있는지

```bash
python .claude/scripts/doc_validate.py
```

---

## 8. 자동화 스크립트

### 8.1 doc_sync.py - 문서 동기화

**목적**: 원본 문서와 한국어 문서 간의 동기화를 감지하고 관리합니다.

**기능**:
- 두 문서 중 하나의 변경 감지
- 내용 및 구조 비교
- 동기화가 필요할 때 알림
- 수동 동기화 워크플로우 지원

**사용법**:
```bash
# 동기화 상태 확인
python .claude/scripts/doc_sync.py --check

# 특정 문서 확인
python .claude/scripts/doc_sync.py --check SPEC.md

# 대화형 동기화 모드
python .claude/scripts/doc_sync.py --sync

# 동기화되지 않은 문서 나열
python .claude/scripts/doc_sync.py --list
```

**출력 예시**:
```
문서 동기화 확인 중...

✅ SPEC.md ↔ SPEC_KOR.md
   버전 일치: 1.0.0
   수정 날짜 일치: 2025-10-25

⚠️  TODO.md ↔ TODO_KOR.md
   버전 불일치: 1.1.0 vs 1.0.0
   수정 날짜 차이: 2025-10-25 vs 2025-10-24
   → 한국어 문서 업데이트 필요

요약: 2개의 문서 쌍 확인됨
      1개 동기화됨
      1개 주의 필요
```

### 8.2 doc_validate.py - 문서 검증

**목적**: 문서 무결성, 메타데이터 및 링크를 검증합니다.

**검사 항목**:
- 메타데이터 형식 및 필수 필드
- 쌍을 이루는 문서 존재 여부
- 링크 무결성 (깨진 링크)
- 쌍 간 버전 일관성
- 상태 필드 유효성
- 레이어 경계 위반

**사용법**:
```bash
# 모든 문서 검증
python .claude/scripts/doc_validate.py

# 특정 문서 검증
python .claude/scripts/doc_validate.py SPEC.md

# 특정 폴더 검증
python .claude/scripts/doc_validate.py --folder .claude/framework/doc/

# 메타데이터만 확인
python .claude/scripts/doc_validate.py --metadata-only

# 링크만 확인
python .claude/scripts/doc_validate.py --links-only
```

**출력 예시**:
```
문서 검증 중...

✅ SPEC.md
   메타데이터: 유효
   쌍을 이루는 문서: 발견됨 (SPEC_KOR.md)
   링크: 5개 확인됨, 모두 유효
   레이어: framework

❌ old-document.md
   오류: 메타데이터에 'version' 누락
   경고: 쌍을 이루는 문서를 찾을 수 없음
   오류: 깨진 링크: ../deleted-doc.md

요약: 10개 문서 검증됨
      9개 통과
      1개 실패
```

### 8.3 layer_validate.py - 레이어 의존성 검증

**목적**: 레이어 의존성 규칙 강제 (Framework → Game 금지).

**알고리즘**:
```python
def validate_layer_dependency(doc_path):
    # 문서 레이어 추출
    layer = get_document_layer(doc_path)

    # 모든 참조 추출
    references = extract_all_references(doc_path)

    for ref in references:
        ref_layer = get_document_layer(ref)

        # 규칙 강제: framework는 game을 참조할 수 없음
        if layer == "framework" and ref_layer == "game":
            raise DependencyViolationError(
                f"금지: Framework 문서 '{doc_path}'는 "
                f"Game 문서 '{ref}'를 참조할 수 없습니다"
            )

    return True
```

**사용법**:
```bash
# 모든 문서 검증
python .claude/scripts/layer_validate.py

# 특정 문서 검증
python .claude/scripts/layer_validate.py layer-system.md

# framework 레이어만 검증
python .claude/scripts/layer_validate.py --layer framework

# game 레이어만 검증
python .claude/scripts/layer_validate.py --layer game
```

**출력 예시**:
```
레이어 의존성 검증 중...

✅ layer-system.md (framework)
   참조: 3개 확인됨, 모든 레이어 유효

❌ bad-framework-doc.md (framework)
   오류: game 문서 '../../games/mygame/design.md' 참조
   45번째 줄: [게임 디자인 보기](../../games/mygame/design.md)

   위반: Framework 레이어는 Game 레이어를 참조할 수 없음

요약: 15개 문서 검증됨
      14개 통과
      1개 위반 발견
```

### 8.4 version_bump.py - 버전 관리

**목적**: 문서의 버전 업데이트를 자동화합니다.

**기능**:
- 버전 증가 (major/minor/patch)
- `modified` 날짜 자동 업데이트
- 쌍을 이루는 문서 버전 업데이트
- 변경 로그 항목 생성 (선택 사항)
- 일괄 버전 업데이트

**사용법**:
```bash
# patch 버전 증가
python .claude/scripts/version_bump.py SPEC.md patch

# minor 버전 증가
python .claude/scripts/version_bump.py SPEC.md minor

# major 버전 증가
python .claude/scripts/version_bump.py SPEC.md major

# 사용자 정의 메시지와 함께 업데이트
python .claude/scripts/version_bump.py SPEC.md minor --message "새 섹션 추가"

# 여러 문서 일괄 업데이트
python .claude/scripts/version_bump.py *.md patch
```

**출력 예시**:
```
SPEC.md의 버전 업데이트 중...

현재 버전: 1.0.0
새 버전: 1.1.0 (minor)

SPEC.md 업데이트됨:
  version: 1.0.0 → 1.1.0
  modified: 2025-10-24 → 2025-10-25

SPEC_KOR.md 업데이트됨:
  version: 1.0.0 → 1.1.0
  modified: 2025-10-24 → 2025-10-25

✅ 버전 업데이트 성공적으로 완료
```

---

## 9. 스크립트 우선 접근 방식

### 9.1 스크립트를 제안해야 하는 경우

**Claude는 다음의 경우 스크립트 생성을 제안해야 합니다**:
- 작업이 반복적임 (여러 번 수행될 것)
- 수동 프로세스가 오류가 발생하기 쉬움
- 작업이 여러 파일이나 복잡한 논리를 포함
- 자동화가 상당한 시간을 절약할 것
- 일관성이 중요함

**예시**:
- 문서 동기화 확인
- 일괄 메타데이터 업데이트
- 프로젝트 전체 링크 검증
- 여러 문서의 버전 업데이트
- 문서 보고서 생성

### 9.2 스크립트 제안 템플릿

**스크립트를 제안할 때**:
```markdown
[작업]을 반복적으로 수행하고 있음을 확인했습니다. 이를 자동화하기 위한 스크립트를 생성하는 것을 권장합니다.

**스크립트 목적**: [수행할 작업]
**이점**:
- [이점 1]
- [이점 2]

**사용 예시**:
```bash
python .claude/scripts/proposed_script.py [args]
```

**예상 개발 시간**: [시간 예상치]

이 스크립트를 생성하도록 진행해도 될까요?
```

### 9.3 스크립트 문서화

**모든 스크립트는 다음을 가져야 합니다**:
- 목적을 설명하는 독스트링
- 주석의 사용 예시
- 도움말 텍스트 (`--help` 플래그)
- 명확한 메시지가 있는 오류 처리
- 디버깅을 위한 로깅

**스크립트 구조 예시**:
```python
"""
doc_sync.py - 문서 동기화 도구

목적: 원본 문서와 한국어 문서 간의 동기화를 확인하고 관리합니다.

사용법:
    python doc_sync.py --check              # 모든 문서 확인
    python doc_sync.py --check SPEC.md      # 특정 문서 확인
    python doc_sync.py --sync               # 대화형 동기화 모드

작성자: HaroFramework Team
"""

import argparse
import logging

def main():
    parser = argparse.ArgumentParser(description="문서 동기화 도구")
    # ... 인자 파싱

if __name__ == "__main__":
    main()
```

---

## 10. 품질 표준

### 10.1 완전성

**모든 문서는 다음을 가져야 합니다**:
- 완전한 메타데이터 (모든 필수 필드)
- 목적을 설명하는 명확한 소개
- 제목이 있는 잘 구성된 섹션
- 적절한 경우 예시
- 관련 문서 링크
- 쌍을 이루는 번역 문서

### 10.2 정확성

**문서는 다음이어야 합니다**:
- 기술적으로 정확함
- 현재 구현과 최신 상태 유지
- 관련 문서와 일관성 있음
- 오래된 정보가 없음

### 10.3 명확성

**작성은 다음이어야 합니다**:
- 명확하고 간결함
- 잘 구성됨
- 이해하기 쉬움
- 대상 독자에게 적절함
- 전문 용어 없음 (또는 전문 용어 설명)

### 10.4 일관성

**문서는 다음을 유지해야 합니다**:
- 전체적으로 일관된 용어
- 일관된 형식 (마크다운 스타일)
- 일관된 구조 (유사한 문서는 유사한 구성 사용)
- 일관된 메타데이터 형식

---

## 11. 템플릿

### 11.1 문서 템플릿

```markdown
---
title: "[문서 제목]"
version: "0.1.0"
layer: "framework|game"
created: "YYYY-MM-DD"
modified: "YYYY-MM-DD"
category: "[카테고리]"
tags: [tag1, tag2]
paired_document: "[filename_KOR.md]"
parent_documents: []
child_documents: []
references: []
status: "draft"
---

# [문서 제목]

## 개요

[이 문서가 다루는 내용에 대한 간략한 설명]

## [주요 섹션 1]

[내용]

## [주요 섹션 2]

[내용]

## 관련 문서

- [관련 문서 1](path/to/doc1.md)
- [관련 문서 2](path/to/doc2.md)

---

**문서 상태**: 초안
**버전**: 0.1.0
**마지막 업데이트**: YYYY-MM-DD
```

### 11.2 메타데이터 템플릿

```yaml
---
title: ""
version: "0.1.0"
layer: ""
created: "YYYY-MM-DD"
modified: "YYYY-MM-DD"
category: ""
tags: []
paired_document: ""
parent_documents: []
child_documents: []
references: []
status: "draft"
---
```

---

## 12. 모범 사례

### 12.1 문서화 워크플로우

1. **작성 전에 계획**
2. **원본을 먼저 작성**
3. **즉시 번역 생성**
4. **관련 문서 연결**
5. **커밋 전에 검증**

### 12.2 유지보수

- 정기적으로 문서 검토
- 코드가 변경될 때 업데이트
- 오래된 정보 제거
- 버전 동기화 유지
- 정기적으로 링크 확인

### 12.3 협업

- 한 사람이 두 언어 버전을 모두 업데이트
- 두 버전을 함께 검토
- 변경사항 추적을 위해 버전 관리 사용
- 중요한 결정 문서화

---

## 관련 문서

- [SPEC.md](../../project/SPEC.md) - 완전한 프로젝트 사양
- [layer-system.md](../architecture/layer-system.md) - 레이어 아키텍처
- [coding-conventions.md](./coding-conventions.md) - 코드 표준

---

**문서 상태**: 승인됨
**버전**: 1.0.0
**마지막 업데이트**: 2025-10-25
