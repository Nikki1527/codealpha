import random
class Chatbot:
  def __init__(self, pairs, reflections={}, use_reflection=True):
    self.pairs = pairs
    self.reflections = reflections
    self.use_reflection = use_reflection
  def chat(self):
    print("Hi! I'm a simple chatbot. How can I help you today?")
    while True:
      user_input = input("You: ")
      if user_input.lower() == "quit":
        break
      response = self.get_response(user_input)
      print("Chatbot: ", response)
  def get_response(self, user_input):
    user_input = user_input.lower()
    for pair in self.pairs:
      if user_input in pair[0]:
        return random.choice(pair[1])
    if self.use_reflection and user_input in self.reflections:
      return random.choice(self.reflections[user_input])
    return "Sorry, I don't understand what you mean."
pairs = [
  (["hi", "hello", "howdy"], ["Hi there!", "Greetings!", "Hey! How can I help you?"]),
  (["what's your name", "who are you"], ["I'm a simple chatbot."]),
  (["how are you", "doing well"], ["I'm doing great, thanks for asking!"]),
  (["what can you do", "what are your capabilities"], ["I can hold basic conversations and understand simple greetings and questions."]),
]
reflections = {
  "i am sad": ["Why are you sad?", "I'm sorry to hear that. Can I help in any way?"],
  "i am happy": ["That's great to hear!", "I'm glad you're happy!"]
}
my_chatbot = Chatbot(pairs, reflections, use_reflection=True)
my_chatbot.chat()
