<p align="center">
  <img src="https://github.com/user-attachments/assets/8a6e42ae-14ed-43b7-b3f3-3ed52e880e22" alt="İstinye Üniversitesi" width="300"/>
</p>

### 👤 Proje Bilgileri

| | |
|---|---|
| **Öğrenci** | Gizem Kızılay |
| **Danışman Eğitmen** | Keyvan Arasteh Abbasabad |
| **Üniversite** | İstinye Üniversitesi |
| **Ders** | Tersine Mühendislik (Reverse Engineering) |

# 🛡️ Form Attack: Stored XSS & Defense-in-Depth Architecture

![Python](https://img.shields.io/badge/Language-Python_3.9+-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Framework-Flask-000000?style=flat-square&logo=flask&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)
[![Python Build](https://github.com/gizemkizilay/form-saldirisi/actions/workflows/python-app.yml/badge.svg)](https://github.com/gizemkizilay/form-saldirisi/actions)

[🇹🇷 Türkçe](#turkce) | [🇬🇧 English](#english)

---

<a id="turkce"></a>
## 🇹🇷 Türkçe

Bu proje, modern web uygulamalarında en sık rastlanan ve kritik sonuçlar doğuran **Stored XSS (Kalıcı Cross-Site Scripting)** zafiyetini simüle eden ve bu saldırıya karşı endüstri standardı olan **"Defense-in-Depth" (Derinlemesine Savunma)** stratejilerini uygulamalı olarak gösteren bir web güvenliği laboratuvarıdır.

### 🚀 Özellikler
* **Korumasız Ortam Simülasyonu (`/vulnerable`):** Girdi temizleme (sanitization) süreçlerinin eksik bırakıldığı, Jinja2 şablon motorunda `| safe` filtresinin kullanılarak XSS saldırısına bilerek kapı açıldığı zafiyetli mod.
* **Güvenli Ortam Simülasyonu (`/secure`):** Hem istemci (Frontend) hem de sunucu (Backend) tarafında güvenlik kalkanlarının aktif olduğu korumalı mod.
* **İstemci Taraflı Doğrulama (Frontend Validation):** Form gönderilmeden önce çalışan JavaScript fonksiyonu (`validateForm`) ile `<` ve `>` karakterlerinin anlık denetimi.
* **Sunucu Taraflı Temizleme (Backend Sanitization):** `html.escape()` metodu kullanılarak zararlı payload'ların HTML encode işlemine tabi tutulması ve düz metne (plain text) çevrilmesi.

### 🛡️ MITRE ATT&CK Matrisi

| ID | İsim | Açıklama |
| :--- | :--- | :--- |
| **T1190** | Exploit Public-Facing Application | Web uygulamasındaki girdi denetimi (Input Validation) eksikliğinin istismar edilmesi. |
| **T1059.007**| Command and Scripting Interpreter: JavaScript | Tarayıcı üzerinde zararlı JS payload'larının (XSS) otonom olarak çalıştırılması. |
| **T1539** | Steal Web Session Cookie | Başarılı bir Stored XSS saldırısı sonucu yetkilendirme çerezlerinin (Cookie) çalınması simülasyonu. |
| **T1189** | Drive-by Compromise | Zafiyetli `/vulnerable` sayfasını ziyaret eden kullanıcıların tarayıcılarında zararlı kodun otomatik tetiklenmesi. |

### ⚙️ Neden Python ve Flask?
Siber güvenlik "Proof of Concept" (PoC) çalışmalarında, sistemin arka planında nelerin olup bittiğini şeffaf bir şekilde görebilmek çok önemlidir. Python Flask mikro-framework'ü, gereksiz karmaşıklıktan uzak yapısıyla güvenlik zafiyetlerinin temel nedenlerini (Root Cause) izole etmeyi sağlar. Jinja2 şablon motoru, `| safe` filtresi gibi yapılarıyla "Auto-Escaping" mekanizmalarının kapatılıp açılabilmesine olanak tanıyarak, savunma katmanlarının etkisini net bir şekilde kanıtlar.

### 📊 Beklenen Derinlik ve Özdeğerlendirme
Web güvenliğinde sadece tek bir noktada (örneğin sadece Frontend JavaScript ile) kontrol yapılması asla yeterli değildir. Saldırganların aracı yazılımlar (Proxy/Burp Suite vb.) ile Frontend kontrollerini kolayca atlatabileceği varsayılmıştır. Bu nedenle projenin mimarisi, güvenliğin asıl merkezi olan sunucu tarafında (Backend) temizleme işlemini zorunlu kılan bir yaklaşımla inşa edilmiştir.

### 🛠 Kurulum ve Kullanım

```bash
# Gereksinimleri yükleyin
pip install -r requirements.txt

# Uygulamayı başlatın
python app.py
