# NN-MIDI

Преобразуем одноканальные (с одним инструментом) midi в - текстовые ноты:
Пройдёмся по midi, с помощью функции 
```python
<< midi_to_note("samples/1.mid")
>> ['C5', 'C6', '-', 'A#5', '-', 'F#5', '-', 'A#5']
```
Обратная для ```midi_to_note()``` функция ```note_to_midi()```
```python
<< note_to_midi('sample.mid', ['C5', 'C6', '-', 'A#5', '-', 'F#5', '-', 'A#5'] )
>> created new file "sample.mid"
