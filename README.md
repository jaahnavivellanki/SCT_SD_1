# 🌡️ TempCraft

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/GUI-CustomTkinter-1f538d?style=for-the-badge" alt="CustomTkinter Badge"/>
</div>

<br>

**TempCraft** is a premium, beautifully crafted desktop application for seamless temperature conversion. Designed with a meticulous focus on modern UI/UX principles, TempCraft moves away from traditional, archaic desktop layouts, delivering a sleek, dark-themed experience that feels like a next-generation software product.

---

## 💼 Resume-Ready Project Description

> **TempCraft - Modern Desktop Application**  
> Developed a responsive, feature-rich desktop application using Python and CustomTkinter. Engineered a modular architecture to support real-time input validation, session-based conversion history, clipboard integration, and CSV data export. Designed a highly polished, asynchronous UI featuring custom themes, dynamic scaling, and error handling, showcasing a strong command of object-oriented programming, event-driven design, and modern UX/UI standards.

---

## ✨ Features

- **Real-Time Validation**: Instant visual feedback on input validity.
- **Session History & Export**: Automatically logs conversions with timestamps and allows exporting data to CSV.
- **Quick Actions**: Swap units instantly, copy results to the clipboard with one click, and trigger conversions via the `Enter` key.
- **Dynamic Layout**: A professional, responsive card-based layout (900x650) that adjusts elegantly.
- **Rich Notifications**: In-app popups and status messages for a smooth user experience.
- **Modern Aesthetics**: Built with CustomTkinter for rounded corners, cohesive color palettes, hover effects, and a premium dark mode.

---

## 📸 Screenshots

*(Replace placeholders with actual images of your application)*

| Main Converter View | History & Export |
| :---: | :---: |
| ![Converter Placeholder](assets/converter_view.png) | ![History Placeholder](assets/history_view.png) |

---

## 🛠️ Technologies Used

- **Python 3.x**: Core application logic and event handling.
- **CustomTkinter**: Modern GUI rendering, theming, and widget creation.
- **Standard Libraries**: `datetime` (timestamps), `csv` (data export), `tkinter` (clipboard and dialogs).

---

## 📂 Project Structure

```text
TempCraft/
├── main.py              # Application entry point
├── README.md            # Project documentation
├── assets/              # Icons and screenshots
│   └── app_icon.ico
```
*(Note: As the project grows, UI components will be abstracted into dedicated modules.)*

---

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/TempCraft.git
   cd TempCraft
   ```

2. **Set up a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install customtkinter
   ```

---

## 🎮 Usage

1. Run the application from your terminal:
   ```bash
   python main.py
   ```
2. Type a temperature value in the input field.
3. Select your Source and Target units.
4. Press `Enter` or click the **Convert** button.
5. Use the **Copy** button to save the result, or view the history panel on the right!

---

## 🔮 Future Enhancements

- **Persistent Storage**: Save conversion history to a local SQLite database across sessions.
- **Additional Units**: Implement support for Rankine and Delisle scales.
- **Theming Options**: Add a settings menu to let users toggle between Dark, Light, and System themes, or define custom accent colors.
- **Advanced Math Parsing**: Allow users to type simple equations (e.g., `20+5`) in the input field.

---
<div align="center">
  <i>Created with ☕ and Python by <a href="https://github.com/yourusername">Your Name</a></i>
</div>
