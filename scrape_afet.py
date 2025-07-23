import twint
import pandas as pd

# Twint config
c = twint.Config()
c.Search = "yardım OR enkaz OR çadır"
c.Since = "2023-02-06"
c.Until = "2023-02-10"
c.Lang = "tr"
c.Limit = 100
c.Store_csv = True
c.Output = "yardim_tweetleri.csv"

# 🚨 KISA VE GÜVENİLİR BİR USER-AGENT EKLE
c.User_full = True
c.User_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"

twint.run.Search(c)
print("✅ Tweetler başarıyla çekildi.")
