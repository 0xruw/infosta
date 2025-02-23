# infosta

<h1> Instagram Details Fetcher Tool </h1>
<p>
This tool allows users to fetch detailed information from Instagram profiles, either for a single user or multiple users. The program supports fetching essential data like the full name, number of followers, posts, bio, profile picture URL, and even the account creation year (based on the user ID).

The application interacts with the Instagram API via Instaloader, and it can send the gathered details directly to your Telegram bot for further use. Additionally, it provides a clean and user-friendly interface with color-coded outputs, ensuring smooth operation and a clear view of the results.

Key Features:

Fetch detailed Instagram profile data (username, full name, followers, etc.)
High-quality profile picture URL retrieval
Account creation year detection based on user ID
Send gathered details directly to Telegram
Multiple options for searching (single user or bulk list of users from a file)
Clean, color-coded interface using colorama
</p>

<h1 style="color: red;">لازم تكون مثبت بايثون و pip</h1>
<h1 style="color: red;">You must have Python and pip installed</h1>

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<h1>أداة جلب تفاصيل حسابات الانستا</h1>

<p>

هذه الأداة تتيح للمستخدمين جلب معلومات تفصيلية من حسابات انستا، سواء لحساب واحد أو لعدة حسابات. يدعم البرنامج جلب بيانات أساسية مثل الاسم الكامل، عدد المتابعين، المنشورات، السيرة الذاتية، رابط صورة الملف الشخصي، وحتى سنة إنشاء الحساب (استنادًا إلى معرّف المستخدم).

يتفاعل التطبيق مع واجهة Instaloader الخاصة بـ إنستاجرام، ويمكنه إرسال التفاصيل التي تم جمعها مباشرة إلى بوت التليجرام الخاص بك لاستخدامها لاحقًا. كما يوفر واجهة مستخدم نظيفة وسهلة مع إخراج ملون لضمان التشغيل السلس والنتائج الواضحة.

الميزات الرئيسية:
جلب تفاصيل حساب إنستاجرام (اسم المستخدم، الاسم الكامل، المتابعين، إلخ)
جلب رابط صورة الملف الشخصي عالية الجودة
تحديد سنة إنشاء الحساب بناءً على معرّف المستخدم
إرسال التفاصيل التي تم جمعها مباشرة إلى التليجرام
خيارات متعددة للبحث (حساب واحد أو قائمة حسابات من ملف)
واجهة ملونة ونظيفة باستخدام colorama
</p>


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Installation windows

1. Install the required dependencies:
   ```bash
   pip install requests instaloader colorama
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/0xruw/infosta.git
   ```

3. **Set up Telegram and Instagram information:**
   - Create a `settings.txt` file in the root directory of the project.
   - Add the following information to the `settings.txt` file:

     ```
     Bot_token=your_telegram_bot_token
     User_id=your_telegram_user_id
     Your_instagram_(fake)=your_instagram_username
     Password=your_instagram_password
     ```

   Replace `your_telegram_bot_token`, `your_telegram_user_id`, `your_instagram_username`, and `your_instagram_password` with your own credentials.

  4. **RUN 0xruwinfosta.exe **


## التثبيت على ويندوز

1. تثبيت الحزم المطلوبة:
   ```bash
   pip install requests instaloader colorama
   ```

2. استنساخ المستودع:
   ```bash
   git clone https://github.com/0xruw/infosta.git
   ```

3. **إعداد معلومات تلغرام وإنستجرام:**
   - أنشئ ملف `settings.txt` في الدليل الرئيسي للمشروع.
   - أضف المعلومات التالية إلى ملف `settings.txt`:

     ```
     Bot_token=التوكن
     User_id=الايدي
     Your_instagram_(fake)= اسم المستخدم
     Password=كلمة المرور
     ```
       4. **شغل البرنامج  0xruwinfosta.exe **


----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Installation on iSH

1. Install the required packages:
   ```bash
   pip install requests instaloader colorama
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/0xruw/infosta.git
   ```
   ```bash
   cd infosta
   ```

3. **Set up Telegram and Instagram information:**
   - Edit the `settings.txt` file and add your information as shown below.
   - We recommend using the **Koder** app to edit the file.

     ```
     Bot_token=your_token
     User_id=your_user_id
     Your_instagram_(fake)=your_username
     Password=your_password
     ```

   - Replace `your_token`, `your_user_id`, `your_username`, and `your_password` with your own information. (Using a fake account is recommended to avoid getting banned)

4. Run the script:
   ```bash
   python3 0xruwinfosta.py
   ```

---

## تثبيت المشروع / Installation

### التثبيت على iSH / Installation on iSH

1. تثبيت الحزم المطلوبة / Install the required packages:
   ```bash
   pip install requests instaloader colorama
   ```

2. استنساخ المستودع / Clone the repository:
   ```bash
   git clone https://github.com/0xruw/infosta.git
   ```
   ```bash
   cd infosta
   ```

3. **إعداد معلومات تلغرام وإنستجرام / Set up Telegram and Instagram information:**
   - عدّل الملف `settings.txt` وضع فيه معلوماتك كما هو موضح أدناه
   - يفضل استخدام تطبيق **Koder** لتعديل الملفات.

     ```
     Bot_token=التوكن
     User_id=الايدي
     Your_instagram_(fake)=اسم المستخدم
     Password=كلمة المرور
     ```

   - استبدل `التوكن` و `الايدي` و `اسم المستخدم` و `كلمة المرور` بمعلوماتك الخاصة. (يُفضل استخدام حساب وهمي لتجنب حظر الحساب)

4. تشغيل السكربت / Run the script:
   ```bash
   python3 0xruwinfosta.py
   ```
```
