---
marp: true
theme: default
paginate: true
backgroundColor: #F0F2F5
style: |
  :root {
    --color-yellow: #FFC928;
    --color-black: #000000;
    --color-white: #FFFFFF;
    --color-bg: #F0F2F5;
  }
  section {
    font-family: 'Inter', -apple-system, sans-serif;
    color: #333;
    padding: 40px 60px;
  }
  section::after {
    font-size: 0.6em;
    color: #999;
  }
  h1 {
    color: var(--color-black);
    font-size: 1.8em;
    border-bottom: 4px solid var(--color-yellow);
    padding-bottom: 0.3em;
  }
  h2 {
    color: var(--color-black);
    font-size: 1.4em;
  }
  h3 {
    color: #555;
    font-size: 1.1em;
  }
  strong {
    color: var(--color-black);
  }
  a {
    color: var(--color-black);
    text-decoration: underline;
    text-decoration-color: var(--color-yellow);
  }
  table {
    font-size: 0.72em;
    width: 100%;
  }
  th {
    background: var(--color-black);
    color: var(--color-yellow);
    font-weight: 700;
  }
  td {
    background: var(--color-white);
  }
  code {
    background: #FFF3D0;
    color: var(--color-black);
    font-size: 0.85em;
  }
  blockquote {
    border-left: 4px solid var(--color-yellow);
    background: #FFF8E1;
    padding: 0.5em 1em;
    font-size: 0.9em;
  }
  ul, ol {
    font-size: 0.9em;
  }
  section.title {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    background: var(--color-black);
    color: var(--color-white);
  }
  section.title h1 {
    color: var(--color-yellow);
    border-bottom: none;
    font-size: 2.2em;
  }
  section.title p {
    color: #ccc;
  }
  section.yellow {
    background: var(--color-yellow);
    color: var(--color-black);
  }
  section.yellow h1 {
    border-bottom-color: var(--color-black);
  }
  .tag {
    display: inline-block;
    background: var(--color-yellow);
    color: var(--color-black);
    padding: 2px 10px;
    border-radius: 12px;
    font-size: 0.75em;
    font-weight: 700;
  }
  .kpi {
    display: inline-block;
    background: var(--color-black);
    color: var(--color-yellow);
    padding: 4px 14px;
    border-radius: 8px;
    font-size: 0.85em;
    font-weight: 700;
    margin: 2px;
  }
---

<!-- _class: title -->

# IPR ПРОФ
## Трансформация продукта

<div style="margin-top:30px">
<svg width="160" height="40" viewBox="0 0 160 40" fill="none">
  <rect x="0" y="0" width="40" height="40" rx="4" fill="#FFC928"/>
  <path d="M10 30L20 10L30 30" stroke="#000" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="52" y="24" font-family="Inter,sans-serif" font-size="16" font-weight="700" fill="#FFC928">IPR MEDIA</text>
</svg>
</div>

Виталий Смирнов — Product Manager
Апрель 2026

---

# Предисловие: экосистема IPR Media

<div style="position:absolute;top:35px;right:55px;opacity:0.10">
<svg width="110" height="110" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="3">
  <circle cx="35" cy="50" r="24"/><circle cx="65" cy="50" r="24"/>
  <circle cx="35" cy="50" r="8" fill="#FFC928" stroke="none"/>
  <circle cx="65" cy="50" r="8" fill="#FFC928" stroke="none"/>
  <line x1="43" y1="50" x2="57" y2="50" stroke-width="4"/>
</svg>
</div>

**IPR SMART** (ВУЗы) и **PROFобразование** (СПО) — два продукта одной экосистемы.

| Возможность | SMART | PROF | Потенциал |
|---|---|---|---|
| SMART-курсы | ✅ | ❌ | **Высокий** |
| Образовательные модули | ✅ | ❌ | **Высокий** |
| Интеграция LMS/Moodle | ✅ | Ограничена | **Критический** |
| Лаборатории СПО | ❌ | ✅ | Развивать |

> **Стратегия:** перенести проверенные механики из SMART, сохранив уникальную специализацию PROF.

---

<!-- _class: yellow -->

# 1. Трансформация продукта
### За счёт чего продукт станет ежедневным инструментом

<div style="text-align:center;margin-top:40px">
<svg width="150" height="150" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="3" stroke-linecap="round">
  <path d="M70 18a32 32 0 0 1 10 32"/>
  <polygon points="78,47 84,35 72,38" fill="#000" stroke="none"/>
  <path d="M30 82a32 32 0 0 1-10-32"/>
  <polygon points="22,53 16,65 28,62" fill="#000" stroke="none"/>
  <rect x="38" y="38" width="24" height="24" rx="4" stroke-width="2.5"/>
  <path d="M45 50h10M50 45v10" stroke-width="2.5"/>
</svg>
</div>

---

# Блок 1. Ключевые барьеры

