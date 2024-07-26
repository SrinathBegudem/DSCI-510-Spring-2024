# Lab 12
# Replace "WRITE CODE HERE" with your python code and remove the "pass" statement
# Do not invoke the functions outside main block
import sqlite3
import pandas as pd


# ----------------- Question 1 -----------------


class MusicFestival:
    def __init__(self, database="music_festival.db"):
        self.database = database

    def create_tables(self) -> None:
        """
        Create tables as per assignment document
        """
        conn = sqlite3.connect(self.database)

        cursor = conn.cursor()
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS artists (
            artist_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            genre TEXT NOT NULL
        )"""
        )

        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS stages (
            stage_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            location TEXT NOT NULL
        )"""
        )

        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS performances (
            performance_id INTEGER PRIMARY KEY,
            artist_id INTEGER,
            stage_id INTEGER,
            start_time DATETIME NOT NULL,
            end_time DATETIME NOT NULL,
            FOREIGN KEY (artist_id) REFERENCES artists(artist_id),
            FOREIGN KEY (stage_id) REFERENCES stages(stage_id)
        )"""
        )

        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS tickets (
            ticket_id INTEGER PRIMARY KEY,
            purchaser_name TEXT NOT NULL,
            purchase_date DATE NOT NULL,
            price REAL NOT NULL
        )"""
        )

        conn.commit()
        conn.close()

    def insert_data(self) -> None:
        """
        Insert data as per assignment document
        """
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        artists_data = [
            ("The Cosmic Keys", "Rock"),
            ("Jazz Jaguars", "Jazz"),
            ("Electro Ensemble", "Electronic"),
            ("Folklore Friends", "Folk"),
            ("Reggae Revolution", "Reggae"),
            ("Classical Quintet", "Classical"),
            ("Blues Brothers", "Blues"),
            ("Pop Parade", "Pop"),
            ("Metal Mavericks", "Metal"),
            ("Country Cousins", "Country"),
        ]

        cursor.executemany(
            "INSERT INTO artists (name, genre) VALUES (?, ?)", artists_data
        )

        # Insert data into 'stages'
        stages_data = [
            ("Main Stage", "Central Field"),
            ("Jazz Corner", "North Wing"),
            ("Electronic Dome", "East Field"),
            ("Folk Forest", "West Woods"),
            ("Classical Hall", "South Side"),
            ("Blues Bar", "Near Entrance"),
            ("Pop Platform", "Central Field"),
            ("Metal Mountain", "North Hill"),
            ("Country Corner", "West Woods"),
            ("Reggae Room", "East Field"),
        ]

        cursor.executemany(
            "INSERT INTO stages (name, location) VALUES (?, ?)", stages_data
        )

        # Assuming artist_id and stage_id are sequentially assigned starting from 1
        # and performances are on '2023-07-04' with varying times
        performances_data = [
            (1, 1, "2023-07-04 12:00", "2023-07-04 14:00"),
            (2, 2, "2023-07-04 12:30", "2023-07-04 14:30"),
            (3, 3, "2023-07-04 15:00", "2023-07-04 17:00"),
            (4, 4, "2023-07-04 15:30", "2023-07-04 17:30"),
            (5, 10, "2023-07-04 16:00", "2023-07-04 18:00"),
            (6, 5, "2023-07-04 18:00", "2023-07-04 20:00"),
            (7, 6, "2023-07-04 18:30", "2023-07-04 20:30"),
            (8, 7, "2023-07-04 21:00", "2023-07-04 23:00"),
            (9, 8, "2023-07-04 21:30", "2023-07-04 23:30"),
            (10, 9, "2023-07-04 19:00", "2023-07-04 21:00"),
        ]

        cursor.executemany(
            "INSERT INTO performances (artist_id, stage_id, start_time, end_time) VALUES (?, ?, ?, ?)",
            performances_data,
        )

        # Insert sample data into 'tickets' - Dates range from '2023-06-01' to '2023-06-10'
        tickets_data = [
            ("Alex Smith", "2023-06-01", 59.99),
            ("Jamie Doe", "2023-06-02", 79.99),
            ("Sam Rivera", "2023-06-03", 49.99),
            ("Chris Green", "2023-06-04", 89.99),
            ("Pat Jordan", "2023-06-05", 99.99),
            ("Morgan Casey", "2023-06-06", 39.99),
            ("Taylor Swift", "2023-06-07", 109.99),
            ("Jordan Lee", "2023-06-08", 69.99),
            ("Casey Smith", "2023-06-09", 59.99),
            ("Riley Brown", "2023-06-10", 79.99),
        ]

        cursor.executemany(
            "INSERT INTO tickets (purchaser_name, purchase_date, price) VALUES (?, ?, ?)",
            tickets_data,
        )

        conn.commit()
        conn.close()

    def query_1_get_artists_with_rock_genre(self) -> list[str]:
        """
        Find all artists performing in the 'Rock' genre.

        Return:
            list[str]: [artist-1, artist-2 . . .]
        """
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM artists WHERE genre = 'Rock'")
        artists = [name[0] for name in cursor.fetchall()]
        conn.close()
        return artists

    def query_2_total_revenue_from_sales(self) -> float:
        """
        Calculate the total revenue generated from ticket sales

        Return:
            float: round to 2 decimal places
        """
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(price) FROM tickets")
        total_revenue = cursor.fetchone()[0]
        conn.close()
        return round(total_revenue, 2)


    def query_3_number_performances(self) -> list[tuple]:
        """
        Number of performances for each stage

        Return:
            list[tuple]: [('performance-1', 1), ('performance-2', 1) . . .]
        """
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT s.name, COUNT(p.performance_id)
            FROM stages s
            LEFT JOIN performances p ON s.stage_id = p.stage_id
            GROUP BY s.stage_id
        """)
        performances = cursor.fetchall()
        conn.close()
        return performances

    def query_4_performances_on_specific_date(self) -> list[tuple]:
        """
        Find all performances on '2023-07-04' with the artist name, stage name, and start time.
    
        Return:
            list[tuple]: [('artist-1', 'stage-1', 'start time-1'),
                          ('artist-2', 'stage-2', 'start time-2'),
                           ...]
        """
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT a.name, s.name, p.start_time
            FROM performances p
            JOIN artists a ON p.artist_id = a.artist_id
            JOIN stages s ON p.stage_id = s.stage_id
            WHERE DATE(p.start_time) = '2023-07-04'
            ORDER BY p.start_time ASC, a.name ASC
        """)
        performances = cursor.fetchall()
        conn.close()
        return performances    

    
    def query_5_longer_performances(self) -> list[str]:
        """
        Artists with performances longer than 2 Hours

        Return:
            list[str]: ["artist-1", "artist-2" . . .]
        """
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT a.name
            FROM performances p
            JOIN artists a ON p.artist_id = a.artist_id
            WHERE (julianday(p.end_time) - julianday(p.start_time)) * 24 > 2
        """)
        artists = [name[0] for name in cursor.fetchall()]
        conn.close()
        return artists


# ----------------- Question 2 -----------------
class Titanic:
    def preprocess_data(self, filename="data/titanic.csv") -> pd.DataFrame:
        df = pd.read_csv(filename)
        # Impute missing 'Age' values with the mode of the 'Age' column
        age_mode = df['Age'].mode()[0]
        df['Age'].fillna(age_mode, inplace=True)
        return df

    @staticmethod
    def get_survived_count(data: pd.DataFrame) -> int:
        return data['Survived'].sum()

    @staticmethod
    def get_average_fare(data: pd.DataFrame) -> float:
        return data['Fare'].mean()

    @staticmethod
    def get_max_age(data: pd.DataFrame) -> float:
        return data['Age'].max()

    @staticmethod
    def get_min_age(data: pd.DataFrame) -> float:
        return data['Age'].min()

    @staticmethod
    def get_male_count(data: pd.DataFrame) -> int:
        return data[data['Sex'] == 'male'].shape[0]

    @staticmethod
    def get_died_under_30_count(data: pd.DataFrame) -> int:
        return data[(data['Age'] < 30) & (data['Survived'] == 0)].shape[0]

    @staticmethod
    def get_passenger_ids(data: pd.DataFrame) -> list:
        return data[data['Fare'] == 0]['PassengerId'].sort_values().tolist()

    @staticmethod
    def get_survivors_classwise(data: pd.DataFrame) -> dict:
        survivors = data[data['Survived'] == 1].groupby('Pclass')['PassengerId'].count().to_dict()
        return survivors

    @staticmethod
    def get_passenger_names(data: pd.DataFrame) -> list:
        females_over_30_class_2 = data[(data['Age'] > 30) & 
                                       (data['Sex'] == 'female') & 
                                       (data['Pclass'] == 2)]['Name'].sort_values().tolist()
        return females_over_30_class_2

    @staticmethod
    def get_oldest_survived_passenger(data: pd.DataFrame) -> str:
        oldest_survived = data[data['Survived'] == 1].sort_values(by='Age', ascending=False).iloc[0]
        return oldest_survived['Name']


if __name__ == "__main__":
    # Question 1
    music = MusicFestival()
    music.create_tables()
    music.insert_data()

    res1 = music.query_1_get_artists_with_rock_genre()
    res2 = music.query_2_total_revenue_from_sales()
    res3 = music.query_3_number_performances()
    res4 = music.query_4_performances_on_specific_date()
    res5 = music.query_5_longer_performances()

    # Question 2
    titanic = Titanic()
    data = titanic.preprocess_data(filename="data/titanic_data.csv")

    ans1 = titanic.get_survived_count(data)
    ans2 = titanic.get_average_fare(data)
    ans3 = titanic.get_max_age(data)
    ans4 = titanic.get_min_age(data)
    ans5 = titanic.get_male_count(data)

    ans6 = titanic.get_died_under_30_count(data)
    ans7 = titanic.get_passenger_ids(data)
    ans8 = titanic.get_survivors_classwise(data)
    ans9 = titanic.get_passenger_names(data)
    ans10 = titanic.get_oldest_survived_passenger(data)
