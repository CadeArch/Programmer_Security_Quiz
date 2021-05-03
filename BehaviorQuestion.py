class BehaviorQuestion:

    def __init__(self, question, focus, suggestion):
        self.question = question
        self.focus = focus
        self.answer = None
        self.type = "Behavior Question"
        self.suggestion = suggestion

        if focus == "personal":
            self.weight = 2
        if focus == "workplace":
            self.weight = 1

    def getWeight(self):
        return self.weight

    def setAnswer(self, answer):
        self.answer = answer

    def getAnswer(self):
        return self.answer

    def getSuggestion(self):
        return self.suggestion

