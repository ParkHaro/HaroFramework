---
title: "Project Overview"
version: "1.0.0"
scope: "framework"
created: "2025-10-25"
modified: "2025-10-25"
category: "Architecture"
tags: [architecture, overview, structure, unity]
paired_document: "project-overview_KOR.md"
parent_documents:
  - "../../project/SPEC.md"
child_documents: []
references:
  - "../guidelines/coding-conventions.md"
  - "../workflow/development-workflow.md"
  - "./scope-system.md"
status: "approved"
---

# Project Overview

## Project Information

- **Project Name**: HaroFramework
- **Unity Version**: 6000.2.9f1 (Unity 6)
- **Render Pipeline**: Universal Render Pipeline (URP) 17.2.0
- **C# Version**: Modern C# features supported by Unity 6
- **Target Platforms**: Multi-platform (PC, Mac, Linux by default)

## Key Technologies

### Unity Packages
- **Input System** (1.14.2) - New Input System for player input
- **URP** (17.2.0) - Universal Render Pipeline for rendering
- **AI Navigation** (2.0.9) - NavMesh and pathfinding
- **Timeline** (1.8.9) - Animations and cutscenes
- **Visual Scripting** (1.9.8) - Visual scripting system
- **UI** (2.0.0) - Unity UI system
- **Test Framework** (1.6.0) - Automated testing

### Development Tools
- Unity Editor - Primary development environment
- Git - Version control
- Claude Code - AI-assisted development

## Project Structure

```
HaroFramework/
├── Assets/
│   ├── Scenes/              # Unity scenes
│   ├── Scripts/             # C# source code
│   │   ├── Runtime/         # Runtime code (to be organized)
│   │   ├── Editor/          # Editor-only code (to be organized)
│   │   └── Tests/           # Test code (to be organized)
│   ├── Settings/            # Project settings (URP, Input, etc.)
│   └── TutorialInfo/        # Unity tutorial assets (removable)
├── Packages/
│   └── manifest.json        # Package dependencies
├── ProjectSettings/         # Unity project settings
├── .claude/                 # Claude Code configuration
│   ├── commands/            # Slash commands
│   ├── skills/              # Auto-activated skills
│   └── doc/                 # Project documentation
└── CLAUDE.md               # Main guidance for Claude Code
```

## Architecture Goals

HaroFramework aims to provide:
- **Modular Design**: Component-based architecture
- **Data-Driven**: ScriptableObject-based configuration
- **Testable**: Comprehensive test coverage
- **Maintainable**: Clear structure and documentation
- **Performant**: Optimized for target platforms

## Development Workflow

1. **Planning**: Define feature requirements
2. **Implementation**: Write code following conventions
3. **Testing**: Create automated tests
4. **Documentation**: Document public APIs
5. **Review**: Code review and validation
6. **Integration**: Merge to main branch

## Build System

Currently using Unity Editor for builds. Command-line builds to be configured.

## Testing Strategy

- **Edit Mode Tests**: Pure C# logic tests
- **Play Mode Tests**: Runtime behavior tests
- **Integration Tests**: System interaction tests
- **Performance Tests**: Performance benchmarks

## Version Control

- **Main Branch**: `main`
- **Strategy**: Feature branches
- **Commit Style**: Descriptive commit messages
- **.gitignore**: Standard Unity .gitignore (to be verified)

## Related Documentation

- [SPEC.md](../../project/SPEC.md) - Complete project specification
- [Scope System](./scope-system.md) - 2-Scope architecture
- [Coding Conventions](../guidelines/coding-conventions.md) - Code standards
- [Development Workflow](../workflow/development-workflow.md) - Development process

---

**Document Status**: Approved
**Version**: 1.0.0
**Last Updated**: 2025-10-25
