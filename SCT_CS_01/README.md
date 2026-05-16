# 🔐 SecureText Studio - Caesar Cipher Tool

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **SkillCraft Technology Cybersecurity Internship - Task 01**

A modern, interactive web application for Caesar Cipher encryption/decryption with advanced features including brute-force attack simulation and frequency analysis.

![SecureText Studio](https://img.shields.io/badge/Status-Production-success)

## 🌟 Features

### ⚡ Core Functionality
- **Encrypt & Decrypt**: Apply Caesar cipher with customizable shift values (1-25)
- **Interactive Cipher Wheel**: Visual representation of letter substitution with drag-to-rotate functionality
- **Real-time Statistics**: Character count, letter frequency, and cipher alphabet mapping

### 💥 Security Analysis
- **Brute-Force Attack Simulation**: Automatically tests all 25 possible shifts
- **Intelligent Scoring**: Uses English letter frequency analysis and common word matching
- **Confidence Rating**: AI-powered scoring to identify the most likely plaintext

### 📊 Frequency Analysis
- **Visual Comparison**: Side-by-side bar charts comparing text frequency vs. standard English
- **Pattern Detection**: Identify encryption signatures through statistical analysis
- **Educational Tool**: Understand why simple substitution ciphers are cryptographically weak

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.8 or higher
pip (Python package manager)
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/manasvi-0523/SCT_CS_01.git
cd SCT_CS_01
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run app.py
```

4. **Open your browser**
```
The app will automatically open at http://localhost:8501
```

## 📖 Usage Guide

### Encryption/Decryption
1. Enter your message in the input text area
2. Select a shift value (1-25) using the slider
3. Click **🔒 Encrypt** or **🔓 Decrypt**
4. View the result with detailed statistics

### Brute-Force Attack
1. Navigate to the **💥 Brute-Force Attack** tab
2. Paste encrypted text
3. Click **Run Brute-Force Attack**
4. Review all 25 candidates ranked by likelihood

### Frequency Analysis
1. Go to the **📊 Frequency Analysis** tab
2. Paste any text (plain or encrypted)
3. Click **Run Frequency Analysis**
4. Compare letter distribution against English baseline

## 🏗️ Project Structure

```
SCT_CS_01/
├── app.py                 # Main Streamlit application
├── caesar.py              # Core cipher logic and algorithms
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## 🛠️ Technical Details

### Algorithms Implemented
- **Caesar Cipher**: Classic shift cipher with modular arithmetic
- **Frequency Analysis**: Chi-squared distance calculation
- **Word Matching**: Dictionary-based plaintext detection
- **Hybrid Scoring**: Combined frequency + word match algorithm

### Technologies Used
- **Streamlit**: Modern web framework for data apps
- **Matplotlib**: Statistical visualization
- **NumPy**: Numerical computations
- **Python 3.8+**: Core programming language

## 📊 Performance

- **Encryption Speed**: O(n) - Linear time complexity
- **Brute-Force**: Tests all 25 shifts in < 1 second
- **Memory Usage**: Minimal - processes text in-place
- **Browser Compatibility**: All modern browsers supported

## 🎓 Educational Value

This project demonstrates:
- ✅ Classical cryptography concepts
- ✅ Cryptanalysis techniques (frequency analysis, brute-force)
- ✅ Why simple substitution ciphers are insecure
- ✅ Statistical analysis in cryptography
- ✅ Modern web application development

## 🔒 Security Note

⚠️ **Educational Purpose Only**: The Caesar cipher is **NOT secure** for real-world use. It's trivially broken by:
- Brute-force (only 25 possible keys)
- Frequency analysis
- Known-plaintext attacks

For actual security needs, use modern encryption standards like AES-256.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Manasvi**
- GitHub: [@manasvi-0523](https://github.com/manasvi-0523)
- Project: SkillCraft Technology Cybersecurity Internship

## 🙏 Acknowledgments

- SkillCraft Technology for the internship opportunity
- Classical cryptography research and educational resources
- Streamlit community for excellent documentation

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

<div align="center">
  <strong>Built with ❤️ for cybersecurity education</strong>
</div>
