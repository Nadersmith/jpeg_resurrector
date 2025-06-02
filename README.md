# jpeg_resurrector
Description
تقوم الأداة بـ:

البحث عن توقيع JPEG داخل الملف (FFD8FFE0 أو FFD8FFE1)

قصّ البيانات من بداية التوقيع حتى النهاية

حفظ الصورة المسترجعة بامتداد .jpg
🚀 كيفية الاستخدام:

1. احفظ الكود في ملف باسم jpeg_resurrector.py


2. اعطه صلاحيات تنفيذ:

chmod +x jpeg_resurrector.py


3. شغّله على ملفك:

python3 jpeg_resurrector.py ٢٠١٧-١١-٠٣-١١-٠٢-٥٠-١٠٤.jpg.fatp recovered.jpg


4. افتح الصورة:

xdg-open recovered.jpg
