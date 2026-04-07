# Katkıda Bulunma Kılavuzu (Contributing Guidelines)

Öncelikle bu projeye zaman ayırdığınız ve katkıda bulunmayı düşündüğünüz için teşekkür ederiz! 🎉

Bu proje, web güvenliği ve XSS (Cross-Site Scripting) zafiyetleri üzerine akademik bir simülasyon olarak geliştirilmiştir. Açık kaynak topluluğunun katkıları, bu simülasyonun daha eğitici ve kapsamlı olmasına yardımcı olacaktır. Lütfen katkıda bulunmadan önce aşağıdaki adımları ve kuralları okuyun.

## Nasıl Katkıda Bulunabilirsiniz?

### 🐛 Hata (Bug) Bildirimi
Eğer projede bir hata bulursanız veya savunma mekanizmalarını (Backend Sanitization) aşan yeni bir XSS vektörü keşfederseniz:
1. Öncelikle projenin `Issues` sekmesini kontrol ederek bu hatanın daha önce bildirilip bildirilmediğine bakın.
2. Eğer bildirilmemişse, yeni bir Issue açın ve oluşturduğumuz `Bug Report` şablonunu kullanın.
3. Hatayı nasıl yeniden üretebileceğimizi (reproduce) adım adım açıklayın ve mümkünse ekran görüntüsü ekleyin.

### 💡 Yeni Özellik Talebi
Simülasyona eklenmesini istediğiniz yeni özellikler veya farklı web zafiyeti türleri (SQLi, CSRF vb.) için:
1. Yeni bir Issue açın.
2. Bu özelliğin neden faydalı olacağını ve projenin akademik amacına nasıl hizmet edeceğini detaylandırın.

### 🛠️ Pull Request (PR) Gönderme
Koda doğrudan katkıda bulunmak isterseniz, lütfen şu profesyonel iş akışını izleyin:
1. Bu depoyu kendi hesabınıza "Fork" edin.
2. Kendi bilgisayarınızda yeni bir dal (branch) oluşturun: `git checkout -b ozellik/yeni-ozellik-adi`
3. Değişikliklerinizi yapın ve yerel ortamda test edin.
4. Kodunuzu commit edin. Anlamlı commit mesajları kullanmaya özen gösterin: `git commit -m "feat: xss filtresi için yeni regex eklendi"`
5. Kendi deponuza pushlayın: `git push origin ozellik/yeni-ozellik-adi`
6. Orijinal depoya gelerek bir "Pull Request" oluşturun ve değişikliklerinizi detaylıca açıklayın.

## Geliştirme Ortamı Kurulumu
Projeyi yerel bilgisayarınızda çalıştırmak için `README.md` dosyasındaki kurulum adımlarını takip edebilir veya sağladığımız `docker-compose.yml` dosyasını kullanarak projeyi anında ayağa kaldırabilirsiniz.

## Güvenlik Bildirimleri
Eğer projede kritik bir güvenlik açığı bulursanız, lütfen bunu açık bir Issue olarak paylaşmak yerine `SECURITY.md` dosyamızdaki yönergeleri izleyerek doğrudan iletişime geçin.

Desteğiniz ve katkılarınız için tekrar teşekkürler!
