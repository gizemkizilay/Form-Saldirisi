# 🛡️ Web Güvenliği Vize Projesi: XSS Analizi ve Savunma Mekanizmaları

Bu proje, modern web uygulamalarında en kritik zafiyetlerden biri olan **Stored XSS (Kalıcı Cross-Site Scripting)** saldırısını simüle etmek ve bu saldırıya karşı geliştirilen çok katmanlı savunma stratejilerini uygulamalı olarak göstermek amacıyla hazırlanmıştır.

---

## 📝 Proje Genel Bakışı
Uygulama, **Python Flask** framework'ü kullanılarak geliştirilmiş bir yorum paneli simülasyonudur. Sistem iki temel moddan oluşmaktadır:

1.  **Zafiyetli Mod (`/vulnerable`):** Girdilerin temizlenmeden işlendiği ve saldırıya açık olan bölüm.
2.  **Güvenli Mod (`/secure`):** Hem istemci (Frontend) hem de sunucu (Backend) tarafında koruma kalkanlarının devrede olduğu bölüm.

---

## 🚀 Teknik Uygulama Detayları

### 1. Zafiyet Senaryosu ve İstismar (Exploit)
Zafiyetli rotada, kullanıcıdan gelen veriler doğrudan veritabanına kaydedilir. 
* **Zafiyet Nedeni:** Jinja2 şablon motorunda kullanılan `| safe` filtresi, tarayıcının veriyi HTML olarak işlemesine izin verir.
* **Saldırı Vektörü:**
    ```html
    <script>alert('Sistem Güvenliği İhlal Edildi!');</script>
    ```
* **Sonuç:** Bu kod yüklendiğinde, sayfayı ziyaret eden her kullanıcının tarayıcısında bir uyarı penceresi açılır. Bu, kötü niyetli bir saldırganın oturum çerezlerini (cookies) çalabileceğini kanıtlar.

---

### 2. Savunma Stratejileri (Güvenli Mod)
Güvenli rotada **"Defense-in-Depth" (Derinlemesine Savunma)** prensibi uygulanmıştır:

#### A. İstemci Taraflı Doğrulama (Frontend Validation)
Kullanıcı formu göndermeden önce çalışan JavaScript fonksiyonu, girdi içerisinde `<` ve `>` karakterlerini kontrol eder.
* **Fonksiyon:** `validateForm()`
* **Etki:** Zararlı karakter tespit edilirse formun sunucuya gitmesi engellenir.

#### B. Sunucu Taraflı Temizleme (Backend Sanitization)
Eğer saldırgan JavaScript engelini aşarsa (örneğin Proxy araçları kullanarak), sunucu tarafında Python devreye girer.
* **Kullanılan Metot:** `html.escape()`
* **Dönüşüm:** `<` karakteri `&lt;`, `>` karakteri `&gt;` formatına çevrilir.
* **Sonuç:** Tarayıcı bu veriyi bir "kod" olarak değil, "düz metin" olarak görür. Böylece saldırı kodu çalışmaz hale gelir.

---

## 🛠️ Kurulum ve Kullanım

1.  **Gereksinimleri Yükle:**
    ```bash
    pip install flask
    ```
2.  **Uygulamayı Başlat:**
    ```bash
    python app.py
    ```
3.  **Test Adresleri:**
    * **Zafiyetli Panel:** `http://127.0.0.1:5000/vulnerable`
    * **Güvenli Panel:** `http://127.0.0.1:5000/secure`

---

## 📊 Sonuç ve Değerlendirme
Bu proje kapsamında yapılan testler sonucunda, güvenli bir web mimarisinde sadece kullanıcı arayüzü kontrollerinin yeterli olmadığı, asıl güvenliğin **sunucu tarafında (Backend)** yapılan veri temizleme işlemleriyle sağlandığı doğrulanmıştır.

---
**Hazırlayan:** Gizem Kızılay 

**Ders:** Güvenli Web Geliştirme (Vize Ödevi)
