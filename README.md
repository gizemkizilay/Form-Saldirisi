<img width="1280" height="305" alt="İstinye_Üniversitesi_logo svg" src="https://github.com/user-attachments/assets/8a6e42ae-14ed-43b7-b3f3-3ed52e880e22" />


# 🛡️ XSS Analizi ve Çok Katmanlı Savunma Mekanizmaları

[![Python Build](https://github.com/gizemkizilay/form-saldirisi/actions/workflows/python-app.yml/badge.svg)](https://github.com/gizemkizilay/form-saldirisi/actions/workflows/python-app.yml)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey.svg)

Bu proje, modern web uygulamalarında en sık rastlanan zafiyetlerden biri olan **Stored XSS (Kalıcı Cross-Site Scripting)** saldırısını simüle etmek ve bu saldırıya karşı geliştirilen çok katmanlı savunma stratejilerini (Defense-in-Depth) uygulamalı olarak göstermek amacıyla geliştirilmiştir.

---

## 👨‍🏫 Akademik Bilgiler
* **Üniversite:** İstinye Üniversitesi
* **Ders:** Güvenli Web Yazılım Geliştirme
* **Danışman Eğitmen:** Keyvan Arasteh Abbasabad
* **Geliştirici:** Gizem Kızılay

---

## 📖 İçindekiler
1. [Proje Özeti ve Amacı](#1-proje-özeti-ve-amacı)
2. [Teknik Uygulama Detayları](#2-teknik-uygulama-detayları)
3. [Savunma Stratejileri](#3-savunma-stratejileri)
4. [Kurulum ve Kullanım](#4-kurulum-ve-kullanım)
5. [Beklenen Derinlik ve Özdeğerlendirme](#5-beklenen-derinlik-ve-özdeğerlendirme)
6. [Yasal Uyarı](#6-yasal-uyarı)

---

## 1. Proje Özeti ve Amacı
Uygulama, **Python Flask** framework'ü ve **SQLite** veritabanı kullanılarak geliştirilmiş bir yorum paneli simülasyonudur. Projenin temel amacı, bir web uygulamasının girdi temizleme (sanitization) süreçleri eksik bırakıldığında oluşabilecek güvenlik risklerini ve bu risklerin hem istemci hem de sunucu tarafında nasıl bertaraf edileceğini kanıtlamaktır.

## 2. Teknik Uygulama Detayları
Sistem iki temel çalışma modundan oluşmaktadır:

* **Zafiyetli Mod (`/vulnerable`):** Kullanıcıdan gelen veriler doğrudan veritabanına kaydedilir. Jinja2 şablon motorunda kullanılan `| safe` filtresi, tarayıcının veriyi HTML olarak işlemesine izin vererek XSS saldırısına kapı açar.
* **Güvenli Mod (`/secure`):** Veriler veritabanına yazılmadan önce encode edilir ve görüntüleme aşamasında otomatik kaçış (escaping) mekanizmaları devrededir.

## 3. Savunma Stratejileri
Projede **"Defense-in-Depth"** prensibi uyarınca iki aşamalı koruma uygulanmıştır:

* **A. İstemci Taraflı Doğrulama (Frontend):** `validateForm()` JavaScript fonksiyonu ile form gönderilmeden önce `<` ve `>` karakterleri denetlenir. Bu, ilk savunma hattıdır.
* **B. Sunucu Taraflı Temizleme (Backend):** JavaScript engellerinin aşılması ihtimaline karşı Python tarafında `html.escape()` metodu kullanılır. `<script>` gibi etiketler `&lt;script&gt;` formatına çevrilerek zararsız düz metin haline getirilir.

## 4. Kurulum ve Kullanım

```bash
# Gereksinimleri yükleyin
pip install -r requirements.txt

# Uygulamayı başlatın
python app.py
```
Uygulama başlatıldıktan sonra tarayıcı üzerinden şu adreslere erişilebilir:
* **Zafiyetli Panel:** `http://127.0.0.1:5000/vulnerable`
* **Güvenli Panel:** `http://127.0.0.1:5000/secure`

## 5. Beklenen Derinlik ve Özdeğerlendirme
* **1. Neden Bu Yaklaşım Seçildi?:** Web güvenliğinde sadece tek bir noktada (örneğin sadece frontend) kontrol yapılması yeterli değildir. Saldırganların aracı yazılımlar (Proxy) ile frontend kontrollerini atlatabileceği varsayılarak, güvenliğin asıl merkezi olan sunucu tarafında temizleme işlemi zorunlu kılınmıştır.
* **2. Ana Güvenlik Sonuçları:** Yapılan testlerde, `| safe` filtresinin kaldırılması ve `html.escape()` kullanımı ile XSS saldırı vektörlerinin tamamen etkisiz hale getirildiği, zararlı scriptlerin tarayıcı tarafından çalıştırılamadığı gözlemlenmiştir.
* **3. Genişletilebilirlik:** Proje, üretim ortamında **Content Security Policy (CSP)** başlıklarının eklenmesi ve daha gelişmiş bir SQL Injection koruması sağlayan ORM yapılarına geçiş yapılarak genişletilebilir.

## 6. Yasal Uyarı
Bu proje, İstinye Üniversitesi bünyesinde tamamen eğitim ve araştırma (Proof of Concept) amacıyla geliştirilmiştir. Kötü niyetli kullanımlarda sorumluluk geliştiriciye ait değildir.
