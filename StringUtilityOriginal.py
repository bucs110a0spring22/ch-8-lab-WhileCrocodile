class StringUtility:
  def __init__(self, string):
    self.string = string

  def __str__(self):
    return self.string

  def vowels(self):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for letter in self.string:
      if letter in vowels:
        vowel_count += 1
    if vowel_count >= 5:
      return "many"
    else:
      return str(vowel_count)

  def bothEnds(self):
    new_string = ""
    new_string += self.string[:2]
    new_string += self.string[-2:]
    return new_string

  def fixStart(self):
    first_char = self.string[:1]
    new_string = self.string[:1]
    for index in range(1, len(self.string)):
      if self.string[index] == first_char:
        new_string += "*"
      else:
        new_string += self.string[index]
    return new_string

  def asciiSum(self):
    sum = 0
    for letter in self.string:
      sum += ord(letter)
    return sum

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

        
    
      
      
      
    

    
    