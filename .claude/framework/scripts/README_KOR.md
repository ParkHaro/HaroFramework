# HaroFramework 문서화 자동화 스크립트

HaroFramework 문서 품질 및 일관성 유지를 위한 자동화 스크립트 모음입니다.

## 사용 가능한 스크립트

### 1. `layer_validate.py` - 레이어 의존성 검증기

2-layer 아키텍처 규칙 강제: Framework 문서는 Game 문서를 참조할 수 없습니다.

**사용법:**
```bash
# 기본 검증
python layer_validate.py

# 상세 진행 상황 표시
python layer_validate.py --verbose
```

**검증 항목:**
- Framework 문서가 Game 레이어 문서를 참조하지 않는지 확인
- `references`와 `parent_documents` 필드의 참조 검사

**종료 코드:**
- `0` - 모든 레이어 의존성이 올바름
- `1` - 위반 사항 발견

---

### 2. `doc_validate.py` - 문서 메타데이터 검증기

문서 메타데이터 형식 및 링크 무결성을 검증합니다.

**사용법:**
```bash
# 기본 검증
python doc_validate.py

# 상세 진행 상황 표시
python doc_validate.py --verbose

# 경고를 오류로 처리
python doc_validate.py --strict
```

**검증 항목:**
- ✅ 필수 메타데이터 필드 (title, version, layer 등)
- ✅ 버전 형식 (MAJOR.MINOR.PATCH)
- ✅ 유효한 상태 값 (draft/review/approved/deprecated/active)
- ✅ 쌍 문서 존재 여부
- ✅ 참조 링크 무결성
- ✅ 부모 문서 존재 여부

**종료 코드:**
- `0` - 모든 문서 유효
- `1` - 오류 발견 (또는 strict 모드에서 경고)

---

### 3. `doc_sync.py` - 문서 동기화 검사기

원본 문서가 한글 번역보다 최신인 경우를 감지합니다.

**사용법:**
```bash
# 기본 검사
python doc_sync.py

# 상세 진행 상황 표시
python doc_sync.py --verbose
```

**검사 항목:**
- 문서 쌍 간의 `modified` 날짜 비교
- 업데이트가 필요한 번역 식별

**종료 코드:**
- `0` - 모든 번역이 동기화됨
- `1` - 동기화되지 않은 문서 발견

---

### 4. `version_bump.py` - 버전 관리

문서 버전 번호를 증가시키고 수정 날짜를 업데이트합니다.

**사용법:**
```bash
# patch 버전 증가 (1.0.0 -> 1.0.1)
python version_bump.py framework/doc/architecture/layer-system.md patch

# minor 버전 증가 (1.0.0 -> 1.1.0)
python version_bump.py framework/doc/architecture/layer-system.md minor

# major 버전 증가 (1.0.0 -> 2.0.0)
python version_bump.py framework/doc/architecture/layer-system.md major

# 드라이 런 (수정 없이 변경 사항 표시)
python version_bump.py framework/doc/architecture/layer-system.md patch --dry-run
```

**기능:**
- 버전 번호 증가 (major/minor/patch)
- `modified` 날짜를 오늘로 업데이트
- 짝이 되는 한글 문서 자동 업데이트

**버전 증가 규칙:**
- **major**: 호환성이 깨지는 변경, 주요 재구성 (1.0.0 -> 2.0.0)
- **minor**: 새로운 내용, 중요한 추가 (1.0.0 -> 1.1.0)
- **patch**: 오타 수정, 사소한 명확화 (1.0.0 -> 1.0.1)

---

## 권장 워크플로우

### 1. 변경 사항 커밋 전

```bash
# 레이어 의존성 검증
python layer_validate.py

# 메타데이터 및 링크 검증
python doc_validate.py

# 번역 동기화 확인
python doc_sync.py
```

커밋 전에 모든 스크립트가 통과해야 합니다.

### 2. 문서 업데이트 후

```bash
# 버전 증가 (적절한 타입 선택)
python version_bump.py framework/doc/architecture/layer-system.md patch

# 변경 사항 검증
python doc_validate.py
```

### 3. CI/CD 통합 (향후)

pre-commit hook 또는 CI 파이프라인에 추가:
```bash
#!/bin/bash
cd .claude/framework/scripts

python layer_validate.py || exit 1
python doc_validate.py --strict || exit 1
python doc_sync.py || exit 1

echo "[+] 모든 검증 검사 통과"
```

---

## 스크립트 요구사항

- **Python**: 3.7+
- **의존성**: 없음 (Python 표준 라이브러리만 사용)
- **플랫폼**: 크로스 플랫폼 (Windows, macOS, Linux)

---

## 파일 구조

```
.claude/framework/scripts/
├── README.md              # 영문 가이드
├── README_KOR.md          # 이 파일 (한글 가이드)
├── layer_validate.py      # 레이어 의존성 검증기
├── doc_validate.py        # 메타데이터 검증기
├── doc_sync.py            # 동기화 검사기
└── version_bump.py        # 버전 관리 도구
```

---

## 문제 해결

### ".claude 디렉토리를 찾을 수 없습니다"

**해결책**: HaroFramework 프로젝트 디렉토리 내에서 스크립트를 실행하세요.

```bash
cd /path/to/HaroFramework
python .claude/framework/scripts/layer_validate.py
```

### "frontmatter를 찾을 수 없습니다"

**해결책**: 문서에 YAML frontmatter가 있는지 확인하세요:

```markdown
---
title: "문서 제목"
version: "1.0.0"
layer: "framework"
created: "2025-10-26"
modified: "2025-10-26"
category: "Architecture"
tags: [tag1, tag2]
paired_document: "document_KOR.md"
parent_documents: []
child_documents: []
references: []
status: "approved"
---

# 문서 내용
```

### "잘못된 버전 형식"

**해결책**: 버전은 `MAJOR.MINOR.PATCH` 형식을 따라야 합니다:
- ✅ `1.0.0`
- ✅ `2.3.1`
- ❌ `1.0` (patch 누락)
- ❌ `v1.0.0` ('v' 접두사 없음)

---

## 향후 개선 사항

계획된 개선 사항:
- [ ] 일반적인 문제에 대한 자동 수정 모드
- [ ] 버전 증가로부터 CHANGELOG 자동 생성
- [ ] 자동화된 번역 동기화 추적
- [ ] GitHub Actions 통합
- [ ] Pre-commit hook 템플릿
- [ ] 관련 문서의 일괄 버전 증가

---

## 관련 문서

- [문서화 규칙](../doc/guidelines/documentation-rules_KOR.md) - 문서화 표준
- [레이어 시스템](../doc/architecture/layer-system_KOR.md) - 2-layer 아키텍처
- [SPEC_KOR.md](../project/SPEC_KOR.md) - 프로젝트 명세
- [TODO_KOR.md](../project/TODO_KOR.md) - 작업 추적

---

**마지막 업데이트**: 2025-10-26
**관리자**: HaroFramework Team