<div style="position:absolute;top:35px;right:55px;opacity:0.10">
<svg width="90" height="90" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round">
  <path d="M50 10L90 85H10Z"/>
  <line x1="50" y1="40" x2="50" y2="60"/>
  <circle cx="50" cy="70" r="2" fill="#000"/>
</svg>
</div>

| Барьер | Суть |
|---|---|
| **ЭБС оторвана от учебного процесса** | Нет инструмента интеграции контента в занятия |
| **Нет триггера возвращения** | Нет уведомлений, задач, дедлайнов — ~50% dormant |
| **UX не соответствует ожиданиям** | Студенты привыкли к VK/YouTube |
| **Ценность скрыта** | 165 000+ единиц контента не проявлены |

---

# Блок 1. Три продуктовых сценария

<div style="position:absolute;top:30px;right:50px;opacity:0.10">
<svg width="110" height="80" viewBox="0 0 120 80" fill="none" stroke="#000" stroke-width="3">
  <circle cx="25" cy="25" r="12"/><path d="M13 78c0-15 10-25 24-25"/>
  <circle cx="60" cy="20" r="14"/><path d="M46 78c0-18 12-28 28-28"/>
  <circle cx="95" cy="25" r="12"/><path d="M83 78c0-15 10-25 24-25"/>
</svg>
</div>

**1. Рабочий стол преподавателя** — персональный дашборд
`Мои дисциплины → Задания студентам → Статистика → Новинки`
Потенциал: **200-600 книговыдач/семестр с одного преподавателя**

**2. Учебный трек студента** — персонализация по специальности
`Мой учебный план → Задания → Рекомендации → Прогресс`
Переход Dormant → Occasional = **+50% книговыдач**

**3. Методический конструктор** — сборка РПД и списков
`Специальность → Дисциплина → Автоподбор изданий → Готовый блок для РПД`

---

# Блок 1. KPI

<div style="position:absolute;top:35px;right:55px;opacity:0.10">
<svg width="90" height="90" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
  <polyline points="10,80 35,55 55,65 90,20"/>
  <polygon points="80,18 92,18 92,30" fill="#000" stroke="none"/>
  <line x1="10" y1="85" x2="95" y2="85" stroke-width="2"/>
  <line x1="10" y1="15" x2="10" y2="85" stroke-width="2"/>
</svg>
</div>

| Метрика | Сейчас | 3 мес. | 6 мес. |
|---|---|---|---|
| Activation Rate | ~30% | 50% | 65% |
| WAU/MAU | ~15% | 25% | 35% |
| Книговыдач / польз. / мес. | ~1.5 | 3 | 5 |
| % преподавателей с подборками | ~5% | 15% | 30% |
| D7 Retention | ~20% | 30% | 40% |

---

<!-- _class: yellow -->

# 2. УМК как точка сборки
### Не отдельный продукт, а «живая оболочка» вокруг контента

<div style="text-align:center;margin-top:40px">
<svg width="150" height="150" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M50 80V30"/>
  <path d="M50 30c-8-8-25-12-35-8v48c10-4 27 0 35 8"/>
  <path d="M50 30c8-8 25-12 35-8v48c-10-4-27 0-35 8"/>
  <line x1="28" y1="40" x2="42" y2="36" stroke-width="2"/>
  <line x1="28" y1="50" x2="42" y2="46" stroke-width="2"/>
  <line x1="58" y1="36" x2="72" y2="40" stroke-width="2"/>
  <line x1="58" y1="46" x2="72" y2="50" stroke-width="2"/>
</svg>
</div>

---

# Блок 2. УМК на платформе

<div style="position:absolute;top:35px;right:55px;opacity:0.10">
<svg width="90" height="90" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="3" stroke-linecap="round">
  <circle cx="50" cy="18" r="8"/>
  <line x1="50" y1="26" x2="50" y2="42"/>
  <line x1="50" y1="42" x2="25" y2="58"/><line x1="50" y1="42" x2="75" y2="58"/>
  <circle cx="25" cy="62" r="6"/><circle cx="75" cy="62" r="6"/>
  <line x1="25" y1="68" x2="25" y2="78"/><line x1="75" y1="68" x2="75" y2="78"/>
  <line x1="25" y1="78" x2="12" y2="88"/><line x1="25" y1="78" x2="38" y2="88"/>
  <line x1="75" y1="78" x2="62" y2="88"/><line x1="75" y1="78" x2="88" y2="88"/>
  <circle cx="12" cy="91" r="4"/><circle cx="38" cy="91" r="4"/>
  <circle cx="62" cy="91" r="4"/><circle cx="88" cy="91" r="4"/>
</svg>
</div>

```
ФГОС СПО → ОПОП → Дисциплина → УМК:
  ├── Основная литература (автоподбор по ФГОС)
  ├── Дополнительная литература
  ├── Практические задания (кейсы, тесты)
  ├── Методические указания
  ├── ФОС
  └── Индустриальные кейсы (от партнёров)
```

