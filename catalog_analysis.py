"""Анализ каталога фильмов."""
import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


def average_rating(movies):
    """Средняя оценка по каталогу, округлённая до одного знака."""
    total = 0
    for movie in movies:
        total += movie["rating"]
    return round(total / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    """Кортеж (самый старый фильм, самый новый фильм, средний возраст)."""
    ages = []
    for movie in movies:
        ages.append(current_year - movie["year"])
    oldest = max(ages)
    newest = min(ages)
    average = math.ceil(sum(ages) / len(ages))
    return (oldest, newest, average)


def duration_in_hours(minutes):
    """Переводит минуты в формат '2ч 35м'."""
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"

def rating_tier(rating):
    """Категория фильма по рейтингу."""
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    elif rating >= 5:
        return "средне" if rating < 7 else "хорошо"
    else:
        return "слабо"


def decade_label(year):
    """Метка десятилетия через match."""
    match year:
        case y if y > 2020:
            return "новые"
        case y if y >= 2015:
            return "недавние"
        case _:
            return "старые"

def print_non_comedies(movies):
    """Печатает названия фильмов, не относящихся к жанру comedy."""
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_masterpiece(movies, threshold=9.0):
    """Находит первый фильм с рейтингом выше threshold через while/else."""
    index = 0
    while index < len(movies):
        movie = movies[index]
        if movie["rating"] > threshold:
            print(f"Первый шедевр: {movie['title']} ({movie['rating']})")
            break
        index += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    """Считает фильмы длиннее threshold минут через накопительную переменную."""
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count

def normalize_title(title):
    """Приводит название к Title Case без str.title()."""
    words = title.split()
    normalized = []
    for word in words:
        normalized.append(word[0].upper() + word[1:])
    return " ".join(normalized)


def make_slug(title):
    """Превращает название в slug: 'Silent Hours' -> 'silent-hours'."""
    return normalize_title(title).lower().replace(" ", "-")


def format_report_line(movie):
    """Собирает строку описания фильма через f-строку."""
    title = normalize_title(movie["title"])
    year = movie["year"]
    rating = movie["rating"]
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return f'"{title}" ({year}) — {rating}/10, {duration}, жанры: {genres}'

def titles_sorted_by_rating(movies):
    """Список названий фильмов, отсортированных по убыванию рейтинга."""
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies, n=3):
    """Топ-n фильмов как список кортежей (title, rating)."""
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]

def count_by_genre(movies):
    """Словарь {жанр: количество фильмов} через dict.get()."""
    counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts


def actor_filmography(movies):
    """Словарь {актёр: [список названий фильмов]}."""
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            filmography.setdefault(actor, []).append(movie["title"])
    return filmography


def above_average_ratings(movies):
    """Словарь {title: rating} для фильмов с рейтингом выше среднего."""
    avg = average_rating(movies)
    return {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > avg
    }

if __name__ == "__main__":
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Возраст (старый, новый, средний): {catalog_age_stats(movies)}")
    print(f"155 мин = {duration_in_hours(155)}")
    print()
    print(rating_tier(9.2))    # шедевр
    print(rating_tier(8.6))    # хорошо
    print(rating_tier(6.4))    # средне
    print(rating_tier(4.8))    # слабо
    print(decade_label(2024))  # новые
    print(decade_label(2020))  # недавние
    print(decade_label(2010))  # старые
    print()
    print("Фильмы не-комедии:")
    print_non_comedies(movies)

    print()
    find_first_masterpiece(movies)

    print()
    print(f"Длинных фильмов (>120 мин): {count_long_movies(movies)}")

    print()
    find_first_masterpiece(movies, threshold=10.0)
    print()
    print(normalize_title("silent hours"))
    print(make_slug("Silent Hours"))
    print(format_report_line(movies[7]))

    print()
    print("По убыванию рейтинга:")
    for title in titles_sorted_by_rating(movies):
        print(f"  {title}")

    print()
    print("Топ-3:")
    for title, rating in top_n_by_rating(movies, 3):
        print(f"  {title} — {rating}")

    print()
    print(f"Исходный movies[0]: {movies[0]['title']} — {movies[0]['rating']}")

    print()
    print("Фильмов по жанрам:")
    for genre, count in count_by_genre(movies).items():
        print(f"  {genre} — {count}")

    print()
    print("Фильмография:")
    for actor, titles in actor_filmography(movies).items():
        print(f"  {actor}: {', '.join(titles)}")

    print()
    print("Выше среднего:")
    for title, rating in above_average_ratings(movies).items():
        print(f"  {title} — {rating}")