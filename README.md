# 🐧 LINUX TOOLS

[![Badge](https://img.shields.io/badge/Format-Markdown-CC33FF?logo=markdown&logoColor=white)](linux-tools.md)
[![Badge](https://img.shields.io/badge/Format-Text-CC33FF?logo=readme&logoColor=white)](/linux-tools.txt)
[![Badge](https://img.shields.io/badge/Format-JSON-CC33FF?logo=json&logoColor=white)](/linux-tools.json)
[![Badge](https://img.shields.io/badge/Format-YAML-CC33FF?logo=yaml&logoColor=white)](/linux-tools.yaml)
[![Badge](https://img.shields.io/badge/License-MIT-97CA00)](/LICENSE)
[![Badge](https://img.shields.io/badge/Python-3.6%2B-007ee7?logo=python&logoColor=white)](https://python.org)
[![Badge](https://img.shields.io/badge/-Buy%20Me%20a%20Coffee-dab728?logo=buymeacoffee&logoColor=white)](https://buymeacoffee.com/paulsorensen)

Linux Tools is a comprehensive list of applications and tools for Linux, as well as distributions.

I created this list to organize what I personally use, find useful or interesting, and to inspire others.
The project also includes a Python CLI application for managing and generating the list in multiple formats.

While I originally built the CLI to manage my Linux tools list, the application itself is generic. You're more than welcome to fork the project and use it to build and manage your own list - whether for another platform, topic, or domain.

---

## Sections

The list is structured into the following main sections:

- 🖥️ **Desktop Tools**
- 🛢️ **Server Tools**
- 💿 **Distributions**

---

## Available Formats

The list is available in the following formats for easy integration with other applications:

- [Markdown](/linux-tools.md)
- [Text](/linux-tools.txt)
- [JSON](/linux-tools.json)
- [YAML](/linux-tools.yaml)

---

## CLI Application

To organize the list I've built a CLI application in Python, which is included in this repository.

![CLI Preview](/assets/cli-preview.png)

### Features

- Add sections, categories, and tools.
- Delete sections, categories, and tools.
- By default, sections, categories, tools, and tags are sorted alphabetically in the output.
- Sections and categories can be manually reordered by priority.
- Generate output in Markdown, Text, JSON, and YAML formats.
- MVC-like project structure with helper classes for clean code organization.

### Data Handling

- **Section names and category names** are sanitized to title case, keeping minor words (like "and", "or", "the") in lowercase (unless they are the first word), and preserving acronyms.
- **Tool titles** are sanitized so that each word starts with an uppercase letter, except for minor words (unless first), and the remaining letters are left as entered.
- **Descriptions** are sanitized to capitalize the first word.
- **URLs** are stored in lowercase and automatically prefixed with `https://` if missing.
- **Tags** are stored in lowercase.

---

### Key Data Files

- [data/structure.yaml](/data/structure.yaml) – Section and category structure.
- [data/tools.yaml](/data/tools.yaml) – List of all tools.
- [data/acronyms.txt](/data/acronyms.txt) – Acronyms.
- [data/minor_words.txt](/data/minor_words.txt) – List of minor words.

---

### Requirements

- **Python 3.6 or newer**
- **ruamel.yaml**

---

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/paulsorensen/linux-tools.git
   cd linux-tools
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   > `ruamel.yaml` is the only required third-party dependency.

---

### Usage

- **Run the CLI application:**

  ```bash
  ./run.sh
  ```

  or

  ```bash
  python linux-tools.py
  ```

- **See the generated outputs** in the project root after using the CLI.

---

## Author

**Paul Sørensen**  

- Website: [https://paulsorensen.io](https://paulsorensen.io)  
- GitHub: [https://github.com/paulsorensen](https://github.com/paulsorensen)

---

## Support

If you found this project useful, a small tip is appreciated ❤️  
[https://buymeacoffee.com/paulsorensen](https://buymeacoffee.com/paulsorensen)

## License

This project is licensed under the MIT License.  
See [LICENSE](LICENSE) for details.

---
