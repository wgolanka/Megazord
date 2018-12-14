FromMegazord - server nasłuchujący na same komunikaty /dane
ToMegazord- server wydający polecenia do klienta

FromBase - client nasłuchujący na polecenia od bazy
ToBase - client wysyłający komunikaty i dane do bazy

Mission - client zapisujący dane do pliku tekstowego i
mający operacje jak np odpalenie funkcji z klasy ToBase,
która wyśle do bazy info, że misje została zakończona,
albo że omija przeszkodę, albo żeby wysłać aktualne dane
zapisane w pliku takim i takim.


Żeby odpalić:

run klasy: FromBase, startBaseToMegazord, startMission, FromMegazord