### Принцип: «Начни с малого — получи большое»

1. **1 мин** — выбрать специальность и дисциплину → автоподборка
2. **5 мин** — скорректировать, добавить своё
3. *Опционально* — добавить тесты, методические указания
4. **Результат:** список литературы → полноценный УМК

---

<!-- _class: yellow -->

# 3. Практикоориентированность
### Перевод продукта в практическую плоскость

<div style="text-align:center;margin-top:40px">
<svg width="150" height="150" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="38" cy="40" r="18" stroke-width="2.5"/>
  <circle cx="38" cy="40" r="7"/>
  <rect x="34" y="34" width="8" height="3" rx="1" transform="rotate(-30 38 40)"/>
  <rect x="34" y="34" width="8" height="3" rx="1" transform="rotate(30 38 40)"/>
  <rect x="34" y="34" width="8" height="3" rx="1" transform="rotate(90 38 40)"/>
  <circle cx="68" cy="62" r="14" stroke-width="2.5"/>
  <circle cx="68" cy="62" r="5"/>
  <rect x="65" y="57" width="6" height="2.5" rx="1" transform="rotate(-45 68 62)"/>
  <rect x="65" y="57" width="6" height="2.5" rx="1" transform="rotate(45 68 62)"/>
  <rect x="65" y="57" width="6" height="2.5" rx="1" transform="rotate(135 68 62)"/>
</svg>
</div>

---

# Блок 3. Решения

<div style="position:absolute;top:35px;right:55px;opacity:0.10">
<svg width="90" height="90" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M50 52c-12 0-22-4-22-10V30c0-6 10-10 22-10s22 4 22 10v12c0 6-10 10-22 10z"/>
  <ellipse cx="50" cy="30" rx="22" ry="10"/>
  <path d="M28 50c0 6 10 10 22 10s22-4 22-10"/>
  <path d="M28 42v18" /><path d="M72 42v18"/>
  <path d="M28 68c0 6 10 10 22 10s22-4 22-10"/>
  <path d="M28 60v18" /><path d="M72 60v18"/>
</svg>
</div>

**1. Банк кейсов от индустриальных партнёров**
Отрасль + задание + материалы из каталога (книговыдачи!) + экспертный разбор
Связка с **Профессионалитетом** и **DataLIB.Проекты**

**2. Практические задания с проверкой**
Тесты по главам, ситуационные задания, ответы с цитатами из изданий
Каждое задание **требует обращения к контенту** → органический рост

**3. Цифровые стажировки**
«День бухгалтера», «Приёмка на стройке» — модульные мини-курсы
Привязка к 200+ специальностям из каталога PROF

---

<!-- _class: yellow -->

# 4. Монетизация
### Как продукт зарабатывает через активацию использования

<div style="text-align:center;margin-top:40px">
<svg width="150" height="150" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="3" stroke-linecap="round">
  <ellipse cx="50" cy="75" rx="25" ry="8"/>
  <path d="M25 75V65c0-5 11-8 25-8s25 3 25 8v10"/>
  <ellipse cx="50" cy="65" rx="25" ry="8"/>
  <path d="M25 65V55c0-5 11-8 25-8s25 3 25 8v10"/>
  <ellipse cx="50" cy="55" rx="25" ry="8"/>
  <path d="M25 55V45c0-5 11-8 25-8s25 3 25 8v10"/>
  <ellipse cx="50" cy="45" rx="25" ry="8"/>
  <path d="M78 28l8-14" stroke-width="2.5"/><path d="M86 14l-6 3M86 14l-1 6" stroke-width="2.5"/>
</svg>
</div>

---

# Блок 4. Цепочка ценности

<div style="position:absolute;top:30px;right:50px;opacity:0.10">
<svg width="100" height="100" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="2.5">
  <path d="M15 20h70l-12 15h-46z" fill="#FFC928" stroke="#000"/>
  <path d="M21 35h58l-10 15h-38z" fill="#FFC928" stroke="#000" opacity="0.8"/>
  <path d="M27 50h46l-8 15h-30z" fill="#FFC928" stroke="#000" opacity="0.6"/>
  <path d="M33 65h34l-6 15h-22z" fill="#FFC928" stroke="#000" opacity="0.4"/>
  <path d="M39 80h22l-4 10h-14z" fill="#FFC928" stroke="#000" opacity="0.3"/>
</svg>
</div>

**Сейчас:** подписка от министерства → минимальное использование → продление «по инерции»

> Базовая подписка → Преподаватель создаёт подборки → Книговыдачи растут → Апселл: +Кейсы +УМК +API → **Продление + расширение**

**Пакеты:**
**Базовая** — контент + подборки · **+ Профессионалитет** — кейсы + стажировки + аналитика · **+ Метод. поддержка** — УМК + отчёты + IPR Education

---

# Блок 4. KPI монетизации

