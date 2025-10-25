---
title: "프로젝트 개요"
version: "1.0.0"
scope: "framework"
created: "2025-10-25"
modified: "2025-10-25"
category: "Architecture"
tags: [architecture, overview, structure, unity]
paired_document: "project-overview.md"
parent_documents:
  - "../../project/SPEC_KOR.md"
child_documents: []
references:
  - "../guidelines/coding-conventions_KOR.md"
  - "../workflow/development-workflow_KOR.md"
  - "./scope-system_KOR.md"
status: "approved"
---

# 프로젝트 개요

## 프로젝트 정보

- **프로젝트 이름**: HaroFramework
- **Unity 버전**: 6000.2.9f1 (Unity 6)
- **렌더 파이프라인**: Universal Render Pipeline (URP) 17.2.0
- **C# 버전**: Unity 6에서 지원하는 최신 C# 기능
- **타겟 플랫폼**: 멀티플랫폼 (기본적으로 PC, Mac, Linux)

## 핵심 기술

### Unity 패키지
- **Input System** (1.14.2) - 플스코프 입력을 위한 새로운 Input System
- **URP** (17.2.0) - 렌더링을 위한 Universal Render Pipeline
- **AI Navigation** (2.0.9) - NavMesh 및 경로 찾기
- **Timeline** (1.8.9) - 애니메이션 및 컷신
- **Visual Scripting** (1.9.8) - 비주얼 스크립팅 시스템
- **UI** (2.0.0) - Unity UI 시스템
- **Test Framework** (1.6.0) - 자동화된 테스트

### 개발 도구
- Unity Editor - 주요 개발 환경
- Git - 버전 관리
- Claude Code - AI 보조 개발

## 프로젝트 구조

```
HaroFramework/
├── Assets/
│   ├── Scenes/              # Unity 씬
│   ├── Scripts/             # C# 소스 코드
│   │   ├── Runtime/         # 런타임 코드 (구성 예정)
│   │   ├── Editor/          # 에디터 전용 코드 (구성 예정)
│   │   └── Tests/           # 테스트 코드 (구성 예정)
│   ├── Settings/            # 프로젝트 설정 (URP, Input 등)
│   └── TutorialInfo/        # Unity 튜토리얼 에셋 (제거 가능)
├── Packages/
│   └── manifest.json        # 패키지 의존성
├── ProjectSettings/         # Unity 프로젝트 설정
├── .claude/                 # Claude Code 설정
│   ├── commands/            # 슬래시 명령
│   ├── skills/              # 자동 활성화 스킬
│   └── doc/                 # 프로젝트 문서
└── CLAUDE.md               # Claude Code를 위한 주요 가이드
```

## 아키텍처 목표

HaroFramework는 다음을 제공하는 것을 목표로 합니다:
- **모듈식 디자인**: 컴포넌트 기반 아키텍처
- **데이터 중심**: ScriptableObject 기반 구성
- **테스트 가능**: 포괄적인 테스트 커버리지
- **유지보수 가능**: 명확한 구조 및 문서화
- **성능 최적화**: 타겟 플랫폼에 최적화

## 개발 워크플로우

1. **계획**: 기능 요구사항 정의
2. **구현**: 규칙을 따라 코드 작성
3. **테스트**: 자동화된 테스트 생성
4. **문서화**: 공개 API 문서화
5. **검토**: 코드 검토 및 검증
6. **통합**: 메인 브랜치에 병합

## 빌드 시스템

현재 Unity Editor를 사용하여 빌드합니다. 커맨드라인 빌드는 구성 예정입니다.

## 테스트 전략

- **Edit Mode 테스트**: 순수 C# 로직 테스트
- **Play Mode 테스트**: 런타임 동작 테스트
- **통합 테스트**: 시스템 상호작용 테스트
- **성능 테스트**: 성능 벤치마크

## 버전 관리

- **메인 브랜치**: `main`
- **전략**: 기능 브랜치
- **커밋 스타일**: 설명적인 커밋 메시지
- **.gitignore**: 표준 Unity .gitignore (검증 예정)

## 관련 문서

- [SPEC.md](../../project/SPEC_KOR.md) - 완전한 프로젝트 사양
- [스코프 시스템](./scope-system_KOR.md) - 2-Scope 아키텍처
- [코딩 규칙](../guidelines/coding-conventions_KOR.md) - 코드 표준
- [개발 워크플로우](../workflow/development-workflow_KOR.md) - 개발 프로세스

---

**문서 상태**: 승인됨
**버전**: 1.0.0
**마지막 업데이트**: 2025-10-25
