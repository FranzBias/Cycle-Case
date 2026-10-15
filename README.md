# cycle_case.py

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Made with ❤️ by Francesco](https://img.shields.io/badge/made%20with%20%E2%9D%A4%EF%B8%8F%20by-Francesco-red)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/platform-Linux-lightgrey?logo=linux)

[🇬🇧 English](#english) · [🇮🇹 Italiano](#italiano) · [🇩🇪 Deutsch](#deutsch) · [🇪🇸 Español](#espanol) · [🇫🇷 Français](#francais) · [🇳🇱 Nederlands](#nederlands) · [🇷🇺 Русский](#russkiy) · [🇸🇦 العربية](#arabic) · [🇨🇳 中文](#zhongwen) · [🇯🇵 日本語](#nihongo)

---

<a id="english"></a>

## 🇬🇧 English


**cycle_case.py** cycles the capitalisation of the currently selected text through three states, triggered by a keyboard shortcut:

```
UPPERCASE → lowercase → Title Case → UPPERCASE → …
```

### Dependencies

```bash
sudo apt install xdotool xclip
```

### Usage

1. Select any text in any application.
2. Press your assigned keyboard shortcut.
3. The text is replaced in place with the next capitalisation variant.

### Keyboard shortcut setup (Linux Mint / GNOME)

Go to **System Settings → Keyboard → Shortcuts → Custom Shortcuts** and add:

| Field   | Value                                      |
|---------|--------------------------------------------|
| Name    | Cycle case                                 |
| Command | `/usr/bin/python3 /path/to/cycle_case.py`  |
| Key     | e.g. `Super+Shift+U`                       |

### How it works

The script operates in three steps:

**1. Read the selection**
It reads the currently selected text from the X primary selection using `xclip -selection primary -o`. In Linux, any text you highlight is automatically placed in this buffer — separate from the clipboard.

**2. Detect state and transform**
The logic determines the current capitalisation state and applies the next one:

```python
if text == text.upper() and not text.islower():
    return text.lower()       # UPPERCASE → lowercase
elif text == text.lower():
    return text.title()       # lowercase → Title Case
else:
    return text.upper()       # anything else → UPPERCASE
```

**3. Replace in place**
The transformed text is written to the clipboard via `xclip`, then `xdotool key ctrl+v` simulates a paste — replacing the selected text directly in the active application.

#### The `sleep(0.05)` detail

A tiny pause of 50 milliseconds is added before the simulated `Ctrl+V`:

```python
time.sleep(0.05)
```

Without it, `xdotool` sometimes fires the paste before the system has finished writing the new text to the clipboard — causing the *previous* clipboard content to be pasted instead. Small delay, big difference.

### Possible extensions

- **`snake_case` and `camelCase`** — useful for developers
- **Sentence case** — only the first letter of the whole text capitalised
- **Visual notification** via `notify-send` to show which state was applied
- **Configurable cycle order** via a config file or CLI argument

> **Note:** works in virtually all GTK/Qt applications. Some terminals handle paste differently and may require adaptation.

### License

MIT

[⬆](#cycle_casepy)

---

<a id="italiano"></a>

## 🇮🇹 Italiano


**cycle_case.py** cicla la capitalizzazione del testo selezionato attraverso tre stati, attivato da una scorciatoia da tastiera:

```
TUTTO MAIUSCOLO → tutto minuscolo → Solo Le Iniziali → TUTTO MAIUSCOLO → …
```

### Dipendenze

```bash
sudo apt install xdotool xclip
```

### Utilizzo

1. Seleziona del testo in qualsiasi applicazione.
2. Premi la scorciatoia assegnata.
3. Il testo viene sostituito sul posto con la variante successiva.

### Configurazione scorciatoia (Linux Mint / GNOME)

Vai in **Impostazioni di sistema → Tastiera → Scorciatoie → Scorciatoie personalizzate** e aggiungi:

| Campo   | Valore                                           |
|---------|--------------------------------------------------|
| Nome    | Ciclo maiuscolo/minuscolo                        |
| Comando | `/usr/bin/python3 /percorso/cycle_case.py`       |
| Tasto   | es. `Super+Shift+U`                              |

### Come funziona

Lo script opera in tre passaggi:

**1. Legge la selezione**
Legge il testo selezionato dalla selezione primaria X con `xclip -selection primary -o`. In Linux, qualsiasi testo evidenziato finisce automaticamente in questo buffer — separato dagli appunti.

**2. Rileva lo stato e trasforma**
La logica determina la capitalizzazione attuale e applica quella successiva:

```python
if text == text.upper() and not text.islower():
    return text.lower()       # MAIUSCOLO → minuscolo
elif text == text.lower():
    return text.title()       # minuscolo → Solo Le Iniziali
else:
    return text.upper()       # qualsiasi altro → MAIUSCOLO
```

**3. Sostituisce in loco**
Il testo trasformato viene scritto negli appunti tramite `xclip`, poi `xdotool key ctrl+v` simula un incolla — sostituendo il testo selezionato direttamente nell'applicazione attiva.

#### Il dettaglio del `sleep(0.05)`

Una piccola pausa di 50 millisecondi viene aggiunta prima del `Ctrl+V` simulato:

```python
time.sleep(0.05)
```

Senza di essa, `xdotool` a volte scatta prima che il sistema abbia finito di scrivere il nuovo testo negli appunti — causando l'incolla del contenuto *precedente* al posto di quello trasformato. Dettaglio piccolo, differenza grande.

### Possibili estensioni

- **`snake_case` e `camelCase`** — utili per chi scrive codice
- **Sentence case** — solo la prima lettera dell'intero testo in maiuscolo
- **Notifica visiva** tramite `notify-send` per indicare quale stato è stato applicato
- **Ordine del ciclo configurabile** tramite file di configurazione o argomento CLI

> **Nota:** funziona in quasi tutte le app GTK/Qt. Alcuni terminali gestiscono il paste diversamente e potrebbero richiedere adattamenti.

### Licenza

MIT

[⬆](#cycle_casepy)

---

<a id="deutsch"></a>

## 🇩🇪 Deutsch


**cycle_case.py** wechselt die Großschreibung des markierten Textes durch drei Zustände, ausgelöst durch ein Tastaturkürzel:

```
GROSSBUCHSTABEN → kleinbuchstaben → Erster Buchstabe Groß → GROSSBUCHSTABEN → …
```

### Abhängigkeiten

```bash
sudo apt install xdotool xclip
```

### Verwendung

1. Text in einer beliebigen Anwendung auswählen.
2. Das zugewiesene Tastaturkürzel drücken.
3. Der Text wird direkt durch die nächste Variante ersetzt.

### Tastaturkürzel einrichten (Linux Mint / GNOME)

Unter **Systemeinstellungen → Tastatur → Tastenkürzel → Benutzerdefinierte Tastenkürzel**:

| Feld     | Wert                                             |
|----------|--------------------------------------------------|
| Name     | Schreibweise wechseln                            |
| Befehl   | `/usr/bin/python3 /pfad/zu/cycle_case.py`        |
| Taste    | z.B. `Super+Shift+U`                             |

### Funktionsweise

Das Skript arbeitet in drei Schritten:

**1. Auswahl lesen**
Der markierte Text wird mit `xclip -selection primary -o` aus der primären X-Auswahl gelesen. Unter Linux landet jeder markierte Text automatisch in diesem Puffer — getrennt von der Zwischenablage.

**2. Zustand erkennen und transformieren**
Die Logik erkennt die aktuelle Schreibweise und wendet die nächste an:

```python
if text == text.upper() and not text.islower():
    return text.lower()       # GROSSBUCHSTABEN → kleinbuchstaben
elif text == text.lower():
    return text.title()       # kleinbuchstaben → Erster Buchstabe Groß
else:
    return text.upper()       # alles andere → GROSSBUCHSTABEN
```

**3. Text ersetzen**
Der transformierte Text wird per `xclip` in die Zwischenablage geschrieben, dann simuliert `xdotool key ctrl+v` einen Einfügevorgang — der markierte Text wird direkt in der aktiven Anwendung ersetzt.

#### Das `sleep(0.05)`-Detail

Vor dem simulierten `Ctrl+V` wird eine kurze Pause von 50 Millisekunden eingelegt:

```python
time.sleep(0.05)
```

Ohne diese Pause löst `xdotool` den Einfügevorgang manchmal aus, bevor das System den neuen Text vollständig in die Zwischenablage geschrieben hat — und fügt dabei den *alten* Inhalt ein. Kleines Detail, großer Unterschied.

### Mögliche Erweiterungen

- **`snake_case` und `camelCase`** — nützlich für Entwickler
- **Sentence case** — nur der erste Buchstabe des gesamten Textes großgeschrieben
- **Visuelle Benachrichtigung** per `notify-send` mit dem aktuellen Zustand
- **Konfigurierbarer Zyklusablauf** per Konfigurationsdatei oder CLI-Argument

> **Hinweis:** funktioniert in nahezu allen GTK/Qt-Anwendungen. Manche Terminals behandeln das Einfügen anders und erfordern möglicherweise Anpassungen.

### Lizenz

MIT

[⬆](#cycle_casepy)

---

<a id="espanol"></a>

## 🇪🇸 Español


**cycle_case.py** alterna la capitalización del texto seleccionado entre tres estados mediante un atajo de teclado:

```
TODO EN MAYÚSCULAS → todo en minúsculas → Primera Letra En Mayúscula → TODO EN MAYÚSCULAS → …
```

### Dependencias

```bash
sudo apt install xdotool xclip
```

### Uso

1. Selecciona texto en cualquier aplicación.
2. Pulsa el atajo de teclado asignado.
3. El texto se reemplaza en su lugar con la siguiente variante.

### Configurar atajo (Linux Mint / GNOME)

Ve a **Configuración del sistema → Teclado → Atajos → Atajos personalizados**:

| Campo   | Valor                                            |
|---------|--------------------------------------------------|
| Nombre  | Ciclo mayúsculas/minúsculas                      |
| Comando | `/usr/bin/python3 /ruta/a/cycle_case.py`         |
| Tecla   | p.ej. `Super+Shift+U`                            |

### Cómo funciona

El script opera en tres pasos:

**1. Leer la selección**
Lee el texto seleccionado desde la selección primaria X con `xclip -selection primary -o`. En Linux, cualquier texto que resaltes va automáticamente a este buffer — separado del portapapeles.

**2. Detectar estado y transformar**
La lógica determina la capitalización actual y aplica la siguiente:

```python
if text == text.upper() and not text.islower():
    return text.lower()       # MAYÚSCULAS → minúsculas
elif text == text.lower():
    return text.title()       # minúsculas → Primera Letra En Mayúscula
else:
    return text.upper()       # cualquier otra → MAYÚSCULAS
```

**3. Reemplazar en el lugar**
El texto transformado se escribe al portapapeles con `xclip`, luego `xdotool key ctrl+v` simula un pegado — reemplazando el texto seleccionado directamente en la aplicación activa.

#### El detalle del `sleep(0.05)`

Se añade una pequeña pausa de 50 milisegundos antes del `Ctrl+V` simulado:

```python
time.sleep(0.05)
```

Sin ella, `xdotool` a veces dispara el pegado antes de que el sistema haya terminado de escribir el nuevo texto en el portapapeles — pegando el contenido *anterior*. Detalle pequeño, gran diferencia.

### Posibles extensiones

- **`snake_case` y `camelCase`** — útiles para desarrolladores
- **Sentence case** — solo la primera letra del texto en mayúscula
- **Notificación visual** con `notify-send` para mostrar el estado aplicado
- **Orden del ciclo configurable** mediante archivo de configuración o argumento CLI

> **Nota:** funciona en prácticamente todas las aplicaciones GTK/Qt. Algunos terminales gestionan el pegado de forma distinta y pueden requerir adaptación.

### Licencia

MIT

[⬆](#cycle_casepy)

---

<a id="francais"></a>

## 🇫🇷 Français


**cycle_case.py** fait défiler la casse du texte sélectionné à travers trois états via un raccourci clavier :

```
TOUT EN MAJUSCULES → tout en minuscules → Premières Lettres En Majuscules → TOUT EN MAJUSCULES → …
```

### Dépendances

```bash
sudo apt install xdotool xclip
```

### Utilisation

1. Sélectionnez du texte dans n'importe quelle application.
2. Appuyez sur le raccourci clavier attribué.
3. Le texte est remplacé sur place par la variante suivante.

### Configurer le raccourci (Linux Mint / GNOME)

Allez dans **Paramètres système → Clavier → Raccourcis → Raccourcis personnalisés** :

| Champ    | Valeur                                           |
|----------|--------------------------------------------------|
| Nom      | Cycle de casse                                   |
| Commande | `/usr/bin/python3 /chemin/vers/cycle_case.py`    |
| Touche   | ex. `Super+Shift+U`                              |

### Fonctionnement

Le script opère en trois étapes :

**1. Lire la sélection**
Il lit le texte sélectionné depuis la sélection primaire X avec `xclip -selection primary -o`. Sous Linux, tout texte mis en surbrillance est automatiquement placé dans ce tampon — distinct du presse-papiers.

**2. Détecter l'état et transformer**
La logique détermine la casse actuelle et applique la suivante :

```python
if text == text.upper() and not text.islower():
    return text.lower()       # MAJUSCULES → minuscules
elif text == text.lower():
    return text.title()       # minuscules → Premières Lettres En Majuscules
else:
    return text.upper()       # autre → MAJUSCULES
```

**3. Remplacer sur place**
Le texte transformé est écrit dans le presse-papiers via `xclip`, puis `xdotool key ctrl+v` simule un collage — remplaçant le texte sélectionné directement dans l'application active.

#### Le détail du `sleep(0.05)`

Une courte pause de 50 millisecondes est ajoutée avant le `Ctrl+V` simulé :

```python
time.sleep(0.05)
```

Sans elle, `xdotool` déclenche parfois le collage avant que le système n'ait fini d'écrire le nouveau texte dans le presse-papiers — collant ainsi le contenu *précédent*. Petit détail, grande différence.

### Extensions possibles

- **`snake_case` et `camelCase`** — utiles pour les développeurs
- **Sentence case** — seule la première lettre du texte en majuscule
- **Notification visuelle** via `notify-send` pour afficher l'état appliqué
- **Ordre du cycle configurable** via un fichier de configuration ou un argument CLI

> **Remarque :** fonctionne dans pratiquement toutes les applications GTK/Qt. Certains terminaux gèrent le collage différemment et peuvent nécessiter une adaptation.

### Licence

MIT

[⬆](#cycle_casepy)

---

<a id="nederlands"></a>

## 🇳🇱 Nederlands


**cycle_case.py** wisselt de hoofdlettergebruik van de geselecteerde tekst tussen drie toestanden via een sneltoets:

```
ALLES HOOFDLETTERS → alles kleine letters → Elk Woord Met Hoofdletter → ALLES HOOFDLETTERS → …
```

### Vereisten

```bash
sudo apt install xdotool xclip
```

### Gebruik

1. Selecteer tekst in een willekeurige toepassing.
2. Druk op de toegewezen sneltoets.
3. De tekst wordt ter plekke vervangen door de volgende variant.

### Sneltoets instellen (Linux Mint / GNOME)

Ga naar **Systeeminstellingen → Toetsenbord → Sneltoetsen → Aangepaste sneltoetsen**:

| Veld     | Waarde                                           |
|----------|--------------------------------------------------|
| Naam     | Hoofdletter wisselen                             |
| Opdracht | `/usr/bin/python3 /pad/naar/cycle_case.py`       |
| Toets    | bijv. `Super+Shift+U`                            |

### Hoe het werkt

Het script werkt in drie stappen:

**1. Selectie lezen**
De geselecteerde tekst wordt gelezen uit de primaire X-selectie met `xclip -selection primary -o`. In Linux wordt elke gemarkeerde tekst automatisch in deze buffer geplaatst — los van het klembord.

**2. Toestand detecteren en transformeren**
De logica bepaalt de huidige schrijfwijze en past de volgende toe:

```python
if text == text.upper() and not text.islower():
    return text.lower()       # HOOFDLETTERS → kleine letters
elif text == text.lower():
    return text.title()       # kleine letters → Elk Woord Met Hoofdletter
else:
    return text.upper()       # overige → HOOFDLETTERS
```

**3. Tekst vervangen**
De getransformeerde tekst wordt via `xclip` naar het klembord geschreven, waarna `xdotool key ctrl+v` een plakbewerking simuleert — de geselecteerde tekst wordt direct in de actieve toepassing vervangen.

#### Het `sleep(0.05)`-detail

Voor de gesimuleerde `Ctrl+V` wordt een korte pauze van 50 milliseconden toegevoegd:

```python
time.sleep(0.05)
```

Zonder deze pauze vuurt `xdotool` het plakken soms af voordat het systeem klaar is met het schrijven van de nieuwe tekst naar het klembord — waardoor de *vorige* inhoud wordt geplakt. Klein detail, groot verschil.

### Mogelijke uitbreidingen

- **`snake_case` en `camelCase`** — handig voor ontwikkelaars
- **Sentence case** — alleen de eerste letter van de volledige tekst als hoofdletter
- **Visuele melding** via `notify-send` om de toegepaste toestand te tonen
- **Configureerbare cyclusvolgorde** via een configuratiebestand of CLI-argument

> **Opmerking:** werkt in vrijwel alle GTK/Qt-toepassingen. Sommige terminals verwerken plakken anders en vereisen mogelijk aanpassing.

### Licentie

MIT

[⬆](#cycle_casepy)

---

<a id="russkiy"></a>

## 🇷🇺 Русский


**cycle_case.py** циклически изменяет регистр выделенного текста между тремя состояниями с помощью сочетания клавиш:

```
ВСЁ ЗАГЛАВНЫМИ → всё строчными → Каждое Слово С Заглавной → ВСЁ ЗАГЛАВНЫМИ → …
```

### Зависимости

```bash
sudo apt install xdotool xclip
```

### Использование

1. Выделите текст в любом приложении.
2. Нажмите назначенное сочетание клавиш.
3. Текст заменяется на следующий вариант прямо на месте.

### Назначение сочетания клавиш (Linux Mint / GNOME)

Перейдите в **Параметры системы → Клавиатура → Сочетания клавиш → Пользовательские сочетания**:

| Поле     | Значение                                         |
|----------|--------------------------------------------------|
| Имя      | Сменить регистр                                  |
| Команда  | `/usr/bin/python3 /путь/к/cycle_case.py`         |
| Клавиша  | напр. `Super+Shift+U`                            |

### Принцип работы

Скрипт работает в три этапа:

**1. Чтение выделения**
Выделенный текст считывается из первичного буфера X с помощью `xclip -selection primary -o`. В Linux любой выделенный текст автоматически помещается в этот буфер — отдельно от буфера обмена.

**2. Определение состояния и преобразование**
Логика определяет текущий регистр и применяет следующий:

```python
if text == text.upper() and not text.islower():
    return text.lower()       # ВСЁ ЗАГЛАВНЫМИ → всё строчными
elif text == text.lower():
    return text.title()       # всё строчными → Каждое Слово С Заглавной
else:
    return text.upper()       # всё остальное → ВСЁ ЗАГЛАВНЫМИ
```

**3. Замена на месте**
Преобразованный текст записывается в буфер обмена через `xclip`, затем `xdotool key ctrl+v` симулирует вставку — заменяя выделенный текст прямо в активном приложении.

#### Деталь `sleep(0.05)`

Перед симулированным `Ctrl+V` добавляется небольшая пауза в 50 миллисекунд:

```python
time.sleep(0.05)
```

Без неё `xdotool` иногда выполняет вставку до того, как система успевает записать новый текст в буфер обмена — и вставляется *предыдущее* содержимое. Маленькая деталь, большая разница.

### Возможные расширения

- **`snake_case` и `camelCase`** — полезно для разработчиков
- **Sentence case** — заглавная только первая буква всего текста
- **Визуальное уведомление** через `notify-send` с указанием применённого состояния
- **Настраиваемый порядок цикла** через файл конфигурации или аргумент CLI

> **Примечание:** работает практически во всех GTK/Qt-приложениях. Некоторые терминалы обрабатывают вставку иначе и могут потребовать адаптации.

### Лицензия

MIT

[⬆](#cycle_casepy)

---

<a id="arabic"></a>

## 🇸🇦 العربية

<div dir="rtl">


**cycle_case.py** يُدوِّر تنسيق حالة الأحرف في النص المحدد عبر ثلاث حالات باستخدام اختصار لوحة المفاتيح:

```
كل الأحرف كبيرة → كل الأحرف صغيرة → أول حرف كبير من كل كلمة → كل الأحرف كبيرة → …
```

### المتطلبات

```bash
sudo apt install xdotool xclip
```

### الاستخدام

1. حدِّد نصًا في أي تطبيق.
2. اضغط على الاختصار المعيَّن.
3. يُستبدل النص في مكانه بالنوع التالي.

### إعداد الاختصار (Linux Mint / GNOME)

اذهب إلى **إعدادات النظام ← لوحة المفاتيح ← الاختصارات ← اختصارات مخصصة**:

| الحقل   | القيمة                                           |
|---------|--------------------------------------------------|
| الاسم   | تدوير حالة الأحرف                               |
| الأمر   | `/usr/bin/python3 /المسار/إلى/cycle_case.py`    |
| المفتاح | مثلاً `Super+Shift+U`                           |

### كيف يعمل

يعمل السكريبت في ثلاث خطوات:

**1. قراءة التحديد**
يقرأ النص المحدد من التحديد الأساسي لـ X باستخدام `xclip -selection primary -o`. في Linux، يُودَع أي نص تُحدِّده تلقائيًا في هذا المخزن المؤقت — بشكل منفصل عن الحافظة.

**2. تحديد الحالة والتحويل**
تحدد الشيفرة الحالة الراهنة وتُطبِّق التالية:

```python
if text == text.upper() and not text.islower():
    return text.lower()       # كبيرة → صغيرة
elif text == text.lower():
    return text.title()       # صغيرة → أول حرف كبير
else:
    return text.upper()       # أي حالة أخرى → كبيرة
```

**3. الاستبدال في المكان**
يُكتب النص المحوَّل إلى الحافظة عبر `xclip`، ثم يُحاكي `xdotool key ctrl+v` عملية اللصق — ليحلَّ محل النص المحدد مباشرةً في التطبيق النشط.

#### تفصيل `sleep(0.05)`

تُضاف توقف قصير مدته 50 ميلي ثانية قبل `Ctrl+V` المحاكَى:

```python
time.sleep(0.05)
```

بدونه، قد يُطلق `xdotool` اللصق قبل أن ينتهي النظام من كتابة النص الجديد إلى الحافظة — فيُلصق المحتوى *السابق* بدلاً منه. تفصيل صغير، فارق كبير.

### توسعات مقترحة

- **`snake_case` و`camelCase`** — مفيد للمطورين
- **Sentence case** — حرف كبير للحرف الأول من النص فقط
- **إشعار مرئي** عبر `notify-send` لإظهار الحالة المُطبَّقة
- **ترتيب دورة قابل للتخصيص** عبر ملف إعداد أو وسيطة CLI

> **ملاحظة:** يعمل في جميع تطبيقات GTK/Qt تقريبًا. قد تتعامل بعض الطرفيات مع اللصق بشكل مختلف وتحتاج إلى تكييف.

### الترخيص

MIT

</div>

[⬆](#cycle_casepy)

---

<a id="zhongwen"></a>

## 🇨🇳 中文


**cycle_case.py** 通过键盘快捷键在三种大小写状态之间循环切换所选文本：

```
全部大写 → 全部小写 → 首字母大写 → 全部大写 → …
```

### 依赖项

```bash
sudo apt install xdotool xclip
```

### 使用方法

1. 在任意应用程序中选中文本。
2. 按下分配的键盘快捷键。
3. 文本将被下一种大小写形式就地替换。

### 配置快捷键（Linux Mint / GNOME）

前往 **系统设置 → 键盘 → 快捷键 → 自定义快捷键**：

| 字段 | 值                                               |
|------|--------------------------------------------------|
| 名称 | 大小写循环                                       |
| 命令 | `/usr/bin/python3 /路径/到/cycle_case.py`        |
| 按键 | 例如 `Super+Shift+U`                             |

### 工作原理

脚本分三步运行：

**1. 读取选中内容**
使用 `xclip -selection primary -o` 从 X 主选区读取选中文本。在 Linux 中，任何高亮文本都会自动进入此缓冲区——与剪贴板相互独立。

**2. 检测状态并转换**
逻辑判断当前大小写状态并应用下一种：

```python
if text == text.upper() and not text.islower():
    return text.lower()       # 全部大写 → 全部小写
elif text == text.lower():
    return text.title()       # 全部小写 → 首字母大写
else:
    return text.upper()       # 其他 → 全部大写
```

**3. 就地替换**
转换后的文本通过 `xclip` 写入剪贴板，然后 `xdotool key ctrl+v` 模拟粘贴操作——直接在当前活动应用中替换选中文本。

#### `sleep(0.05)` 的细节

在模拟的 `Ctrl+V` 之前添加了 50 毫秒的短暂停顿：

```python
time.sleep(0.05)
```

没有它，`xdotool` 有时会在系统将新文本写入剪贴板之前触发粘贴——导致粘贴的是*之前*的内容。小细节，大差别。

### 可能的扩展

- **`snake_case` 和 `camelCase`**——对开发者很有用
- **Sentence case**——仅将整段文本的首字母大写
- **视觉通知**——通过 `notify-send` 显示已应用的状态
- **可配置的循环顺序**——通过配置文件或 CLI 参数

> **注意：** 适用于几乎所有 GTK/Qt 应用程序。部分终端对粘贴的处理方式不同，可能需要调整。

### 许可证

MIT

[⬆](#cycle_casepy)

---

<a id="nihongo"></a>

## 🇯🇵 日本語


**cycle_case.py** はキーボードショートカットで選択テキストの大文字・小文字を3つの状態で順番に切り替えます：

```
全て大文字 → 全て小文字 → 各単語の頭文字を大文字 → 全て大文字 → …
```

### 依存関係

```bash
sudo apt install xdotool xclip
```

### 使い方

1. 任意のアプリケーションでテキストを選択する。
2. 割り当てたキーボードショートカットを押す。
3. テキストがその場で次のバリアントに置き換えられる。

### ショートカットの設定（Linux Mint / GNOME）

**システム設定 → キーボード → ショートカット → カスタムショートカット** に移動：

| フィールド | 値                                               |
|------------|--------------------------------------------------|
| 名前       | 大文字小文字の切り替え                           |
| コマンド   | `/usr/bin/python3 /パス/cycle_case.py`           |
| キー       | 例：`Super+Shift+U`                              |

### 仕組み

スクリプトは3つのステップで動作します：

**1. 選択内容を読み取る**
`xclip -selection primary -o` を使って X プライマリセレクションから選択テキストを読み取ります。Linux では、ハイライトしたテキストは自動的にこのバッファに入ります——クリップボードとは別のものです。

**2. 状態を検出して変換する**
現在の大文字小文字の状態を判定し、次の状態を適用します：

```python
if text == text.upper() and not text.islower():
    return text.lower()       # 全て大文字 → 全て小文字
elif text == text.lower():
    return text.title()       # 全て小文字 → 各単語の頭文字を大文字
else:
    return text.upper()       # それ以外 → 全て大文字
```

**3. その場で置き換える**
変換されたテキストは `xclip` でクリップボードに書き込まれ、その後 `xdotool key ctrl+v` がペーストを模擬します——アクティブなアプリケーション内で選択テキストが直接置き換えられます。

#### `sleep(0.05)` の詳細

模擬された `Ctrl+V` の前に50ミリ秒の短い待機時間が追加されます：

```python
time.sleep(0.05)
```

これがないと、システムがクリップボードへの書き込みを完了する前に `xdotool` がペーストを実行してしまい、*以前の*内容が貼り付けられることがあります。小さな詳細ですが、大きな違いです。

### 拡張の可能性

- **`snake_case` と `camelCase`** ——開発者に便利
- **Sentence case** ——テキスト全体の最初の文字だけを大文字にする
- **視覚的通知** ——`notify-send` で適用された状態を表示
- **設定可能なサイクル順序** ——設定ファイルまたは CLI 引数で指定

> **注意：** ほぼすべての GTK/Qt アプリケーションで動作します。一部のターミナルはペーストの処理が異なるため、調整が必要な場合があります。

### ライセンス

MIT

[⬆](#cycle_casepy)

---
