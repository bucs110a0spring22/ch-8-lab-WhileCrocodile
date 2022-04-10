class StringUtility:
  def __init__(self, string):
    self.string = string

  def __str__(self):
    return self.string

  def vowels(self):
    return "many" if len([letter for letter in self.string if letter in "aeiouAEIOU"]) >= 5 else str(len([letter for letter in self.string if letter in "aeiouAEIOU"]))

  def bothEnds(self):
    return self.string[:2] + self.string[-2:]

  def fixStart(self):
    return self.string[:1] + "".join(["*" if self.string[index] == self.string[:1] else self.string[index] for index in range(1, len(self.string))])

  def asciiSum(self):
    return sum([ord(letter) for letter in self.string])

  def cipher(self):
    new_string = ""
    for letter in self.string:
      if letter.isalpha():
        new_letter = ord(letter) + len(self.string)
        if letter.isupper() and new_letter > 90:
          while new_letter > 90:
            new_letter -= 26
        elif letter.islower() and new_letter > 122:
          while new_letter > 122:
            new_letter -= 26
        new_letter = chr(new_letter)
        new_string += new_letter
      else:
        new_string += letter
    return new_string

def main():
  utility = StringUtility("watermelon")
  print(utility.vowels())
  print(utility.bothEnds)
  print(utility.fixStart)
  print(utility.asciiSum)
  print(utility.cipher)
  
if __name__ == "__main__":
    main()

        
    
      
      
      
    

    
    