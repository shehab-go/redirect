# 📱 Droidify Redirector

مشروع ويب بسيط يقوم بتوجيه روابط تطبيقات Android من المتصفح إلى تطبيق Android عبر Deep Links.

A simple web project that redirects Android app links from the browser to the Android app via Deep Links.

## 📋 الوصف / Description

هذا المشروع يعمل كوسيط (redirector) بين روابط HTTP/HTTPS وتطبيق Android (Droidify). عند زيارة رابط معين، يقوم الموقع بإنشاء Deep Link وفتح التطبيق مباشرة.

This project works as a redirector between HTTP/HTTPS links and the Android app (Droidify). When visiting a specific link, the site creates a Deep Link and opens the app directly.

## 🎯 الوظيفة الأساسية / Main Functionality

عند زيارة رابط مثل:
When visiting a link like:

```
https://droidify.eu.org/app/?id=com.example.app&repo_address=https://repo.example.com/repo
```

يتم تنفيذ التالي:
The following is executed:

1. ✅ استخراج المعاملات من URL (`id` و `repo_address`)
   Extract parameters from URL (`id` and `repo_address`)

2. ✅ إنشاء Deep Link: `fdroid.app://com.example.app?repo_address=https://repo.example.com/repo`
   Create Deep Link: `fdroid.app://com.example.app?repo_address=https://repo.example.com/repo`

3. ✅ محاولة فتح التطبيق مباشرة
   Attempt to open the app directly

4. ✅ إذا فشل (بعد timeout)، عرض رابط Google Play Store كبديل
   If failed (after timeout), show Google Play Store link as fallback

## 📝 المعاملات / Parameters

- **`id`** (مطلوب / Required): package name للتطبيق (مثال: `com.example.app`)
- **`repo_address`** (اختياري / Optional): عنوان المستودع الكامل (مثال: `https://myrepo.com/fdroid/repo`)

## 📁 هيكل المشروع / Project Structure

```
droidify-redirector/
│
├── app/
│   └── index.html              # الصفحة الرئيسية / Main page
│
├── .well-known/
│   └── assetlinks.json        # Android App Links configuration
│
├── README.md                   # هذا الملف / This file
│
├── .htaccess                   # Apache configuration (optional)
│
└── robots.txt                  # SEO configuration (optional)
```

## 💻 تشغيل الخادم المحلي / Running Local Server

### الطريقة السريعة (Windows)
**Quick Method (Windows)**

1. انقر نقراً مزدوجاً على ملف `start.bat`
   Double-click `start.bat` file

2. سيفتح المتصفح تلقائياً على: `http://localhost:8000/app/`
   Browser will open automatically at: `http://localhost:8000/app/`

### الطريقة السريعة (Linux/Mac)
**Quick Method (Linux/Mac)**

```bash
chmod +x start.sh
./start.sh
```

### الطريقة اليدوية (جميع الأنظمة)
**Manual Method (All Systems)**

```bash
python server.py
```

أو:
Or:

```bash
python3 server.py
```

بعد التشغيل، افتح المتصفح على:
After running, open browser at:

```
http://localhost:8000/app/
```

### اختبار الروابط
**Test Links**

- رابط بسيط:
  ```
  http://localhost:8000/app/?id=com.example.app
  ```

- رابط مع repo:
  ```
  http://localhost:8000/app/?id=com.example.app&repo_address=https://repo.example.com/fdroid/repo
  ```

### الوصول من أجهزة أخرى على نفس الشبكة
**Access from Other Devices on Same Network**

1. **افتح جدار الحماية:**
   Open firewall:

   - **Windows:** شغّل `open-firewall.ps1` كمسؤول (Right-click > Run as Administrator)
   - **Windows:** Run `open-firewall.ps1` as Administrator
   - أو اتبع التعليمات في ملف `فتح-جدار-الحماية.md`
   - Or follow instructions in `فتح-جدار-الحماية.md` file

2. **تأكد أن كلا الجهازين على نفس الشبكة (WiFi/LAN)**
   Make sure both devices are on the same network (WiFi/LAN)

3. **استخدم IP الشبكة:**
   Use network IP:
   ```
   http://192.168.20.186:8000/app/
   ```
   (سيظهر IP الخاص بك في نافذة الخادم)
   (Your IP will be shown in the server window)

4. **من الجهاز الآخر، افتح المتصفح واذهب إلى:**
   From the other device, open browser and go to:
   ```
   http://[YOUR_IP]:8000/app/?id=com.example.app
   ```

### إيقاف الخادم
**Stop Server**

اضغط `Ctrl+C` في نافذة Terminal
Press `Ctrl+C` in Terminal window

## 🚀 كيفية النشر / How to Deploy

### الطريقة 1: GitHub Pages

1. ارفع المشروع إلى GitHub repository
   Upload the project to a GitHub repository

2. اذهب إلى Settings > Pages
   Go to Settings > Pages

3. اختر Branch: `main` و Folder: `/root`
   Select Branch: `main` and Folder: `/root`

4. احفظ التغييرات
   Save changes

5. الموقع سيكون متاحاً على: `https://yourusername.github.io/repo-name/app/`
   The site will be available at: `https://yourusername.github.io/repo-name/app/`

### الطريقة 2: Netlify

1. ارفع الملفات إلى Netlify (Drag & Drop)
   Upload files to Netlify (Drag & Drop)

2. الموقع سيكون متاحاً فوراً
   The site will be available immediately

### الطريقة 3: استضافة ويب عادية (Apache/Nginx)