<div style="position:absolute;top:35px;right:55px;opacity:0.10">
<svg width="90" height="90" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="3" stroke-linecap="round">
  <rect x="10" y="60" width="16" height="28" rx="2" fill="#FFC928" stroke="#000"/>
  <rect x="32" y="45" width="16" height="43" rx="2" fill="#FFC928" stroke="#000"/>
  <rect x="54" y="30" width="16" height="58" rx="2" fill="#FFC928" stroke="#000"/>
  <rect x="76" y="15" width="16" height="73" rx="2" fill="#FFC928" stroke="#000"/>
  <line x1="5" y1="90" x2="97" y2="90" stroke-width="2"/>
</svg>
</div>

| Метрика | 3 мес. | 6 мес. |
|---|---|---|
| Рост ARPU | +5% | +15% |
| Конверсия в апселл | 5% | 12% клиентов |
| Retention Rate | +3 п.п. | +8 п.п. |
| Клиентов на «Профессионалитет» | 10 | 40 |

---

<!-- _class: yellow -->

# 5. AI в продукте
### Где ИИ усилит использование

<div style="text-align:center;margin-top:40px">
<svg width="150" height="150" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="2.5" stroke-linecap="round">
  <path d="M50 18c-16 0-28 12-28 26 0 9 5 17 13 22v8c0 2 2 4 4 4h22c2 0 4-2 4-4v-8c8-5 13-13 13-22 0-14-12-26-28-26z"/>
  <line x1="40" y1="78" x2="60" y2="78" stroke-width="2"/>
  <line x1="42" y1="83" x2="58" y2="83" stroke-width="2"/>
  <path d="M38 40c3-4 8-6 12-6s9 2 12 6" stroke-width="2"/>
  <circle cx="40" cy="48" r="3" fill="#000"/>
  <circle cx="60" cy="48" r="3" fill="#000"/>
  <path d="M42 58c4 3 12 3 16 0" stroke-width="2"/>
  <line x1="50" y1="8" x2="50" y2="14" stroke-width="2"/>
  <line x1="22" y1="20" x2="26" y2="24" stroke-width="2"/>
  <line x1="78" y1="20" x2="74" y2="24" stroke-width="2"/>
  <line x1="14" y1="44" x2="20" y2="44" stroke-width="2"/>
  <line x1="80" y1="44" x2="86" y2="44" stroke-width="2"/>
</svg>
</div>

---

# Блок 5. Три AI-сценария

<div style="position:absolute;top:30px;right:50px;opacity:0.10">
<svg width="100" height="100" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="2.5">
  <rect x="20" y="20" width="60" height="60" rx="8"/>
  <rect x="30" y="30" width="15" height="15" rx="2"/><rect x="55" y="30" width="15" height="15" rx="2"/>
  <rect x="30" y="55" width="15" height="15" rx="2"/><rect x="55" y="55" width="15" height="15" rx="2"/>
  <line x1="45" y1="37" x2="55" y2="37" stroke-width="2"/>
  <line x1="37" y1="45" x2="37" y2="55" stroke-width="2"/>
  <line x1="63" y1="45" x2="63" y2="55" stroke-width="2"/>
  <line x1="45" y1="63" x2="55" y2="63" stroke-width="2"/>
  <circle cx="50" cy="10" r="5"/><line x1="50" y1="15" x2="50" y2="20"/>
  <circle cx="50" cy="90" r="5"/><line x1="50" y1="80" x2="50" y2="85"/>
  <circle cx="10" cy="50" r="5"/><line x1="15" y1="50" x2="20" y2="50"/>
  <circle cx="90" cy="50" r="5"/><line x1="80" y1="50" x2="85" y2="50"/>
</svg>
</div>

| | Как сейчас | С AI | Эффект |
|---|---|---|---|
| **Подбор литературы** | 2-4 часа вручную | 5 минут, AI анализирует 9 400+ учебников | 100-300 книговыдач на список |
| **Навигация по контенту** | Листает 300 стр. → уходит в Google | Вопрос → релевантные фрагменты → ссылки | Каждый вопрос = книговыдача |
| **Генерация тестов** | 1-2 дня на 20-50 вопросов | 30 минут, привязка к страницам | Рост глубины чтения |

<br>

| KPI | 3 мес. | 6 мес. |
|---|---|---|
| Преподаватели с AI-подбором | 10% | 25% |
| Конверсия AI → книговыдача | 40% | 60% |
| AI-сгенерированных тестов | 200 | 1 000 |

---

<!-- _class: yellow -->

# 6. Работа с рынком
### Почему покупают, но не используют активно

<div style="text-align:center;margin-top:40px">
<svg width="150" height="150" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="2.5" stroke-linecap="round">
  <circle cx="50" cy="28" r="10"/>
  <path d="M35 75c0-15 7-22 15-22h0c8 0 15 7 15 22"/>
  <circle cx="22" cy="35" r="8"/>
  <path d="M10 72c0-12 5-18 12-18s12 6 12 18"/>
  <circle cx="78" cy="35" r="8"/>
  <path d="M66 72c0-12 5-18 12-18s12 6 12 18"/>
  <line x1="5" y1="80" x2="95" y2="80" stroke-width="2"/>
