from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import pyodbc


class ActionPlan(Action):
    def name(self):
        return 'action_plan'

    def run(self, dispatcher, tracker, domain):
        plan = tracker.get_slot('plan')
        connection = pyodbc.connect(
            'Driver={SQL Server Native Client 11.0};'
            'Server=ServerName;'
            'Database=DBName;'
            'Trusted_Connection=yes;'
        )
        cursor = connection.cursor()
        query = "query to fetch details from the database"
        cursor.execute(query)

        for row in cursor:
            response = row[0]
            dispatcher.utter_message(response)

        return [SlotSet('plan', plan)]

