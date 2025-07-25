# BEAM - Assistive AI for Accessibility

## Overview
**BEAM** (Blind, Echo, Assist, Motion) is an open-source AI toolkit designed to assist people with disabilities such as blindness, deafness, muteness, and hand amputation. This personal project aims to explore how AI can help restore independence through smart automation, voice interfaces, visual assistance, and accessibility training.

⚠️ **Note**: This is a prototype and personal project that is not actively maintained or updated. It serves primarily as a proof of concept.

## ✨ Features
* **Blind Assistance**: Voice-controlled navigation, screen reading, object detection
* **Deaf Assistance**: Real-time speech-to-text conversion, emergency alerts
* **Muteness Assistance**: Text-to-speech interfaces for communication
* **Hand Amputation Assistance**: Full voice-based control of the Windows environment, automation of common tasks
* **Training Tools**: Keyboard practice and accessibility training for skill development
* **Modular AI Control**: Easily toggle features on/off via `ai_toggle_config.json`

## 📂 Project Structure
```
BEAM/
├── Blind - Zarah/
│   └── (Blindness-related tools)
├── Deaf - Echo/
│   └── (Deafness-related tools)
├── Hand Amputation - Hollow/
│   └── (Hand amputation assistive tools)
├── gui.py
├── keyboardtraining.py
├── ai_toggle_config.json
└── README.md
```

## 🚀 Getting Started

### Prerequisites
* Python 3.10 or newer
* Pip (Python package installer)
* Windows 10/11 (full support)

### Installation
1. **Clone the repository**
```bash
git clone https://github.com/Its-BB/BEAM.git
cd BEAM
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```
*(Note: Since this is a prototype project, you may need to manually install dependencies like `speechrecognition`, `opencv-python`, `pyttsx3`, and `tkinter` as needed)*

3. **Run the GUI**
```bash
python gui.py
```

## ⚙️ Configuration
You can control which assistive AIs are active using the `ai_toggle_config.json` file. Example:
```json
{
{"Zarah": false,
"Ava": false,
"Echo": false,
"Hollow": false,
"BlindKeyboardTraining": false}
}
```

## 🛠️ Development
This project is modular. Each disability category has its own folder where you can extend or improve individual AI components.
* New AI models can easily be added
* Feature toggles allow lightweight operation

## 📜 License
This project is licensed under the MIT License.


## 🚨 Disclaimer
BEAM is a prototype personal project and is **not a medical device**. It was created as an exploration of accessibility technology and is not intended for critical use cases. Always consult professional accessibility solutions when necessary.
