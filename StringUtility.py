class StringUtility:
  def __init__(self, string="string"):
    '''
    Initializes the StringUtility object.
    string: (str) string to be transformed
    '''
    self.string = string

  def __str__(self):
    '''
    Returns the string used for StringUtility.
    return: (str) original string passed to StringUtility
    '''
    return self.string

  def vowels(self):
    '''
    Counts the number of vowels in a string.
    return: (str) the number of vowels in a given string
    '''
    return "many" if len([letter for letter in self.string if letter in "aeiouAEIOU"]) >= 5 else str(len([letter for letter in self.string if letter in "aeiouAEIOU"]))

  def bothEnds(self):
    '''
    Returns a new string with only the first and last two characters.
    return: (str) a string with only two characters from both ends.
    '''
    return self.string[:2] + self.string[-2:]

  def fixStart(self):
    '''
    Replaces all occurences of the first character of a string with "*"
    (except the first character itself)
    return: (str) the asterick-modified string.
    '''
    return self.string[:1] + "".join(["*" if self.string[index] == self.string[:1] else self.string[index] for index in range(1, len(self.string))])

  def asciiSum(self):
    '''
    Returns the sum of all ascii values in the string.
    return: (int) the sum of all ascii values in a string
    '''
    return sum([ord(letter) for letter in self.string])

  def cipher(self):
    '''
    Returns a ciphered string with all character shifted to the right
    by the same amount as the full length of the string (looped around
    from a --> z if necessary)
    return: (str) ciphered string
    '''
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

        
    
      
      
      
    

    
    