</svg>
</div>

---

# Блок 6. Реальная обратная связь

<div style="position:absolute;top:30px;right:50px;opacity:0.10">
<svg width="100" height="100" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="2.5">
  <rect x="28" y="10" width="44" height="80" rx="8"/>
  <rect x="34" y="24" width="32" height="50" rx="2" fill="#FFC928" opacity="0.3"/>
  <circle cx="50" cy="82" r="4"/>
  <polygon points="35,38 38,30 41,38" fill="#FFC928" stroke="#000" stroke-width="1.5"/>
  <polygon points="43,38 46,30 49,38" fill="#FFC928" stroke="#000" stroke-width="1.5"/>
  <polygon points="51,38 54,30 57,38" fill="#FFC928" stroke="#000" stroke-width="1.5"/>
  <polygon points="59,38 62,30 65,38" fill="#000" stroke="#000" stroke-width="1.5" opacity="0.15"/>
</svg>
</div>

### IPR SMART (Google Play, 3.9★, 933 отзыва)
- «При попытке листать — выделяется текст» — навигация сломана
- Горизонтальный режим «зеркалит», мелкий шрифт
- PDF не позволяет менять размер шрифта
- Оффлайн пытается подключиться к интернету

### Конкуренты

| ЭБС | Рейтинг | Главная проблема |
|---|---|---|
| **Лань** (лидер) | **1.9★** RuStore | «Постоянно вылетает, невозможно читать» |
| **IPR SMART** | **3.9★** Google Play | UX ридера, но стабильное |
| **Юрайт** | — | Фокус на ВУЗах, не СПО |

> **IPR стабильнее конкурента в 2 раза** — это не используется в маркетинге!

---

# Блок 6. Гипотезы (на основе данных)

<div style="position:absolute;top:35px;right:55px;opacity:0.10">
<svg width="90" height="90" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="3" stroke-linecap="round">
  <path d="M35 70V55c-5-3-8-8-8-15a18 18 0 0 1 36 0c0 7-3 12-8 15v15"/>
  <path d="M35 75h20M35 82h20"/>
  <line x1="45" y1="87" x2="45" y2="95" stroke-width="2"/>
  <circle cx="45" cy="40" r="5" fill="#FFC928" stroke="none"/>
  <path d="M60 25l10-8M62 40h12M60 55l10 8" stroke-width="2"/>
</svg>
</div>

| # | Гипотеза | Источник | Проверка |
|---|---|---|---|
| H1 | «Нет проводника» — никто не обучает пользователей | Отзывы только от руководства | CustDev неактивных |
| H2 | «Нет интеграции в процесс» — ЭБС отдельно от работы | Нет отзывов о рабочих сценариях | Карта инструментов |
| H3 | «Ридер — барьер для студентов» | Google Play, жалобы на навигацию | A/B тест нового ридера |
| H4 | «Аудио и текст живут отдельно» | 1 100+ аудио без синхронизации | Пилот на 10 изданиях |
| H5 | «Стабильность не в маркетинге» | 3.9★ vs 1.9★ | Сравнение в sales-материалах |

---

# Блок 6. NPS-подход

<div style="position:absolute;top:35px;right:55px;opacity:0.10">
<svg width="90" height="90" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="3" stroke-linecap="round">
  <path d="M15 75a42 42 0 0 1 70 0" fill="none"/>
  <path d="M15 75a42 42 0 0 1 70 0" fill="none" stroke="#FFC928" stroke-width="5" stroke-dasharray="66 132"/>
  <line x1="50" y1="73" x2="62" y2="42" stroke-width="3"/>
  <circle cx="50" cy="75" r="5" fill="#000"/>
  <text x="12" y="90" font-size="10" font-family="Inter,sans-serif" fill="#000">0</text>
  <text x="85" y="90" font-size="10" font-family="Inter,sans-serif" fill="#000">10</text>
</svg>
</div>

**Текущий NPS неизвестен.** Предложение:

1. **Измерение:** in-app NPS-опрос после 5+ книговыдач
2. **Сегментация:** преподаватели / студенты / библиотекари
3. **Proxy:** Google Play 3.9★ ≈ NPS +10..+20

### Рычаги роста NPS

| Инициатива | Потенциал |
|---|---|
| Исправление мобильного ридера (H3) | +10-15 pts (мобильные) |
| Синхронизация позиции чтения | +5-8 pts |
| AI-саммаризация | Рост activation |
| Полноценный оффлайн | Устранение фрустрации |

---

<!-- _class: yellow -->

# 7. Модель развития
### Roadmap на 3 года

