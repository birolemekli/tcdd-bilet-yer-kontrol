# TCDD Bilet Kontrol

### Paket Kurulumu

`$ pip install -r requirements.txt`

- Chrome driver indirme https://chromedriver.storage.googleapis.com/index.html?path=79.0.3945.36/
- chromedriver Linux makinemde /usr/local/bin/ altındadır

Uygulama TCDD sitesine özel tasarlanmıştır.

Sizin uygulamayı çalıştırırken vereceğiniz argumentler doğrultusunda çalışmaktadır. 5dk aralıklarla verdiğiniz güzergah üzerinde ilgili saatteki seferi kontrol eder.

```sh
$ python3 main.py binişyeri inişyeri tarih saat email
$ python3 main.py Arifiye Eskişehir 10.10.2020 15:45 test@hotmail.com
```
