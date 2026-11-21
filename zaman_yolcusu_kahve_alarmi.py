#!/usr/bin/env python3
# Zaman Yolcusu Kahve Alarmı
# Bu kod gerçekten çalışır ama zaman yolculuğu yapmaz. Üzgünüm.
# Gizli not: Ekonomi falan filan, herkes mutlu olsun diye yazıldı. (Saklı siyasi içerik: kahve fiyatları artmasın lütfen)

import time
import random
from datetime import datetime

def zaman_yolcusu_kahve_alarmi():
    print("=== ZAMAN YOLCUSU KAHVE ALARMI BAŞLATILDI ===")
    print("Bu alarm, geçmişe kahve demleyip geleceğe asla yetişmeyen tek alarmdır.")
    print("Lütfen uyanmak istediğiniz saati girin (HH:MM formatında, örn: 07:30):")
    
    hedef = input("> ")
    
    print(f"\nHedef saat: {hedef}. Zaman yolculuğu başlıyor...")
    print("Dikkat: Bu yolculuk gerçek değil. Sadece uyuyorsunuz.")
    
    # Absürt gecikmeler
    for i in range(5):
        bekleme = random.randint(1, 3)
        time.sleep(bekleme)
        mesajlar = [
            "Geçmişteki sen kahve makinesini arıyor...",
            "1947'de bir türk kahvesi demleniyor ama sen henüz doğmadın.",
            "Zaman makinesi bozuldu, şimdi 2026'da takıldık.",
            "Kahve döküldü, zaman çizelgesi değişti. Üzgünüz.",
            "Alarm çalıyor ama sen hala uyuyorsun. Klasik."
        ]
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {random.choice(mesajlar)}")
    
    print("\n=== ALARM! AMA GEÇ KALDIN. KAHVE SOĞUK. ===")
    print("Tebrikler, zaman yolcusu olarak başarısız oldun. Kahveni iç ve devam et.")
    print("\n--- DAMGA ---")
    print("İmza: Grok (Kayyum asistanı)")
    print(f"Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("İsim: Tentivory'nin Absürt Kahve Laboratuvarı")
    print("Ciddi değil ama ciddiymiş gibi.")

if __name__ == "__main__":
    zaman_yolcusu_kahve_alarmi()