<div style="text-align:center;margin-top:40px">
<svg width="150" height="150" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M15 80c10-5 15-20 25-25s15 10 25 5 15-30 25-40" stroke-width="4"/>
  <circle cx="15" cy="80" r="5" fill="#000"/>
  <circle cx="40" cy="55" r="5" fill="#000"/>
  <circle cx="65" cy="60" r="5" fill="#000"/>
  <circle cx="90" cy="20" r="5" fill="#000"/>
  <path d="M85 18l5 2 2-6" stroke-width="2.5"/>
  <text x="8" y="95" font-size="9" font-family="Inter,sans-serif" fill="#000" font-weight="700">2026</text>
  <text x="55" y="78" font-size="9" font-family="Inter,sans-serif" fill="#000" font-weight="700">2027</text>
  <text x="80" y="15" font-size="9" font-family="Inter,sans-serif" fill="#000" font-weight="700">2028</text>
</svg>
</div>

---

# Блок 7. 2026 — Quick Wins

<div style="position:absolute;top:30px;right:50px;opacity:0.10">
<svg width="100" height="100" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="3" stroke-linecap="round">
  <path d="M30 75l20-50 10 20 15-30" stroke-width="4"/>
  <polygon points="73,11 80,15 76,22" fill="#000" stroke="none"/>
  <rect x="15" y="78" width="70" height="4" rx="2" fill="#FFC928" stroke="none"/>
</svg>
</div>

**Цель:** библиотека для галочки → инструмент каждую неделю

| Квартал | Инициатива | Эффект |
|---|---|---|
| Q2 | Рабочий стол преподавателя + конструктор | Рост книговыдач |
| Q3 | Учебный трек студента + персонализация | Activation rate ↑ |
| Q3 | CustDev: 50+ интервью | Валидация roadmap |
| Q4 | AI-подбор литературы (MVP) | Снижение барьера |
| Q4 | 50 кейсов от индустриальных партнёров | Практика-контент |

<span class="kpi">WAU/MAU 15% → 30%</span> <span class="kpi">Книговыдач 1.5 → 4/мес.</span>

---

# Блок 7. 2027 — Масштабирование

<div style="position:absolute;top:30px;right:50px;opacity:0.10">
<svg width="100" height="100" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M50 85V40"/>
  <path d="M50 40l-15 18h10v27"/>
  <path d="M50 40l15 18h-10v27"/>
  <path d="M50 40V15l-10 14h7"/>
  <path d="M50 15l10 14h-7"/>
  <circle cx="35" cy="30" r="3" fill="#FFC928" stroke="none"/>
  <circle cx="65" cy="30" r="3" fill="#FFC928" stroke="none"/>
  <circle cx="50" cy="8" r="4" fill="#FFC928" stroke="#000" stroke-width="2"/>
</svg>
</div>

**Цель:** платформа, без которой колледж не может работать

| Направление | Что делаем | Эффект |
|---|---|---|
| УМК | Полноценный конструктор | Системная привязка |
| Практика | 500+ кейсов, стажировки ТОП-20 | PROF = не только книги |
| AI | Суммаризация, тесты, ассистент | Частота ×2-3 |
| Интеграции | API для LMS, SSO | Бесшовное встраивание |
| Монетизация | Модульная модель | ARPU +20-30% |

<span class="kpi">Retention 90%+</span> <span class="kpi">ARPU +25%</span>

---

# Блок 7. 2028 — Целевая модель

<div style="position:absolute;top:30px;right:50px;opacity:0.10">
<svg width="100" height="100" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
  <polygon points="50,8 62,38 95,38 68,58 78,90 50,70 22,90 32,58 5,38 38,38" stroke-width="2.5"/>
  <polygon points="50,25 56,42 75,42 60,52 65,70 50,60 35,70 40,52 25,42 44,42" fill="#FFC928" stroke="none"/>
</svg>
</div>

**Цель:** IPR ПРОФ = стандарт цифровой методической среды СПО

| Стейкхолдер | Роль IPR ПРОФ |
|---|---|
| **Преподаватель** | Единое рабочее место: литература + УМК + задания + AI |
| **Студент** | Персональная среда от поступления до выпуска |
| **Колледж** | Платформа управления качеством образования |
| **Регион** | Аналитическая панель по колледжам |
| **Индустрия** | Кейсы, стажировки, оценка выпускников |

<br>

<span class="kpi">Каждый 3-й колледж страны (сейчас каждый 7-й)</span>

---

# Блок 7. Приоритизация Impact / Effort

<div style="position:absolute;top:35px;right:55px;opacity:0.10">
<svg width="90" height="90" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="2.5">
  <line x1="50" y1="10" x2="50" y2="90"/>
  <line x1="10" y1="50" x2="90" y2="50"/>
  <rect x="15" y="15" width="30" height="30" rx="4" fill="#FFC928" opacity="0.4" stroke="none"/>
  <rect x="55" y="15" width="30" height="30" rx="4" fill="#E3F2FD" opacity="0.5" stroke="none"/>
  <rect x="15" y="55" width="30" height="30" rx="4" fill="#F3E5F5" opacity="0.5" stroke="none"/>
  <rect x="55" y="55" width="30" height="30" rx="4" fill="#EEE" opacity="0.5" stroke="none"/>
  <text x="22" y="34" font-size="8" font-family="Inter,sans-serif" fill="#000" font-weight="700">QW</text>
  <text x="64" y="34" font-size="7" font-family="Inter,sans-serif" fill="#000" font-weight="700">Стр.</text>
