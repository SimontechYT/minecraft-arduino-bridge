# minecraft-arduino-bridge
Questo progetto collega un Arduino con il PC tramite seriale, e un semplice script Python che ascolta il click destro del mouse.  
Quando viene rilevato un click destro, lo script manda un segnale ad Arduino che accende un LED per mezzo secondo.

## Hardware necessario

- Arduino Uno (o compatibile)
- LED collegato al pin 13 (integrato sulla maggior parte delle board Arduino)

## Software necessario

- Python 3
- Librerie Python: `pyserial` e `pynput`
'''bash
pip install pyserial
'''bash
pip install pynput
