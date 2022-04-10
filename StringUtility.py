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
 		return "".join([chr((ord(letter) + len(self.string) - (int(((ord(letter) + len(self.string))-65)/26)*26))) if letter.isupper() else (chr(ord(letter) + len(self.string) - (int(((ord(letter) + len(self.string))-97)/26)*26))) if letter.isalpha() else letter for letter in self.string])

def main():
  utility = StringUtility("watermelon")
  print(utility.vowels())
  print(utility.bothEnds)
  print(utility.fixStart)
  print(utility.asciiSum)
  print(utility.cipher)
  
if __name__ == "__main__":
    main()

        
    
      
      
      
    

    
    