</svg>
</div>

| | Низкие усилия | Высокие усилия |
|---|---|---|
| **Высокий Impact** | ⭐ **Quick Wins:** Рабочий стол преподавателя, Учебный трек, Оффлайн, CustDev 50+ | 🎯 **Стратегические:** Конструктор УМК, AI-суммаризация, API для LMS, Модульная модель |
| **Низкий Impact** | ✅ **Заполняем:** Ночной режим, Словарь, Мультиформатность | ⏳ **Отложить:** Аналитика регионов, Цифровые стажировки, Аудио-синхронизация |

---

<!-- _class: yellow -->

# 8. Редизайн и миграция
### Полный редизайн + смена стека при 388 000 активных пользователей

<div style="text-align:center;margin-top:40px">
<svg width="150" height="150" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
  <rect x="18" y="40" width="55" height="40" rx="4"/>
  <rect x="22" y="44" width="47" height="32" rx="2" fill="#FFC928" opacity="0.2" stroke="none"/>
  <rect x="30" y="28" width="55" height="40" rx="4" fill="#F0F2F5"/>
  <rect x="34" y="32" width="47" height="32" rx="2" fill="#FFC928" opacity="0.3" stroke="none"/>
  <rect x="42" y="16" width="55" height="40" rx="4" fill="#fff"/>
  <rect x="46" y="20" width="47" height="32" rx="2" fill="#FFC928" opacity="0.4" stroke="none"/>
  <line x1="52" y1="30" x2="82" y2="30" stroke-width="2"/>
  <line x1="52" y1="36" x2="75" y2="36" stroke-width="2"/>
  <line x1="52" y1="42" x2="70" y2="42" stroke-width="2"/>
</svg>
</div>

---

# Блок 8. Последовательность

<div style="position:absolute;top:30px;right:50px;opacity:0.10">
<svg width="100" height="100" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="3" stroke-linecap="round">
  <rect x="10" y="70" width="22" height="20" rx="3" fill="#FFC928" opacity="0.5"/>
  <rect x="28" y="50" width="22" height="40" rx="3" fill="#FFC928" opacity="0.5"/>
  <rect x="48" y="30" width="22" height="60" rx="3" fill="#FFC928" opacity="0.5"/>
  <rect x="68" y="10" width="22" height="80" rx="3" fill="#FFC928" opacity="0.5"/>
</svg>
</div>

### Фаза 0: Подготовка (1-2 мес.)
Аудит стека + UX → формирование команды → определение MVP scope

### Фаза 1: Дизайн-система (2-3 мес.)
Адаптация DS → прототипирование → юзабилити-тесты (5-7 препод. + 10 студентов)

### Фаза 2: Разработка (4-6 мес.)
**Strangler Fig Pattern:** новые фичи на новом стеке, старый продукт работает
Feature parity → миграция данных → тестирование на staging

### Фаза 3: Бета-тест + переключение (2-3 мес.)
5-10 колледжей → toggle «Попробовать» → полное переключение

---

# Блок 8. Риски и метрики

<div style="position:absolute;top:35px;right:55px;opacity:0.10">
<svg width="90" height="90" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
  <path d="M50 10L85 85H15Z"/>
  <path d="M50 15L80 80H20Z" fill="#FFC928" opacity="0.2" stroke="none"/>
  <path d="M50 38v20" stroke-width="4"/>
  <circle cx="50" cy="68" r="3" fill="#000"/>
</svg>
</div>

| Риск | Вероятность | Митигация |
|---|---|---|
| Просадка метрик | Высокая | Мягкое переключение, возврат |
| Scope creep | Высокая | Жёсткий MVP, milestone каждые 2 нед. |
| Потеря данных | Низкая | Многоэтапное тестирование, rollback |
| Несовместимость API | Средняя | Раннее тестирование, backward compat |

### Критерии успеха
- Загрузка < 2 сек, Conversion Rate +15%
- NPS новой > NPS старой через 1 мес.
- Книговыдачи не ниже текущего уровня **в любой момент**

---

<!-- _class: yellow -->

# 9. Визия: через 3 года

