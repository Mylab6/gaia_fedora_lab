# GAIA UI Documentation

## Table of Contents
- [GAIA UI Documentation](#gaia-ui-documentation)
  - [Table of Contents](#table-of-contents)
- [UI Overview](#ui-overview)
- [Qt Interface](#qt-interface)
  - [Prerequisites](#prerequisites)
  - [Using Qt Designer](#using-qt-designer)
    - [Launching Qt Designer](#launching-qt-designer)
    - [Editing the UI](#editing-the-ui)
    - [Working with Assets](#working-with-assets)
  - [Compiling Changes](#compiling-changes)
  - [Troubleshooting](#troubleshooting)
- [GAIA UI Interface](#raux-interface)
  - [New in GAIA UI (RAUX)](#new-in-gaia-beta-raux)
- [License](#license)

# UI Overview

GAIA provides a single modern user interface:
- **GAIA UI (RAUX)** - A modern Electron-based desktop application providing an intuitive interface for GAIA

# Installation

Install GAIA UI on Windows and Ubuntu using the packages from the GitHub [Releases](https://github.com/amd/gaia/releases) page.

## Supported platforms
- Windows 11 (64-bit) - Full GUI and CLI support
- Linux: Ubuntu 22.04 LTS / 24.04 LTS / Fedora 38+ (64-bit) - Full GUI and CLI support

## Windows (.exe)
1. Download the latest `gaia-ui-setup.exe` from [Releases](https://github.com/amd/gaia/releases).
2. Double-click `gaia-ui-setup.exe` and follow the prompts.
3. Launch GAIA UI from the Start Menu (search for "GAIA UI") or the desktop shortcut.
4. On first launch, setup may take a moment. An internet connection is required the first time.
5. Updating: download the newer `gaia-ui-setup.exe` from [Releases](https://github.com/amd/gaia/releases) and run it.
6. Uninstalling: Windows Settings → Apps → Installed apps → find "GAIA UI" → Uninstall.

## Linux Installation

### Ubuntu/Debian (.deb)
1. Download the latest `gaia-ui-setup.deb` (amd64) from [Releases](https://github.com/amd/gaia/releases).
2. Open a terminal in the folder where you downloaded the package, then install with apt:
```bash
sudo apt update
sudo apt install ./gaia-ui-setup.deb
```
3. Launch GAIA UI from your application menu (search for "GAIA UI").
4. On first launch, setup may take a moment. An internet connection is required the first time.
5. Updating: download the newer .deb file and install it again with apt (same command as above).
6. Uninstalling:
```bash
sudo apt remove gaiaui
```

### Fedora/RHEL (.rpm)
1. Download the latest `gaia-ui-setup.rpm` (x86_64) from [Releases](https://github.com/amd/gaia/releases).
2. Open a terminal in the folder where you downloaded the package, then install with dnf:
```bash
sudo dnf install ./gaia-ui-setup.rpm
```
3. Launch GAIA UI from your application menu (search for "GAIA UI").
4. On first launch, setup may take a moment. An internet connection is required the first time.
5. Updating: download the newer .rpm file and install it again with dnf (same command as above).
6. Uninstalling:
```bash
sudo dnf remove gaiaui
```

**Note:** Both .deb and .rpm packages are automatically built using Electron Forge and published to GitHub releases. See the [Building Packages](#building-packages) section for building locally.

# GAIA UI (RAUX) Interface

**GAIA UI (also referred to as RAUX for RyzenAI User Experience)** is a modern Electron-based desktop application that provides the primary interface for GAIA. Built as a fork from [Open-WebUI](https://github.com/open-webui/open-webui), it delivers an extensible, feature-rich, and user-friendly AI platform experience. GAIA UI is actively developed with regular feature updates and improvements.

## New in GAIA UI (RAUX)
- Improved error handling and progress reporting via inter-process communication (IPC) between the main and renderer processes.
- Unified GAIA UI branding and updated messaging throughout the installer and UI.

### 🙏 **Acknowledgments: RAUX & OpenWebUI**

#### **Built on OpenWebUI Foundation**

RAUX (RyzenAI UX) is built upon the excellent foundation provided by **OpenWebUI**, an outstanding open-source project that has revolutionized how users interact with AI models through web interfaces.

#### **Special Thanks**

We extend our heartfelt gratitude to:

- **[Timothy Jaeryang Baek](https://github.com/tjbck)** and the entire **OpenWebUI team** for creating and maintaining such an exceptional open-source project
- The **OpenWebUI community** for their continuous contributions, feedback, and innovation
- All **open-source contributors** who have helped shape the modern AI interface landscape

#### **Open Source Heritage**

GAIA UI builds upon OpenWebUI's solid architectural foundation while adding AMD-specific optimizations and integrations tailored for the GAIA ecosystem. This collaboration exemplifies the power of open-source software in advancing AI accessibility and user experience. The OpenWebUI project's commitment to creating intuitive, powerful, and extensible AI interfaces has made GAIA UI possible. 

**Learn more about OpenWebUI**: [https://github.com/open-webui/open-webui](https://github.com/open-webui/open-webui)

---

For more information about GAIA UI (RAUX), including setup instructions and feature documentation, please refer to the [RAUX GitHub repository README](https://github.com/aigdat/raux/blob/main/README.md).

# Building Packages

GAIA uses Electron Forge to build desktop application packages for multiple platforms. The build system automatically generates platform-specific installers.

## Building RPM and DEB Packages

The GAIA Electron apps (like JAX - Jira Agent Experience) are configured to build both .deb (Debian/Ubuntu) and .rpm (Fedora/RHEL) packages automatically.

### Prerequisites

- Node.js 20+
- npm

### Build Process

1. Navigate to the app directory:
```bash
cd src/gaia/apps/jira/webui  # or any other app
```

2. Install dependencies:
```bash
npm ci
```

3. Build all packages:
```bash
npm run make
```

This will generate packages in `out/make/`:
- **DEB package**: `out/make/deb/x64/*.deb` (for Ubuntu/Debian)
- **RPM package**: `out/make/rpm/x64/*.rpm` (for Fedora/RHEL)
- **Windows installer**: `out/make/squirrel.windows/x64/*.exe`

### Package Configuration

The packages are configured in each app's `package.json` using Electron Forge makers:

```json
{
  "makers": [
    {
      "name": "@electron-forge/maker-deb",
      "config": {},
      "platforms": ["linux"]
    },
    {
      "name": "@electron-forge/maker-rpm",
      "config": {},
      "platforms": ["linux"]
    }
  ]
}
```

### CI/CD Automation

The `.github/workflows/build-electron-apps.yml` workflow automatically builds packages for all platforms on every commit:

- **Windows**: .exe installer via Squirrel
- **Linux**: Both .deb and .rpm packages

Packages are uploaded as GitHub Actions artifacts and can be published to releases.

### Testing Packages Locally

**Test .deb package (Ubuntu/Debian):**
```bash
sudo apt install ./out/make/deb/x64/*.deb
```

**Test .rpm package (Fedora):**
```bash
sudo dnf install ./out/make/rpm/x64/*.rpm
```

# License

[MIT License](../LICENSE.md)

Copyright(C) 2024-2025 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: MIT
