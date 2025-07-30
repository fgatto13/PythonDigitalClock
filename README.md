# Python Digital Clock ⏰
**Made using PyQt5**

A minimal desktop digital clock built with PyQt5, featuring a custom 7-segment-style font, dynamic layout, and robust exception handling. This project demonstrates modular GUI programming, file-based logging, and safe resource loading.

---

## 🚀 Features

- **Live digital clock** updating every second
- **Custom digital font** (`DS-DIGIT.TTF`) applied using Qt's font database
- **Exception-safe font loading** with automatic fallback to the system font
- **Auto-generated log files** with detailed error tracebacks (timestamped)
- Clean GUI with:
  - Centered layout
  - HSL color styling
  - Dark background for high contrast

---

## 🗂 Project Structure

```
PythonDigitalClock/
├── main.py              # Entry point – sets up logging and launches the app
├── digitalClock.py      # Contains the DigitalClock widget (UI + logic)
├── logConfig.py         # Handles timestamped log file setup
├── fonts/
│   └── ds_digital/
│       └── DS-DIGIT.TTF # Custom font file
├── logs/                # Automatically created log files for each run
└── README.md            # You're here :)
```

---

## 🧠 How It Works

### Font Loading
The clock uses a custom font (`DS-DIGIT.TTF`) to mimic a digital display. Font loading is handled through `QFontDatabase`. If the font fails to load (e.g., missing, corrupt, unreadable), the program:

- Logs the error to a **timestamped file** (inside `/logs`)
- Falls back to a **default system font**
- Keeps the application running safely

### Logging
- Logs are saved to `/logs/clock_YYYY-MM-DD_HH-MM-SS.log`
- Only **errors and critical issues** are logged
- Output is sent to both:
  - A file for persistent inspection
  - The console for real-time debugging

---

## 🔧 Requirements

- Python 3.7+
- PyQt5

Install dependencies with:

```bash
pip install PyQt5
```

---

## ▶️ Running the App

Make sure you're in the root folder:

```bash
python main.py
```

A new log file will be created automatically in the `logs/` folder each time you run the app.

---

## 📁 Fonts

The custom font is located at:

```
fonts/ds_digital/DS-DIGIT.TTF
```

You can replace it with any `.ttf` file of your choice by modifying the path inside `load_font()`.

---

## 🛡️ Exception Handling

Exception types handled during font loading:
- `FileNotFoundError` – if the font file is missing
- `IndexError` – if no font families are returned after loading
- `RuntimeError` – raised manually when font registration fails
- `OSError` – if the file is corrupted or locked

These are caught gracefully and logged via Python’s `logging` module.

---

## 🧑‍💻 Author

Built by @fgatto13, based on the work made by BroCode.  
Cleanly written and modularized to demonstrate PyQt5 best practices.
