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
```
Затем необходимо преобразовать список нот в матрицу с помощью функции ```convert_to_matrix(notes_array, luft)```
```luft``` необходим для того, чтобы ограничить количество октав (длину векторов, которые будет возвращать функция)

```python
<< convert_to_matrix(['C5', 'C6', '-', 'A#5', '-', 'F#5', '-', 'A#5'], 4)
>>
>> [0, 0, 0, 0, 0, 0, 0, 0, 0, 72, 0, 216, 255, 0, 108, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 72, 0, 216]
>> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 102, 0, 255, 0]
>> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 68, 0, 0, 255, 0, 102, 0, 0, 0]
>> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 102, 0, 255, 0]
```

Создадим несколько .mid файлов, с которыми будет сравниваться основной, преобразуем их матрицы и запишем в .txt

-/text_presets<br>
---/0.txt<br>
---/1.txt<br>
---/2.txt<br>
---/3.txt<br>
---/4.txt<br>

Запустим модуль neural_network
```python
>> {'classes': 0, 'probabilities': array([0.5215701, 0.4784299])}
>> {'classes': 0, 'probabilities': array([0.5240148, 0.4759852])}
>> {'classes': 0, 'probabilities': array([0.52296138, 0.47703862])}
>> {'classes': 0, 'probabilities': array([0.52408582, 0.47591418])}
>> {'classes': 0, 'probabilities': array([0.52055538, 0.47944462])}
>> {'classes': 0, 'probabilities': array([0.5215701, 0.4784299])}
>> {'classes': 0, 'probabilities': array([0.5173605, 0.4826395])}
```
Эти списки показывают, насколько основной файл, разбитый по чанкам соответсвует другим семплам


<h1>Введение</h1>
<p>
	<b>Нейронная сеть -</b> 
	Иску́сственная нейро́нная се́ть — математическая модель, а также её программное или аппаратное воплощение, построенная по принципу организации и функционирования биологических нейронных сетей — сетей нервных клеток живого организма.

</p>
<p>
	Для классификации изображений часто используются свёрточные нейронные сети, нацеленные на эффективное распознование образов.
</p>

<h3>Свёрточная нейроная сеть</h3>
<p>
	<br>
	 — специальная архитектура искусственных нейронных сетей, предложенная Яном Лекуном в 1988 году
	 <br>
	  Использует некоторые особенности зрительной коры, в которой были открыты так называемые простые клетки, реагирующие на прямые линии под разными углами, и сложные клетки, реакция которых связана с активацией определённого набора простых клеток. Таким образом, идея свёрточных нейронных сетей заключается в чередовании свёрточных слоёв	
</p>

<h3>Интерпретация свёрточной нейронной сети</h3>
<p>
	Работа свёрточной нейронной сети обычно интерпретируется как переход от конкретных особенностей изображения к более абстрактным деталям, и далее к ещё более абстрактным деталям вплоть до выделения понятий высокого уровня. При этом сеть самонастраивается и вырабатывает сама необходимую иерархию абстрактных признаков (последовательности карт признаков), фильтруя маловажные детали и выделяя существенное.
	<br>
	Подобная интерпретация носит скорее метафорический или иллюстративный характер. Фактически «признаки», вырабатываемые сложной сетью, малопонятны и трудны для интерпретации настолько, что в практических системах не особенно рекомендуется пытаться понять содержания этих признаков или пытаться их «подправить», вместо этого рекомендуется усовершенствовать саму структуру и архитектуру сети, чтобы получить лучшие результаты. Так, игнорирование системой каких-то существенных явлений может говорить о том, что либо не хватает данных для обучения, либо структура сети обладает недостатками и система не может выработать эффективных признаков для данных явлений.
</p>


<p>
	Существует несколько библиотек машинного обучения, а также библиотек для работы с большими данными и их визуализацией
	<ul>
		<li>Scikit-learn</li>
		<li>Theano</li>
		<li>Pandas</li>
		<li>Seaborn</li>
		<li>Torch</li>
	</ul>
	Однако, мною была выбрана библиотека Tensorflow, поскольку ...
</p>

<h3>Библиотека машинного обучения tensorflow</h3>
<p>
	TensorFlow — открытая программная библиотека для машинного обучения, разработанная компанией Google для решения задач построения и тренировки нейронной сети с целью автоматического нахождения и классификации образов, достигая качества человеческого восприятия.
</p>

<b>Свёрточная нейронная сеть представляет собой последовательность из слоёв
	Слои могут быть:
	<ul>
		<li>Свёрточным</li>
		<li>Слоями макспулинга</li>
		<li>Полносвязными</li>
	</ul>
</b>


<h3>Свёрточные слои</h3>
<p>....</p>
<h3>Макспулинг</h3>
<p>....</p>
<h3>Полносвязные слои</h3>
<p>....</p>