1. ارفع جميع الملفات إلى المجلد `public_html` أو `www`
   Upload all files to `public_html` or `www` folder

2. تأكد من تفعيل HTTPS
   Make sure HTTPS is enabled

3. تأكد من أن المسار `.well-known/assetlinks.json` متاح
   Make sure the path `.well-known/assetlinks.json` is accessible

## 📖 أمثلة الاستخدام / Usage Examples

### مثال 1: رابط مع package name فقط
**Input:** 
```
https://droidify.eu.org/app/?id=com.example.app
```
**Output (Deep Link):**
```
fdroid.app://com.example.app
```

### مثال 2: رابط مع package name و repo address
**Input:**
```
https://droidify.eu.org/app/?id=com.example.app&repo_address=https://myrepo.com/fdroid/repo
```
**Output (Deep Link):**
```
fdroid.app://com.example.app?repo_address=https://myrepo.com/fdroid/repo
```

### مثال 3: رابط بدون id (خطأ)
**Input:**
```
https://droidify.eu.org/app/?repo_address=https://myrepo.com/repo
```
**Output:**
```
رسالة خطأ: "خطأ: رابط غير صحيح. يجب تحديد package name."
Error message: "Error: Invalid link. Package name must be specified."
```

## 🔒 متطلبات الأمان / Security Requirements

1. **Input Validation**
   - التحقق من وجود `id` (مطلوب)
   - Validation of `id` presence (required)
   - تنظيف جميع المعاملات قبل الاستخدام
   - Sanitizing all parameters before use
   - منع XSS attacks
   - Preventing XSS attacks

2. **HTTPS Required**
   - الموقع يجب أن يعمل على HTTPS فقط
   - The site must work on HTTPS only
   - SSL certificate إلزامي لـ Android App Links
   - SSL certificate mandatory for Android App Links

3. **Error Handling**
   - معالجة جميع الأخطاء بشكل صحيح
   - Proper error handling for all cases
   - رسائل خطأ واضحة بالعربية والإنجليزية
   - Clear error messages in Arabic and English

## 🔧 الإعداد / Configuration

### إعداد Android App Links

1. افتح ملف `.well-known/assetlinks.json`
   Open `.well-known/assetlinks.json`

2. استبدل `PASTE_YOUR_SHA256_FINGERPRINT_HERE` بـ SHA256 fingerprint للتطبيق
   Replace `PASTE_YOUR_SHA256_FINGERPRINT_HERE` with the app's SHA256 fingerprint

3. يمكنك الحصول على SHA256 fingerprint باستخدام:
   You can get the SHA256 fingerprint using:

```bash
keytool -list -v -keystore your-keystore.jks -alias your-alias
```

أو من Android Studio:
Or from Android Studio:

```
Build > Generate Signed Bundle/APK > Choose keystore > View certificate
```

## 📱 متطلبات التوافق / Compatibility Requirements

- ✅ يعمل على Chrome, Firefox, Safari, Edge
   Works on Chrome, Firefox, Safari, Edge
- ✅ يعمل على Android و iOS
   Works on Android and iOS
- ✅ Responsive design
- ✅ Fast loading (< 1 second)

## 🌐 المتطلبات الفنية / Technical Requirements

- **سيرفر ويب:** Apache أو Nginx (أو أي استضافة ويب)
  Web server: Apache or Nginx (or any web hosting)
- **HTTPS:** SSL Certificate إلزامي
  HTTPS: SSL Certificate mandatory
- **JavaScript:** يجب أن يكون مفعّل
  JavaScript: Must be enabled
- **Static Hosting:** يمكن استخدام GitHub Pages، Netlify، Vercel، إلخ
  Static Hosting: Can use GitHub Pages, Netlify, Vercel, etc.

## 🐛 حل المشاكل / Troubleshooting

### المشكلة: التطبيق لا يفتح
**الحل:**
- تأكد من تثبيت تطبيق Droidify
- تأكد من تفعيل Deep Links في إعدادات Android
- جرب فتح الرابط مباشرة من المتصفح

**Problem: App doesn't open**
**Solution:**
- Make sure Droidify app is installed
- Make sure Deep Links are enabled in Android settings
- Try opening the link directly from browser

### المشكلة: رسالة خطأ عند الوصول للرابط
**الحل:**
- تأكد من وجود معامل `id` في الرابط
- تأكد من صحة package name

**Problem: Error message when accessing link**
**Solution:**
- Make sure `id` parameter exists in the link
- Verify package name is correct

## 📄 الترخيص / License

هذا المشروع متاح للاستخدام الحر.
This project is free to use.

## 👨‍💻 الدعم / Support

للإبلاغ عن مشاكل أو اقتراحات، يرجى فتح Issue في GitHub.
To report issues or suggestions, please open an Issue on GitHub.

## ✅ الميزات / Features

- ✅ واجهة مستخدم بسيطة وحديثة
  Simple and modern user interface
- ✅ دعم اللغة العربية (RTL) والإنجليزية (LTR)
  Arabic (RTL) and English (LTR) language support
- ✅ تصميم متجاوب (Responsive)
  Responsive design
- ✅ معالجة الأخطاء بشكل شامل
  Comprehensive error handling
- ✅ Fallback إلى Google Play Store
  Fallback to Google Play Store
- ✅ أمان عالي (XSS protection)
  High security (XSS protection)
- ✅ تحميل سريع (< 1 ثانية)
  Fast loading (< 1 second)

---

**Made with ❤️ for Droidify Community**

