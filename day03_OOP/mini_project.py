import json


class ChatUser:
    def __init__(self, name, plan="free"):
        self.name = name
        self.plan = plan
        self.queries = 0

    def ask(self):
        self.queries += 1
        return f"Query #{self.queries} submitted"

    def info(self):
        return f"{self.name} | plan: {self.plan} | queries: {self.queries}"


class PremiumUser(ChatUser):
    def __init__(self, name):
        super().__init__(name, plan="pro")
        self.priority_support = True

    def ask(self):
        self.queries += 1
        return f"[PRIORITY] Query #{self.queries} submitted"


class Conversation:
    def __init__(self):
        self.messages = []

    def __str__(self):
        return f"Conversation with {len(self.messages)} messages"

    def __len__(self):
        return len(self.messages)

    def add_user(self, content):
        self.messages.append({"role": "user", "content": content})

    def add_assistant(self, content):
        self.messages.append({"role": "assistant", "content": content})

    def history(self):
        lines = []
        for message in self.messages:
            lines.append(f"{message['role']}: {message['content']}")
        return "\n".join(lines)

    def count_user_messages(self):
        return sum(1 for message in self.messages if message["role"] == "user")

    def save(self, path):
        with open(path, "w") as file:
            json.dump(self.messages, file, indent=2)

    def load(self, path):
        with open(path, "r") as file:
            self.messages = json.load(file)


class Session:
    def __init__(self, user):
        self.user = user
        self.convo = Conversation()

    def ask(self, question):
        result = self.user.ask()
        self.convo.add_user(question)
        return result

    def summary(self):
        return f"{self.user.name} | messages: {len(self.convo)}"


class SessionManager:
    def __init__(self):
        self.sessions = {}

    def start_session(self, user):
        self.sessions[user.name] = Session(user)

    def ask(self, username, question):
        session = self.sessions.get(username)
        if session is None:
            return f"No session for {username}"
        return session.ask(question)

    def save_all(self, folder):
        for username, session in self.sessions.items():
            session.convo.save(f"{folder}/{username}_convo.json")

    def report(self):
        lines = []
        for session in self.sessions.values():
            lines.append(session.summary())
        return "\n".join(lines)


if __name__ == "__main__":
    manager = SessionManager()
    manager.start_session(ChatUser("Ali"))
    manager.start_session(PremiumUser("Zara"))

    print(manager.ask("Ali", "How do I renew my CNIC?"))
    print(manager.ask("Zara", "What are FBR filing deadlines?"))
    print(manager.ask("Ali", "What documents do I need?"))
    print(manager.ask("Bilal", "Hello?"))

    print()
    print(manager.report())

    manager.save_all("day03_OOP")