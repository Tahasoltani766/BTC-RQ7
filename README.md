# BTC-RQ7

[🇬🇧 English](README.md) | [🇮🇷 فارسی](README.fa.md)

> ⚠️ **WARNING: This repository contains a malware sample for cybersecurity research and educational purposes. Do NOT execute it on a personal, production, or otherwise trusted system.**

## 🦠 Overview

**BTC-RQ7** is a cybersecurity research project demonstrating how malicious cryptomining activity can be disguised as a seemingly legitimate cryptocurrency wallet-related utility.

The project was created to demonstrate a common social-engineering and malware-delivery concept:

**A malicious payload is presented to the user as a legitimate security/cryptocurrency utility while performing unauthorized activity in the background.**

The primary purpose of releasing this project as Open Source is **security awareness, malware analysis, detection engineering, and defensive research**.

This project is **not intended to be used for unauthorized access, resource theft, cryptojacking, or deployment against systems without explicit authorization.**

---

## 🎯 Research Objectives

BTC-RQ7 was developed to demonstrate:

* How malicious software can be disguised as a legitimate application
* How cryptocurrency-themed tools can be abused as a delivery mechanism
* How unauthorized cryptomining activity may remain hidden from the user
* What artifacts and behaviors defenders can investigate
* How SOC analysts can identify suspicious process and resource activity
* How malware analysis can be used to improve endpoint detection capabilities

The goal is to help security researchers and defenders understand **how seemingly legitimate tools can hide malicious behavior**.

---

## 🔬 High-Level Attack Flow

The project demonstrates a simplified attack chain:

```text
User
  │
  ▼
Fake / Malicious Wallet Utility
  │
  ├──► Legitimate-looking functionality
  │
  └──► Hidden malicious execution
             │
             ▼
        Cryptomining Activity
             │
             ▼
      Unauthorized Resource Usage
```

The important security lesson is that **the visible functionality of an application does not necessarily represent its complete behavior**.

---

## 🧩 Project Components

| Component               | Purpose                                           |
| ----------------------- | ------------------------------------------------- |
| `cracker_wallet/`       | Wallet-related / malicious application components |
| `form_windos/`          | Windows application interface/components          |
| `miner_runer/`          | Component associated with miner execution         |
| `review_target_system/` | Target-system inspection/review functionality     |
| `server/`               | Supporting server-side components                 |
| `main.py`               | Main application entry point                      |
| `balance_generator.py`  | Generates simulated wallet/balance data           |
| `bal.json`              | Example wallet/balance data                       |

> Component names and behavior are provided for research and analysis purposes.

---

## 🛡️ What Defenders Should Look For

Security teams analyzing similar malware should pay attention to behavioral indicators rather than trusting the application's appearance.

Potential detection opportunities include:

### Process Activity

Look for:

* Unexpected high-CPU processes
* Unknown executables launched by user-facing applications
* Child processes that do not logically belong to the parent application
* Executables running from unusual directories
* Processes with suspicious command-line arguments

### System Resource Usage

Cryptominers commonly produce noticeable resource consumption.

Potential indicators include:

```text
High CPU utilization
Unexpected GPU utilization
Sustained resource consumption
Performance degradation
Abnormal fan activity
Unexpected power consumption
```

### Network Activity

Investigate:

* Unexpected outbound connections
* Connections to mining infrastructure
* Persistent connections from applications that normally should not communicate externally
* Suspicious DNS requests
* Unusual destination ports or protocols

### Persistence

Defenders should also investigate whether suspicious components attempt to survive:

* Reboots
* User logoff
* Application termination

---

## 🔍 Malware Analysis

For safe analysis, use an isolated laboratory environment.

Recommended setup:

```text
                    ┌─────────────────────┐
                    │   Analysis Host     │
                    │                     │
                    │  Windows VM         │
                    │  Procmon             │
                    │  Process Explorer    │
                    │  Wireshark           │
                    │  Sysmon              │
                    │  x64dbg              │
                    │  Autoruns            │
                    └──────────┬──────────┘
                               │
                         Isolated Network
                               │
                    ┌──────────▼──────────┐
                    │  Analysis / Logging │
                    │      Systems        │
                    └─────────────────────┘
```

Recommended precautions:

* Use a disposable virtual machine
* Take a VM snapshot before analysis
* Do not use personal wallets or credentials
* Do not connect the VM to a trusted corporate network
* Monitor network traffic
* Monitor process creation
* Monitor filesystem changes
* Monitor registry modifications
* Destroy/revert the VM after analysis

---

## 🧪 Defensive Research Use Cases

This repository can be used as a controlled sample for:

* Malware analysis training
* SOC analyst training
* EDR detection development
* SIEM use-case development
* Threat hunting
* Behavioral detection research
* Incident response exercises
* Endpoint telemetry analysis
* Cybersecurity awareness demonstrations

For example, a SOC team could build detections around:

```text
Suspicious Parent → Child Process
        +
High CPU Utilization
        +
Unexpected Network Connection
        +
Unknown Executable
```

This combination can provide a stronger detection signal than relying on a single indicator.

---

## 🚨 Disclaimer

This repository contains potentially malicious code.

The code is published **strictly for cybersecurity research, education, malware analysis, and defensive purposes**.

Do not use this project to:

* Deploy malware against systems you do not own
* Consume another user's computing resources
* Perform unauthorized cryptomining
* Evade security controls
* Obtain unauthorized access
* Damage systems or data

Only analyze or execute the software in an isolated environment where you have explicit authorization.

The author is not responsible for damage, data loss, unauthorized access, resource consumption, or any other consequences resulting from the misuse of this repository.

---

## 📚 Why Open Source It?

Malware becomes more dangerous when defenders cannot easily understand how it works.

By publishing this project openly, the intention is to allow security researchers, SOC analysts, students, and defenders to:

> **Inspect the code → understand the behavior → build detections → improve defenses.**

The objective is not to make malware more effective.

The objective is to make defenders **more aware of how seemingly legitimate applications can hide malicious behavior.**

---

## 👨‍💻 Author

**Taha Soltani**

Cybersecurity Researcher

Interested in:

* Security Research
* SOC & SIEM
* Malware Analysis
* Threat Detection
* Security Automation
* AI for Cybersecurity
* Open Source Security

---

## ⭐ Security Research

If you are a security researcher or SOC analyst, feel free to use this project as a controlled sample for defensive research and detection engineering.

**Stay curious. Stay defensive. 🛡️**
