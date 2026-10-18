<div align="center">

<img src="git-images/Icon.png" alt="Logo of EGEOSPACE (PRIVATE) LIMITED" width="150" height="150" style="margin: 24px 0;">
<h1>MD2P3 Project</h1>

[![Issues](https://img.shields.io/github/issues/egeospace-lab/md2p3)](https://github.com/egeospace-lab/md2p3/issues)
[![Licence](https://img.shields.io/badge/licence-MIT-blue)](LICENSE.md)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](#)
[![Contributors](https://img.shields.io/github/contributors/egeospace-lab/md2p3)](CONTRIBUTING.md)

The **md2p3** project is an open‑source Python tool by **EGEOSPACE (PRIVATE) LIMITED** that transforms Markdown files into professional PowerPoint presentations.  

It is designed for educators, professionals, and teams who want to automate the creation of structured, visually consistent presentations.

[Visit the Website](https://www.egeospace.in/) · [Report a Bug](https://github.com/egeospace-lab/md2p3/issues) · [Request a Feature](https://github.com/egeospace-lab/md2p3/issues)

</div>

## Table of Contents
- [About the Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [First Conversion](#first-conversion)
- [Usage](#usage)
- [Contributing](#contributing)
- [Security](#security)
- [Licence](#licence)
- [Contact](#contact)

## About the Project

The **md2p3** project provides a reliable Markdown‑to‑PowerPoint converter with enterprise‑grade slide mapping and formatting utilities.  

**Key Features:**
- Convert Markdown files into structured PowerPoint decks  
- Support configurable Slide Maps and custom templates  
- Provide extensible slide classes (Cover, Agenda, Theme, Content, Final)  
- Preserve Markdown formatting (bold, italic, inline code) inside slides  

### Built With
- [Python](https://www.python.org/)  
- [python-pptx](https://python-pptx.readthedocs.io/)  
- [markdown-it-py](https://markdown-it-py.readthedocs.io/)  
- [Regex](https://docs.python.org/3/library/re.html)  

## Getting Started

Follow these steps to set up **md2p3** locally and run your first conversion.

### Prerequisites
- Python 3.10+  
- pip package manager  
- VS Code or any preferred editor  

### Installation
1. Clone the repository:  
   ```sh
   git clone https://github.com/egeospace-lab/md2p3.git
   ```
2. Install dependencies:  
   ```sh
   pip3 install -r requirements.txt
   ```
3. Verify the installation:  
   ```sh
   python3 -m bin.view-layout
   ```

### First Conversion
1. Place your Markdown files inside the `markdown/` folder.  
2. Ensure the Slide Map file (`conf/slide-maps/template-pptx.json`) is configured.  
3. Run the conversion:  
   ```sh
   python3 -m bin.md2p3 --src markdown --destination dist
   ```
4. Your PowerPoint deck will be available in the `dist/` folder.

## Usage

### Inspecting PPTX Templates with `view-layout`
Before creating or editing a Slide Map, inspect the PowerPoint template to identify layout indices and placeholder positions.

Run:
```sh
python3 -m bin.view-layout -t template/template.pptx
```

### Converting Markdown to PPTX with `md2p3`
Typical use cases:
- Convert Markdown lecture notes into slides  
- Generate structured presentations with agenda, themes, and content slides  
- Automate documentation into visual decks  

Example:
```sh
python3 -m bin.md2p3 --src markdown --destination dist
```

## Contributing

We welcome contributions from approved stakeholders. Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.  

## Security

Please see [SECURITY.md](SECURITY.md) for vulnerability reporting and disclosure guidelines.  

## Licence

This project is licensed under the terms of the **MIT Licence**.  
See [LICENCE.md](LICENCE.md) for details.  

## Contact

**EGEOSPACE (PRIVATE) LIMITED**  
Uthaya Bhavanam  
Mathagal West, Mathagal  
Jaffna, Northern Province 40000  
Sri Lanka  

[md2p3@egeospace.in](mailto:md2p3@egeospace.in)
