import json

def match_bot(lookup, message, inspire_message):
  message = message.lower()
  if "inspire" in message:
    return inspire_message()
  for key in lookup.keys():
    if key in message:
      return lookup[key]
  
def empty():
  return None

def inspiration():
  return "I am inspired"

def test_midterm() :
  result = match_bot({"midterm" : "None"}, "midterm yay", empty)
  assert result == "None"

def test_midterm_insensitive() :
  result = match_bot({"midterm" : "None"}, "MidTerm", empty)
  assert result == "None"

def test_final() :
  result = match_bot({"final" : "None"}, "final yay!", empty)
  assert result == "None"

def test_no_match() :
  result = match_bot({"final" : "none"}, "cry", empty)
  assert result == None

def test_with_dict() :
  with open("responses.json") as f:
    responses = json.loads(f.read())
  result = match_bot( responses, "midterm", empty)
  assert result == "The midterm is now and everything is on it"

def test_inspire() :
  result = match_bot({}, "inspire", inspiration)
  assert result == inspiration()