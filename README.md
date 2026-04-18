# 🦠 COVID-19 Hasta Tahmini - Makine Öğrenmesi Projesi

##  Proje Açıklaması
Bu proje, COVID-19 semptom verilerini kullanarak bir kişinin hasta olup olmadığını tahmin eden bir makine öğrenmesi modelidir.

Amaç, farklı algoritmaların performansını karşılaştırarak en iyi modeli bulmaktır.

---

##  Kullanılan Veri Seti
Veri seti Kaggle üzerinden alınmıştır.

📎 Veri seti linki:
https://www.kaggle.com/datasets

Veri seti şu özellikleri içerir:
- Breathing Problem
- Fever
- Dry Cough
- Sore Throat
- Headache
- COVID-19 sonucu (Yes / No)

---

##  Veri Ön İşleme
- Yes / No değerleri 1 / 0’a dönüştürüldü
- Eksik veriler kontrol edildi
- Bağımsız değişkenler (X) ve hedef değişken (y) ayrıldı
- Train-test split işlemi yapıldı (%80 eğitim, %20 test)

---

##  Kullanılan Makine Öğrenmesi Algoritmaları

### 1. Logistic Regression
Lineer sınıflandırma algoritmasıdır. Olasılık hesaplayarak sınıf tahmini yapar.

### 2. Random Forest
Birden fazla decision tree kullanarak daha doğru tahminler yapar.

### 3. (Opsiyonel) KNN
En yakın komşulara göre sınıflandırma yapar.

---

##  Model Performansı

| Model | Accuracy |
|------|----------|
| Logistic Regression | ~0.xx |
| Random Forest | ~0.xx |

 Random Forest genellikle daha yüksek doğruluk verir.

---

## Sonuç
Model, semptomlara bakarak COVID-19 tahmini yapabilmektedir.
Random Forest modeli genellikle daha başarılı sonuçlar vermiştir.

---

## ▶️ Projeyi Çalıştırma



### 📦 Gerekli Kütüphaneler
Projeyi çalıştırmak için aşağıdaki kütüphaneler gereklidir:
pip install pandas numpy matplotlib seaborn scikit-learn