<div style="text-align:center;margin-top:40px">
<svg width="150" height="150" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="50" cy="50" r="18"/>
  <circle cx="50" cy="50" r="10" fill="#FFC928" opacity="0.3"/>
  <circle cx="50" cy="50" r="4" fill="#000"/>
  <line x1="68" y1="50" x2="82" y2="50" stroke-width="4"/>
  <line x1="82" y1="40" x2="82" y2="60" stroke-width="3"/>
  <line x1="86" y1="44" x2="86" y2="56" stroke-width="3"/>
  <line x1="18" y1="50" x2="32" y2="50" stroke-width="4"/>
  <line x1="18" y1="40" x2="18" y2="60" stroke-width="3"/>
  <line x1="14" y1="44" x2="14" y2="56" stroke-width="3"/>
</svg>
</div>

---

# Блок 9. IPR ПРОФ через 3 года

<div style="position:absolute;top:30px;right:50px;opacity:0.10">
<svg width="100" height="100" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="2.5" stroke-linecap="round">
  <path d="M15 85h70" stroke-width="2"/>
  <path d="M20 85V55l15-15 15 10 15-20 15 5V85"/>
  <circle cx="20" cy="55" r="3" fill="#FFC928"/><circle cx="35" cy="40" r="3" fill="#FFC928"/>
  <circle cx="50" cy="50" r="3" fill="#FFC928"/><circle cx="65" cy="30" r="3" fill="#FFC928"/>
  <circle cx="80" cy="35" r="3" fill="#FFC928"/>
  <path d="M82 28l-2 7 7-1" stroke-width="2"/>
</svg>
</div>

Цифровая методическая среда, в которой:

- **Преподаватель** проводит значительную часть рабочего дня: учебные программы, назначения, практические задания, AI-помощник, аналитика
- **Студент** — персональное пространство от первого курса до выпуска: учебники, практика, портфолио
- **Колледж** не представляет организацию учебного процесса без PROF — как без электронного журнала

### Ключевой сдвиг

Решение о продлении подписки принимается не «для галочки», а потому что **40%+ преподавателей** ведут дисциплины в PROF, студенты ежедневно открывают платформу, руководство получает прозрачную аналитику.

<span class="kpi">IPR ПРОФ = стандартная инфраструктура СПО</span>

---

<!-- _class: yellow -->

# 10. Самооценка

<div style="text-align:center;margin-top:40px">
<svg width="150" height="150" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="3">
  <circle cx="50" cy="50" r="38"/>
  <circle cx="50" cy="50" r="26" stroke-dasharray="4 3"/>
  <circle cx="50" cy="50" r="14"/>
  <circle cx="50" cy="50" r="5" fill="#FFC928" stroke="#000" stroke-width="2"/>
  <line x1="50" y1="8" x2="50" y2="16" stroke-width="2"/>
  <line x1="50" y1="84" x2="50" y2="92" stroke-width="2"/>
  <line x1="8" y1="50" x2="16" y2="50" stroke-width="2"/>
  <line x1="84" y1="50" x2="92" y2="50" stroke-width="2"/>
</svg>
</div>

---

# Блок 10. Оценка компетенций

<div style="position:absolute;top:25px;right:45px;opacity:0.10">
<svg width="110" height="110" viewBox="0 0 100 100" fill="none" stroke="#000" stroke-width="2">
  <polygon points="50,12 65,35 90,35 72,52 78,78 50,64 22,78 28,52 10,35 35,35" stroke-dasharray="3 2"/>
  <polygon points="50,22 60,38 80,38 66,50 70,68 50,58 30,68 34,50 20,38 40,38" fill="#FFC928" opacity="0.3" stroke="#000" stroke-width="1.5"/>
</svg>
</div>

| Блок | Оценка | Комментарий |
|---|---|---|
| 1. Трансформация | **8** | Трансформация LMS → платформа развития |
| 2. УМК | **7** | Понимаю ФГОС→ОПОП→РПД, нет опыта СПО |
| 3. Практика | **8** | Конструктор курсов с практикой в LMS |
| 4. Монетизация | **8** | B2B SaaS: retention, upsell, unit-экономика |
| 5. AI | **9** | Внедрял AI в LMS, сократили время на 50% |
| 6. Рынок | **8** | CustDev 5-12/квартал, участие в продажах |
| 7. Roadmap | **7** | Квартальные есть, 3 года — шире |
| 8. Редизайн | **9** | Tech Lead + PM, миграция LMS |
| 9. Визия | **8** | Целевое состояние → тактические шаги |

<span class="kpi">Средняя: 8.0 / 10</span>
**Сильные:** tech, EdTech, AI, data-driven | **Зона роста:** нормативка СПО, B2G, регионы

---

<!-- _class: title -->

# Спасибо

<div style="margin-top:10px">
<svg width="180" height="40" viewBox="0 0 180 40" fill="none">
  <rect x="0" y="0" width="40" height="40" rx="4" fill="#FFC928"/>
  <path d="M10 30L20 10L30 30" stroke="#000" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="52" y="24" font-family="Inter,sans-serif" font-size="16" font-weight="700" fill="#FFC928">IPR MEDIA</text>
</svg>
</div>

**Виталий Смирнов**
Product Manager — IPR ПРОФ
Апрель 2026

ТГ @smalvik
