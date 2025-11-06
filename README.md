# **Task Manager CLI**

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

A command-line task manager with persistent storage, priority tracking, and completion status - built with pure Python.

![Task Manager Demo](demo/demo-task.gif)

## **Features** ✨

- **CRUD Operations**: Create, Read, Update, Delete tasks
- **Priority System**: LOW, MEDIUM, HIGH, URGENT
- **Visual Status**: Color-coded completion (✅/⏳)
- **Persistent Storage**: JSON-based data persistence
- **User-Friendly CLI**: Intuitive menu system

## **Installation** 🛠️

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/task-manager-cli.git
   cd task-manager-cli
   ```
2. **Set up environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```

## **Usage** 🚀
```bash
python src/main.py
```

### **Menu Options**:
1. 🖨 Show tasks
2. ➕ Add new task
3. 🗑 Delete task
4. ✔ Mark task complete
5. ☢ Delete all tasks
6. 🚪 Exit

## **Project Structure** 📂
```text
task-manager-cli/
├── src/
│   ├── main.py              # Entry point
│   ├── task_functions.py    # Core logic
│   └── file_operations.py   # JSON persistence
├── data/
│   └── tasks.json           # Task storage
├── tests/                   # (Future test directory)
├── requirements.txt
└── README.md
```

## **Technical Highlights** 💻

- **Pure Python**: No external dependencies (except `colorama` for UI)
- **Clean Architecture**: Separation of concerns (UI/Logic/Data)
- **Type Hints**: Better code maintainability
- **Cross-Platform**: Works on Windows, Linux, and macOS

## **Roadmap** 🗺️

Planned improvements:
- [ ] Add due date notifications
- [ ] Implement task categories
- [ ] Add export to CSV/Excel
- [ ] Develop GUI version
- [ ] Build test suite

## **How to Contribute** 🤝

We welcome contributions! Please see our [Contribution Guidelines](CONTRIBUTING.md) and:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## **License** 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

> **Note**: This is an active development project. Expect regular updates and improvements!