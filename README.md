# 📡 Wi-Fi Network Scanner (Python)

A simple Python application that scans and displays nearby Wi-Fi networks detected by your computer's wireless adapter.

## ✨ Features

* 📶 Scan nearby Wi-Fi networks
* 📡 Display SSID (Network Name)
* 🔒 Show Authentication & Encryption Type
* 📍 Display BSSID (MAC Address)
* 📊 Show Signal Strength
* 📻 Display Channel & Frequency (platform dependent)
* ⚡ Lightweight and beginner-friendly

---

## 📂 Project Structure

```text
wifi-scanner/
│
├── wifi_scanner.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🛠 Requirements

* Python 3.8+
* Windows (using `netsh`) or Linux (using `pywifi`)
* Wireless network adapter

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/swarupdhar011-sketch/wifi-scanner.git
```

Go to the project folder:

```bash
cd wifi-scanner
```

Install dependencies (Linux version):

```bash
pip install pywifi
```

---

## ▶️ Usage

Run the scanner:

```bash
python wifi_scanner.py
```

Example output:

```text
SSID          : Home_WiFi
Signal        : 85%
Authentication: WPA2-Personal
Encryption    : CCMP
Channel       : 6
-----------------------------------
SSID          : CoffeeShop
Signal        : 62%
Authentication: Open
Encryption    : None
```

---

## ⚙️ How It Works

The application uses your computer's wireless adapter to scan for nearby Wi-Fi networks.

* **Windows:** Uses the built-in `netsh` command.
* **Linux:** Uses the `pywifi` library.

No data is transmitted externally, and the application only displays information that your operating system already makes available.

---

## 🔒 Privacy & Security

This project is intended for educational purposes and personal network management.

It **does not**:

* Recover or reveal Wi-Fi passwords
* Connect to networks automatically
* Interfere with wireless networks
* Perform hacking or penetration testing

The scanner only lists Wi-Fi networks that your device can detect.

---

## 🚀 Future Improvements

* GUI with Tkinter or CustomTkinter
* Export scan results to CSV or JSON
* Real-time network monitoring
* Signal strength visualization
* Automatic network refresh
* Cross-platform support improvements

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful:

* ⭐ Star the repository
* 🍴 Fork the project
* 💡 Suggest improvements by opening an issue

Happy Coding! 🚀
